import cv2
import numpy as np
import os

# Constantes configurables
PNG_NAME = "gafas.png"
SCALE = 1.0
POSITION_OFFSET = (0, -20)  # (x, y) offset desde el centro de la cara
ROTATION = 0  # grados
OPACITY = 0.8

def get_script_directory():
    """Obtiene el directorio donde está ubicado este script"""
    return os.path.dirname(os.path.abspath(__file__))

def load_overlay_image():
    """Carga la imagen de las gafas desde el mismo directorio del script"""
    script_dir = get_script_directory()
    overlay_path = os.path.join(script_dir, PNG_NAME)
    
    if not os.path.exists(overlay_path):
        raise FileNotFoundError(f"No se encontró {PNG_NAME} en {script_dir}")
    
    # Cargar imagen con canal alpha
    overlay = cv2.imread(overlay_path, cv2.IMREAD_UNCHANGED)
    if overlay is None:
        raise ValueError(f"No se pudo cargar la imagen {PNG_NAME}")
    
    return overlay

def rotate_image(image, angle):
    """Rota una imagen dado un ángulo en grados"""
    if angle == 0:
        return image
    
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    return rotated

def overlay_image_alpha(background, overlay, x, y, alpha=1.0):
    """Superpone una imagen con canal alpha sobre otra"""
    h, w = overlay.shape[:2]
    
    # Verificar límites
    if x < 0 or y < 0 or x + w > background.shape[1] or y + h > background.shape[0]:
        return background
    
    # Extraer la región de interés del fondo
    roi = background[y:y+h, x:x+w]
    
    if overlay.shape[2] == 4:  # Si tiene canal alpha
        # Separar canales RGB y alpha
        overlay_rgb = overlay[:, :, :3]
        overlay_alpha = overlay[:, :, 3] / 255.0 * alpha
        
        # Aplicar alpha blending
        for c in range(3):
            roi[:, :, c] = roi[:, :, c] * (1 - overlay_alpha) + overlay_rgb[:, :, c] * overlay_alpha
    else:  # Sin canal alpha
        roi = cv2.addWeighted(roi, 1-alpha, overlay, alpha, 0)
    
    background[y:y+h, x:x+w] = roi
    return background

def main():
    # Cargar imagen de gafas
    try:
        gafas = load_overlay_image()
        print(f"Imagen {PNG_NAME} cargada correctamente desde {get_script_directory()}")
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Aplicar rotación si es necesaria
    if ROTATION != 0:
        gafas = rotate_image(gafas, ROTATION)
    
    # Inicializar detector de caras
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Inicializar cámara
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara")
        return
    
    print("Presiona 'q' para salir")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convertir a escala de grises para detección
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detectar caras
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Superponer gafas en cada cara detectada
        for (x, y, w, h) in faces:
            # Calcular tamaño de las gafas basado en el ancho de la cara
            gafas_width = int(w * SCALE)
            gafas_height = int(gafas.shape[0] * (gafas_width / gafas.shape[1]))
            
            # Redimensionar gafas
            gafas_resized = cv2.resize(gafas, (gafas_width, gafas_height))
            
            # Calcular posición de superposición
            gafas_x = x + (w - gafas_width) // 2 + POSITION_OFFSET[0]
            gafas_y = y + h // 3 + POSITION_OFFSET[1]  # Aproximadamente donde están los ojos
            
            # Superponer gafas
            frame = overlay_image_alpha(frame, gafas_resized, gafas_x, gafas_y, OPACITY)
            
            # Opcional: dibujar rectángulo de detección (comentar si no se desea)
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Mostrar resultado
        cv2.imshow('Gafas AR', frame)
        
        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Limpiar recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()