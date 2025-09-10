import cv2
import numpy as np

# Programa simple para contar objetos usando la webcam
# Detecta objetos oscuros sobre fondo claro (o viceversa)

def main():
    # Inicializar la cámara web
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: No se puede acceder a la cámara")
        return
    
    print("Instrucciones:")
    print("- Pon objetos oscuros sobre fondo claro")
    print("- Presiona 't' para cambiar entre modo claro/oscuro")
    print("- Presiona 'q' para salir")
    
    # Variable para cambiar entre detectar objetos oscuros u objetos claros
    detect_dark_objects = True
    
    while True:
        # PASO 1: Capturar frame de la cámara
        ret, frame = cap.read()
        if not ret:
            break
        
        # Voltear imagen (efecto espejo)
        frame = cv2.flip(frame, 1)
        
        # PASO 2: Convertir a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # PASO 3: Aplicar desenfoque para reducir ruido
        # El desenfoque ayuda a eliminar pequeños detalles que pueden confundir la detección
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)
        
        # PASO 4: Binarizar la imagen (convertir a blanco y negro puro)
        # THRESH_BINARY: pixels < threshold = 0 (negro), pixels >= threshold = 255 (blanco)
        # THRESH_BINARY_INV: lo contrario
        if detect_dark_objects:
            # Detectar objetos oscuros (aparecen en blanco en la imagen binaria)
            _, binary = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)
            mode_text = "Detectando objetos OSCUROS"
        else:
            # Detectar objetos claros (aparecen en blanco en la imagen binaria)
            _, binary = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
            mode_text = "Detectando objetos CLAROS"
        
        # PASO 5: Operaciones morfológicas para limpiar la imagen
        # Crear un kernel (elemento estructurante) circular
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
        
        # Opening: elimina ruido pequeño (erosión seguida de dilatación)
        cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        
        # PASO 6: Encontrar contornos (bordes de los objetos)
        contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # PASO 7: Filtrar contornos por tamaño y contar objetos
        min_area = 500    # Área mínima para considerar un objeto
        max_area = 50000  # Área máxima para evitar contar el fondo completo
        valid_objects = 0
        
        # Crear una copia del frame original para dibujar
        result = frame.copy()
        
        # Procesar cada contorno encontrado
        for i, contour in enumerate(contours):
            # Calcular el área del contorno
            area = cv2.contourArea(contour)
            
            # Si el área está en el rango válido, es un objeto
            if min_area < area < max_area:
                valid_objects += 1
                
                # Dibujar el contorno en verde
                cv2.drawContours(result, [contour], -1, (0, 255, 0), 2)
                
                # Obtener el rectángulo que encierra el objeto
                x, y, w, h = cv2.boundingRect(contour)
                
                # Dibujar rectángulo azul alrededor del objeto
                cv2.rectangle(result, (x, y), (x + w, y + h), (255, 0, 0), 2)
                
                # Escribir número del objeto
                cv2.putText(result, f"#{i+1}", (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # PASO 8: Mostrar información en pantalla
        # Contador de objetos
        cv2.putText(result, f"Objetos detectados: {valid_objects}", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        
        # Modo actual
        cv2.putText(result, mode_text, 
                   (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        
        # Instrucciones
        cv2.putText(result, "Presiona 't' para cambiar modo", 
                   (10, result.shape[0] - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(result, "Presiona 'q' para salir", 
                   (10, result.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # PASO 9: Mostrar las imágenes
        cv2.imshow('Imagen Original', result)
        cv2.imshow('Imagen Binaria (procesada)', cleaned)
        
        # PASO 10: Manejar teclas
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