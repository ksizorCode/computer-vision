import cv2
import numpy as np

# Seleccionar diccionario
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Generar marcador con ID=42
marker_id = 42
marker_size = 200  # en píxeles
marker_img = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

# Guardar como PNG
cv2.imwrite("aruco_marker_42.png", marker_img)

cv2.imshow("ArUco Marker", marker_img)
cv2.waitKey(0)
cv2.destroyAllWindows()