# Instalar OpenCV
# La instalación en local se realiza a través de Terminal o Línea de comandos:
# pip install opencv-python


# Para ejecutar el código pulsa Play y espera un momento a que se inicie la webcam.
# También puedes ejecutar el script desde la terminal o línea de comandos.

# --------------------------------------------------------------------------------

import cv2
import numpy as np

# Inicializa la webcam
cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if ret==True:
        # Convertir a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Aplicar Canny
        edges = cv2.Canny(gray, 100, 200)
        # Mostrar imagen original y bordes
        cv2.imshow('frame',frame)
        cv2.imshow('Canny',edges)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
