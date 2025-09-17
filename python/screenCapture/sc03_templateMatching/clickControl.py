# importar paquetes necesarios
import cv2
import numpy as np
import pyautogui
import os
import time

# ----------------------- CONSTANTES -----------------------
TEMPLATE_FOLDER = "detectar"  # carpeta donde están las imágenes que usarás como plantilla
ITERACIONES = 10               # número de veces que se ejecutará la detección
DELAY = 1                    # segundos entre cada iteración
CONFIDENCE_THRESHOLD = 0.8    # confianza mínima para considerar una coincidencia
SCROLL_PIXELS = -800          # píxeles a desplazar tras cada iteración (negativo = bajar)
# ----------------------------------------------------------

# función para cargar todas las plantillas de la carpeta
def cargar_plantillas(folder):
    plantillas = []
    for archivo in os.listdir(folder):
        ruta = os.path.join(folder, archivo)
        # comprobar que es un archivo de imagen
        if os.path.isfile(ruta) and archivo.lower().endswith((".png", ".jpg", ".jpeg")):
            img = cv2.imread(ruta)
            plantillas.append((archivo, img))
    return plantillas

# función para detectar plantillas en la pantalla y hacer click
def detectar_y_click(plantillas):
    # tomar captura de pantalla completa
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    for nombre, plantilla in plantillas:
        # obtener tamaño de la plantilla
        h, w = plantilla.shape[:2]

        # hacer template matching
        res = cv2.matchTemplate(screenshot, plantilla, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        print(f"[INFO] {nombre}: max_val = {max_val:.2f}")  # mostrar confianza encontrada

        # si la coincidencia es mayor que la confianza mínima, hacemos click
        if max_val >= CONFIDENCE_THRESHOLD:
            centro_x = max_loc[0] + w // 2
            centro_y = max_loc[1] + h // 2
            pyautogui.click(centro_x, centro_y)
            print(f"[CLICK] Haciendo click en {nombre} en ({centro_x}, {centro_y})")

# ---------------------- PROGRAMA PRINCIPAL ----------------------
if __name__ == "__main__":
    plantillas = cargar_plantillas(TEMPLATE_FOLDER)
    print(f"[INFO] Se cargaron {len(plantillas)} plantillas.")

    for i in range(ITERACIONES):
        print(f"\n[ITERACION {i+1}/{ITERACIONES}] Detectando y haciendo click...")
        detectar_y_click(plantillas)
        
        # hacer scroll tras la iteración
        pyautogui.scroll(SCROLL_PIXELS)
        print(f"[SCROLL] Desplazando {abs(SCROLL_PIXELS)} píxeles hacia abajo.")
        
        time.sleep(DELAY)

    print("\n[INFO] Proceso completado.")
