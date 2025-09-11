# Versión optimizada y simplificada de ar_000C_MarkerRandomLoop.py
# (hace lo mismo pero con menos código)

import cv2
import numpy as np
import os

def generar_marcadores(cantidad=5):
    # Configuración
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    
    # Crear carpeta
    carpeta = os.path.join(os.path.dirname(__file__), "marcadores")
    os.makedirs(carpeta, exist_ok=True)
    
    # Generar marcadores
    for i in range(cantidad):
        # ID aleatorio y generar imagen
        id_marcador = np.random.randint(0, 250)
        imagen = cv2.aruco.generateImageMarker(aruco_dict, id_marcador, 200)
        
        # Guardar archivo
        nombre = f"aruco_marker_{id_marcador:03d}.png"
        ruta = os.path.join(carpeta, nombre)
        cv2.imwrite(ruta, imagen)
        
        # Mostrar
        print(f"Marcador {i+1}: ID {id_marcador} guardado como {nombre}")
        cv2.imshow(f"Marcador {i+1}", imagen)
    
    # Esperar y cerrar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ejecutar
generar_marcadores(5)