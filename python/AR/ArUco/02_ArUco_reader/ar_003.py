import cv2
import numpy as np
import os

# Configuración básica
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)

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
    corners, ids, _ = detector.detectMarkers(gray)
    
    if ids is not None and len(ids) > 0:
        # Dibujar marcadores detectados
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
        try:
            # Estimación de pose para cada marcador individualmente
            for i, corner in enumerate(corners):
                # Usar solvePnP en lugar de estimatePoseSingleMarkers
                object_points = np.array([
                    [-marker_size/2,  marker_size/2, 0],
                    [ marker_size/2,  marker_size/2, 0],
                    [ marker_size/2, -marker_size/2, 0],
                    [-marker_size/2, -marker_size/2, 0]
                ], dtype=np.float32)
                
                success, rvec, tvec = cv2.solvePnP(
                    object_points, 
                    corner.reshape(-1, 2), 
                    camera_matrix, 
                    dist_coeffs
                )
                
                if success:
                    cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, rvec, tvec, 0.03)
                    
        except Exception as e:
            print(f"Error en estimación de pose: {e}")
            # Solo dibujar marcadores sin pose
            pass
    
    cv2.imshow('AR Simple', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()