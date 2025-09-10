import cv2
import numpy as np

# Cargar diccionario ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Cargar la imagen a superponer
overlay = cv2.imread("imagenAR.png")

# Inicializar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar marcadores
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    if ids is not None:
        for corner in corners:
            # Coordenadas del marcador detectado (en la imagen de la webcam)
            pts_dst = corner[0].astype(np.float32)

            # Redimensionar overlay al tamaño del marcador
            h, w, _ = overlay.shape
            pts_src = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)

            # Calcular homografía (transformación de perspectiva)
            matrix, _ = cv2.findHomography(pts_src, pts_dst)

            # Warpear la imagen al área del marcador
            warped = cv2.warpPerspective(overlay, matrix, (frame.shape[1], frame.shape[0]))

            # Crear máscara para fusionar
            mask = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.uint8)
            cv2.fillConvexPoly(mask, pts_dst.astype(int), 255)
            mask_inv = cv2.bitwise_not(mask)

            # Quitar zona del marcador en el frame
            frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)

            # Añadir overlay warpeado
            frame = cv2.add(frame_bg, warped)
    
    cv2.imshow('AR Markers', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()