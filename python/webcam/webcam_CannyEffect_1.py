import cv2

def main():
    """
    Programa básico que captura video de la cámara web
    y aplica el filtro Canny para detección de bordes
    """
    # Inicializar la cámara (0 = cámara por defecto)
    cap = cv2.VideoCapture(0)
    
    # Verificar que la cámara se abrió correctamente
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara")
        return
    
    # Crear ventanas para mostrar las imágenes
    cv2.namedWindow('Video Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Bordes Detectados', cv2.WINDOW_NORMAL)
    
    print("Detector de bordes Canny activado")
    print("Presiona 'q' para salir del programa")
    
    # Bucle principal
    while True:
        # Capturar un frame de la cámara
        ret, frame = cap.read()
        
        # Si no se pudo leer el frame, salir del bucle
        if not ret:
            print("Error al leer el frame de la cámara")
            break
        
        # PASO 1: Convertir la imagen a escala de grises
        # Canny requiere una imagen en escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # PASO 2: Aplicar el detector de bordes Canny
        # Parámetros: imagen, umbral_mínimo, umbral_máximo
        # Umbral bajo (50) = detecta más bordes (incluso débiles)
        # Umbral alto (150) = solo bordes fuertes
        bordes = cv2.Canny(gris, 2, 30)
        
        # PASO 3: Mostrar las imágenes en las ventanas
        cv2.imshow('Video Original', frame)
        cv2.imshow('Bordes Detectados', bordes)
        
        # PASO 4: Verificar si se presionó la tecla 'q' para salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Saliendo del programa...")
            break
    
    # PASO 5: Limpiar recursos
    cap.release()           # Liberar la cámara
    cv2.destroyAllWindows() # Cerrar todas las ventanas


def que_hace_canny():
    """
    Función educativa que explica qué hace el detector Canny
    """
    print("=== ¿QUÉ HACE EL DETECTOR CANNY? ===")
    print("Encuentra los bordes (contornos) de los objetos en la imagen")
    print("- Analiza dónde cambia bruscamente la intensidad de los píxeles")
    print("- Convierte la imagen a blanco y negro:")
    print("  * BLANCO = hay un borde")
    print("  * NEGRO = no hay borde")
    print()
    print("PARÁMETROS USADOS:")
    print("- Umbral mínimo: 50 (bordes débiles)")
    print("- Umbral máximo: 150 (bordes fuertes)")
    print("- A mayor umbral = menos bordes detectados")
    print("- A menor umbral = más bordes detectados")
    print()


if __name__ == "__main__":
    # Mostrar explicación
    que_hace_canny()
    
    # Ejecutar el programa
    main()