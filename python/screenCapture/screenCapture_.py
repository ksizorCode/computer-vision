import cv2
import numpy as np
from PIL import ImageGrab
import time

def capturar_pantalla_canny():
    """
    Captura la pantalla y aplica el filtro Canny para detectar bordes
    """
    while True:
        # Capturar la pantalla
        screenshot = ImageGrab.grab()
        
        # Convertir PIL Image a formato OpenCV
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        # Convertir a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Aplicar desenfoque gaussiano para reducir ruido
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Aplicar filtro Canny
        # Parámetros: imagen, umbral_bajo, umbral_alto
        edges = cv2.Canny(blurred, 50, 150)
        
        # Redimensionar ventanas para que no sean demasiado grandes
        height, width = frame.shape[:2]
        if width > 1200:
            scale = 1200 / width
            new_width = int(width * scale)
            new_height = int(height * scale)
            
            frame = cv2.resize(frame, (new_width, new_height))
            edges = cv2.resize(edges, (new_width, new_height))
        
        # Mostrar las ventanas
        cv2.imshow('Pantalla Original', frame)
        cv2.imshow('Detección de Bordes (Canny)', edges)
        
        # Salir con 'q' o 'ESC'
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:
            break
        
        # Pequeña pausa para no sobrecargar el CPU
        time.sleep(0.01)
    
    # Cerrar ventanas
    cv2.destroyAllWindows()

def captura_unica_canny():
    """
    Hace una captura única y guarda el resultado
    """
    # Capturar la pantalla
    screenshot = ImageGrab.grab()
    
    # Convertir a formato OpenCV
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Aplicar filtro Canny
    edges = cv2.Canny(gray, 50, 150)
    
    # Guardar las imágenes
    cv2.imwrite('pantalla_original.png', frame)
    cv2.imwrite('pantalla_canny.png', edges)
    
    print("Imágenes guardadas:")
    print("- pantalla_original.png")
    print("- pantalla_canny.png")
    
    # Mostrar resultados
    cv2.imshow('Original', frame)
    cv2.imshow('Canny', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Selecciona una opción:")
    print("1. Captura en tiempo real (presiona 'q' para salir)")
    print("2. Captura única y guardar")
    
    opcion = input("Opción (1 o 2): ")
    
    if opcion == "1":
        print("Iniciando captura en tiempo real...")
        print("Presiona 'q' o ESC para salir, 's' para guardar")
        time.sleep(2)  # Dar tiempo para cambiar de ventana
        capturar_pantalla_canny()
    elif opcion == "2":
        print("Haciendo captura única en 3 segundos...")
        time.sleep(3)  # Dar tiempo para preparar la pantalla
        captura_unica_canny()
    else:
        print("Opción no válida")