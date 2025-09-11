import cv2
import numpy as np
import os

# Configuración básica
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Cargar imagen
script_dir = os.path.dirname(__file__)
img_path = os.path.join(script_dir, "img_aruco", "imagenAR.png")
overlay = cv2.imread(img_path)

if overlay is None:
    print("No se pudo cargar la imagen")
    exit()

# Parámetros simplificados
camera_matrix = np.array([[600, 0, 320], [0, 600, 240], [0, 0, 1]], dtype=np.float32)
dist_coeffs = np.zeros((4, 1))
marker_size = 0.05

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    if ids is not None:
        # Solo dibujar marcadores detectados (sin 3D)
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
        # Opcional: añadir estimación de pose simple
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, dist_coeffs)
        for rvec, tvec in zip(rvecs, tvecs):
            cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvec, tvec, 0.03)
    
    cv2.imshow('AR Simple', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()