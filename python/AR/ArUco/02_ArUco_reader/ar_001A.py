# Detectar y dibujar sobre marcador ArUco el ID de marcador
# Requiere una cámara conectada al ordenador

import cv2
import numpy as np

# Cargar diccionario ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)


# Inicializar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar marcadores
    corners, ids, _ = detector.detectMarkers(gray)  # Usar el detector
    
    # Dibujar marcadores detectados
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
    
    cv2.imshow('AR Markers', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()