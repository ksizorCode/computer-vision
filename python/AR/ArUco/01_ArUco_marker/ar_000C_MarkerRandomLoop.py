# VERSIÓN AVANZADA

# Generar y guardar un marcador ArUco con ID aleatorio usando OpenCV
# Este código también guarda los marcadores junto a este archivo

import cv2
import numpy as np
import os

# constantes
MARCADORES_A_GENERAR = 5  # número de marcadores a generar
DICCIONARIO = cv2.aruco.DICT_6X6_250  # diccionario ArUco a usar
POSIBILES_IDS = 250  # número de IDs posibles en el diccionario
TAMANO_MARCADOR = 200  # tamaño del marcador en píxeles

# Seleccionar diccionario
aruco_dict = cv2.aruco.getPredefinedDictionary(DICCIONARIO)

def generar_id_marcador():
    # Número entero aleatorio
    aleatorio = np.random.randint(0, 250)  # entre 0-249 para DICT_6X6_250
    print(f"ID del marcador generado: {aleatorio}")

    # Formatear para nombre de archivo (más simple con f-string)
    aleatoriobonito = f"{aleatorio:03d}"  # Siempre 3 dígitos con ceros delante
    print(f"ID del marcador formateado: {aleatoriobonito}")

    # Generar marcador
    marker_id = aleatorio  # ID del marcador (mantener como int)
    marker_size = TAMANO_MARCADOR  # en píxeles
    marker_img = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)

    # Crear carpeta 'marcadores' junto al script si no existe
    script_dir = os.path.dirname(__file__)
    output_dir = os.path.join(script_dir, "marcadores")
    os.makedirs(output_dir, exist_ok=True)

    # Ruta completa del archivo
    file_path = os.path.join(output_dir, f"aruco_marker_{aleatoriobonito}.png")

    # Guardar como PNG
    cv2.imwrite(file_path, marker_img)
    print(f"Marcador guardado en: {file_path}")
    
    return marker_img

# Generar X marcadores aleatorios
print(f"Generando {MARCADORES_A_GENERAR} marcadores ArUco...")
marcadores = [] # array para guardar los marcadores generados

for i in range(MARCADORES_A_GENERAR):
    print(f"\n--- Marcador {i+1}/{MARCADORES_A_GENERAR} ---")
    marker_img = generar_id_marcador()
    marcadores.append(marker_img)

# Mostrar todos los marcadores generados
print(f"\nMostrando {len(marcadores)} marcadores generados...")
for i, marker_img in enumerate(marcadores):
    cv2.imshow(f"ArUco Marker {i+1}", marker_img)

cv2.waitKey(0)  
cv2.destroyAllWindows() 