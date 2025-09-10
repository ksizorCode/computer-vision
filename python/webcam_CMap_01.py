import cv2
import numpy as np

# Programa simple para aplicar un colormap efectista a la webcam
# Perfecto como ejemplo base para clases de visión por computadora

def main():
    # Inicializar la cámara web (0 es la cámara por defecto)
    cap = cv2.VideoCapture(0)
    
    # Verificar que la cámara se haya abierto correctamente
    if not cap.isOpened():
        print("Error: No se puede acceder a la cámara")
        return
    
    print("Presiona 'q' para salir")
    
    # Bucle principal para capturar y mostrar frames
    while True:
        # Capturar un frame de la cámara
        ret, frame = cap.read()
        
        # Verificar que el frame se haya capturado correctamente
        if not ret:
            print("Error: No se puede leer el frame")
            break
        
        # Voltear la imagen horizontalmente (efecto espejo)
        frame = cv2.flip(frame, 1)
        
        # PASO 1: Convertir imagen a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # PASO 2: Aplicar colormap efectista
        # COLORMAP_JET: azul (frío) -> verde -> amarillo -> rojo (caliente)
        colored = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
        
        # Opcional: Otros colormaps efectistas que puedes probar:
        # colored = cv2.applyColorMap(gray, cv2.COLORMAP_HOT)      # Negro -> rojo -> amarillo -> blanco
        # colored = cv2.applyColorMap(gray, cv2.COLORMAP_RAINBOW)  # Arcoíris completo
        # colored = cv2.applyColorMap(gray, cv2.COLORMAP_PLASMA)   # Púrpura -> rosa -> amarillo
        # colored = cv2.applyColorMap(gray, cv2.COLORMAP_INFERNO)  # Negro -> púrpura -> rojo -> amarillo
        
        # PASO 3: Mostrar ambas imágenes
        # Imagen original en escala de grises
        cv2.imshow('Imagen Original (Grises)', gray)
        
        # Imagen con colormap aplicado
        cv2.imshow('Imagen con Colormap JET', colored)
        
        # PASO 4: Detectar si el usuario presiona 'q' para salir
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    
    # PASO 5: Liberar recursos y cerrar ventanas
    cap.release()              # Liberar la cámara
    cv2.destroyAllWindows()    # Cerrar todas las ventanas

# Ejecutar el programa principal
if __name__ == "__main__":
    main()