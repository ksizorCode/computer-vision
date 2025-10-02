
#pip install pyinstaller


import cv2

def main():
    # Abrir cámara (0 = cámara principal)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("No se pudo abrir la cámara")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame")
            break

        # Aplica un colormap
        frame_colormap = cv2.applyColorMap(frame, cv2.COLORMAP_JET)

        # Añade texto "Hola Mundo"
        cv2.putText(frame_colormap,
                    "Hola Mundo Texto aquí",
                    (50, 50),                  # posición
                    cv2.FONT_HERSHEY_SIMPLEX,  # fuente
                    1,                         # tamaño
                    (255, 255, 255),           # color blanco
                    2,                         # grosor
                    cv2.LINE_AA)

        # Mostrar ventana
        cv2.imshow("Webcam con filtro", frame_colormap)

        # Salir con "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
