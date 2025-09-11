import cv2

# Generar marcador ArUco ID=0
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
marker = cv2.aruco.generateImageMarker(aruco_dict, 0, 200)
cv2.imwrite('marker_0.png', marker) #la imagen se guarda en la raiz del proyecto github