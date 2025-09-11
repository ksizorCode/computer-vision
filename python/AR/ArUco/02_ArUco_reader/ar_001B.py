# Igual que la versión anterior pero con mejoras estéticas 

# Detectar y dibujar sobre marcador ArUco el ID de marcador
# Requiere una cámara conectada al ordenador


import cv2
import numpy as np

#Versión de OpenCV
print(f"OpenCV version: {cv2.__version__}")
#print(f"OpenCV build info:\n{cv2.getBuildInformation()}")

# Cargar diccionario ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()
detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)  #Nueva forma en OpenCV 4.7.0



# Inicializar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
    # Detectar marcadores
    corners, ids, _ = detector.detectMarkers(gray)  # Cambio aquí OpenCV 4.7.0
        
    # Dibujar marcadores detectados
    if ids is not None:
        # Dibujar contornos de los marcadores
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
        # Dibujar IDs personalizados
        for i, corner in enumerate(corners):
            # Calcular centro del marcador
            center = np.mean(corner[0], axis=0).astype(int)
            
            # ID del marcador
            marker_id = ids[i][0]
            
            # Dibujar ID con fuente más grande y personalizada
            cv2.putText(frame, 
                       f"ID: {marker_id}", 
                       (center[0] - 30, center[1] - 40),  # Posición arriba del marcador
                       cv2.FONT_HERSHEY_SIMPLEX,          # Fuente
                       1.5,                               # Escala (más grande)
                       (0, 255, 0),                       # Color verde
                       3,                                 # Grosor
                       cv2.LINE_AA)                       # Antialiasing
        
    cv2.imshow('AR Markers', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()