import cv2
import numpy as np
from pathlib import Path

# Cargar diccionario ArUco
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters()

# Ruta de la imagen usando pathlib
script_path = Path(__file__).parent
img_path = script_path / "img_aruco" / "imagenAR.png"

# Verificar si existe la imagen
if not img_path.exists():
    print(f"Error: No se encontró la imagen en {img_path}")
    print("Asegúrate de que existe la carpeta 'img_aruco' con la imagen 'imagenAR.png'")
    exit()

# Cargar la imagen a superponer
overlay = cv2.imread(str(img_path))

if overlay is None:
    print(f"Error: No se pudo cargar la imagen desde {img_path}")
    exit()

print(f"Imagen cargada desde: {img_path}")

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
            # Coordenadas del marcador detectado
            pts_dst = corner[0].astype(np.float32)

            # Coordenadas de la imagen overlay
            h, w, _ = overlay.shape
            pts_src = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)

            # Calcular homografía
            matrix, _ = cv2.findHomography(pts_src, pts_dst)

            # Warpear la imagen
            warped = cv2.warpPerspective(overlay, matrix, (frame.shape[1], frame.shape[0]))

            # Crear máscara
            mask = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.uint8)
            cv2.fillConvexPoly(mask, pts_dst.astype(int), 255)
            mask_inv = cv2.bitwise_not(mask)

            # Fusionar imágenes
            frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
            frame = cv2.add(frame_bg, warped)
    
    cv2.imshow('AR Markers', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()