import cv2
import numpy as np

# Programa simple para contar objetos usando la webcam con controles deslizantes
# Detecta objetos oscuros sobre fondo claro (o viceversa)

# Variables globales para los parámetros ajustables
threshold_value = 60
min_area = 500
max_area = 50000
blur_kernel = 11
morph_kernel = 9

def create_trackbars():
    """Crear ventana con controles deslizantes (trackbars)"""
    cv2.namedWindow('Controles')
    
    # Crear trackbars para ajustar parámetros en tiempo real
    cv2.createTrackbar('Threshold', 'Controles', threshold_value, 255, lambda x: None)
    cv2.createTrackbar('Area Minima', 'Controles', min_area // 10, 1000, lambda x: None)  # Dividido por 10 para el slider
    cv2.createTrackbar('Area Maxima', 'Controles', max_area // 1000, 100, lambda x: None)  # Dividido por 1000
    cv2.createTrackbar('Desenfoque', 'Controles', blur_kernel, 31, lambda x: None)  # Solo valores impares
    cv2.createTrackbar('Morfologia', 'Controles', morph_kernel, 21, lambda x: None)
    
    # Crear un texto informativo en la ventana de controles
    info_img = np.zeros((200, 400, 3), dtype=np.uint8)
    cv2.putText(info_img, 'CONTROLES:', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(info_img, 'Threshold: Nivel de binarizacion', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
    cv2.putText(info_img, 'Area Min/Max: Tamano de objetos', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
    cv2.putText(info_img, 'Desenfoque: Suavizado de imagen', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
    cv2.putText(info_img, 'Morfologia: Limpieza de ruido', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
    cv2.putText(info_img, '', (10, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (100, 255, 100), 1)
    cv2.putText(info_img, 'Presiona "t" - cambiar modo', (10, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (100, 255, 100), 1)
    cv2.putText(info_img, 'Presiona "q" - salir', (10, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (100, 255, 100), 1)
    
    cv2.imshow('Controles', info_img)

def get_trackbar_values():
    """Obtener valores actuales de los trackbars"""
    global threshold_value, min_area, max_area, blur_kernel, morph_kernel
    
    threshold_value = cv2.getTrackbarPos('Threshold', 'Controles')
    min_area = cv2.getTrackbarPos('Area Minima', 'Controles') * 10  # Multiplicar por 10
    max_area = cv2.getTrackbarPos('Area Maxima', 'Controles') * 1000  # Multiplicar por 1000
    blur_kernel = cv2.getTrackbarPos('Desenfoque', 'Controles')
    morph_kernel = cv2.getTrackbarPos('Morfologia', 'Controles')
    
    # Asegurar que los kernels sean impares y mínimo 3
    if blur_kernel % 2 == 0:
        blur_kernel += 1
    if blur_kernel < 3:
        blur_kernel = 3
        
    if morph_kernel % 2 == 0:
        morph_kernel += 1
    if morph_kernel < 3:
        morph_kernel = 3
    
    # Asegurar que min_area < max_area
    if min_area >= max_area:
        min_area = max_area - 100

def main():
    # Inicializar la cámara web
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: No se puede acceder a la cámara")
        return
    
    print("Instrucciones:")
    print("- Pon objetos oscuros sobre fondo claro")
    print("- Usa los sliders para ajustar la detección")
    print("- Presiona 't' para cambiar entre modo claro/oscuro")
    print("- Presiona 'q' para salir")
    
    # Crear ventana de controles
    create_trackbars()
    
    # Variable para cambiar entre detectar objetos oscuros u objetos claros
    detect_dark_objects = True
    
    while True:
        # PASO 1: Capturar frame de la cámara
        ret, frame = cap.read()
        if not ret:
            break
        
        # Voltear imagen (efecto espejo)
        frame = cv2.flip(frame, 1)
        
        # PASO 2: Obtener valores actuales de los controles
        get_trackbar_values()
        
        # PASO 3: Convertir a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # PASO 4: Aplicar desenfoque (kernel dinámico desde slider)
        blurred = cv2.GaussianBlur(gray, (blur_kernel, blur_kernel), 0)
        
        # PASO 5: Binarizar la imagen (threshold dinámico desde slider)
        if detect_dark_objects:
            # Detectar objetos oscuros
            _, binary = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY_INV)
            mode_text = "Detectando objetos OSCUROS"
        else:
            # Detectar objetos claros  
            _, binary = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY)
            mode_text = "Detectando objetos CLAROS"
        
        # PASO 6: Operaciones morfológicas (kernel dinámico desde slider)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (morph_kernel, morph_kernel))
        cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        
        # PASO 7: Encontrar contornos
        contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # PASO 8: Filtrar contornos por tamaño (áreas dinámicas desde sliders)
        valid_objects = 0
        result = frame.copy()
        
        for i, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            
            # Usar valores dinámicos de min_area y max_area
            if min_area < area < max_area:
                valid_objects += 1
                
                # Dibujar contorno en verde
                cv2.drawContours(result, [contour], -1, (0, 255, 0), 2)
                
                # Rectángulo delimitador
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(result, (x, y), (x + w, y + h), (255, 0, 0), 2)
                
                # Número del objeto y área
                cv2.putText(result, f"#{i+1}", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(result, f"{int(area)}", (x, y+h+20), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
        
        # PASO 9: Mostrar información en pantalla
        cv2.putText(result, f"Objetos: {valid_objects}", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.putText(result, mode_text, 
                   (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        
        # Mostrar parámetros actuales
        cv2.putText(result, f"Threshold: {threshold_value}", 
                   (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(result, f"Area: {min_area}-{max_area}", 
                   (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(result, f"Blur: {blur_kernel}x{blur_kernel}", 
                   (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(result, f"Morph: {morph_kernel}x{morph_kernel}", 
                   (10, 170), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # PASO 10: Mostrar las imágenes
        cv2.imshow('Detector de Objetos', result)
        cv2.imshow('Imagen Binaria', cleaned)
        cv2.imshow('Imagen Desenfocada', blurred)
        
        # PASO 11: Manejar teclas
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('t'):
            detect_dark_objects = not detect_dark_objects
    
    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()