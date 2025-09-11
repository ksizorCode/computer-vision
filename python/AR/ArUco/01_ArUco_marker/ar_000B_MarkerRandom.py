# VERSIÓN INTERMEDIA

# Generar y guardar un marcador ArUco con ID=aleatorio usando OpenCV
# Este código también guarda los marcadores junto a este archivo

import cv2
import numpy as np
import os

# Seleccionar diccionario
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

# Número entero aleatorio
aleatorio = int(np.random.randint(0, 249))  # entre 0-249 para DICT_6X6_250
print(f"ID del marcador generado: {aleatorio}")

# aleatoriobonito para nombre de archivo
# si es mejor de 100, poner 0 delante para que tenga 3 dígitos siempre
aleatoriobonito = aleatorio
if aleatoriobonito < 100:
    if aleatoriobonito < 10:
        aleatoriobonito = f"00{aleatoriobonito}"
        print(f"ID del marcador se le ha añadido 00 delante")
    else:
        aleatoriobonito = f"0{aleatoriobonito}"
        print(f"ID del marcador se le ha añadido 0 delante")

print(f"ID del marcador formateado: {aleatoriobonito}")

# Generar y guardar marcador
marker_id = aleatorio # ID del marcador 
marker_size = 200  # en píxeles
marker_img = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

# Crear carpeta 'output' junto al script si no existe:

script_dir = os.path.dirname(__file__)          # Obtener la ruta del directorio donde está el script 

output_dir = os.path.join(script_dir, "marcadores") # Crear la ruta completa del archivo
os.makedirs(output_dir, exist_ok=True)          # Crear carpeta si no existe


# Ruta completa del archivo
file_path = os.path.join(output_dir, f"aruco_marker_{aleatoriobonito}.png")

# Guardar como PNG en la misma carpeta del script
cv2.imwrite(file_path, marker_img)


cv2.imshow("ArUco Marker", marker_img)
cv2.waitKey(0)
cv2.destroyAllWindows()