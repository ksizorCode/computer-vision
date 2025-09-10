import pyautogui
import cv2
import pytesseract
import numpy as np
import time
import sys
from PIL import Image

# Configuración inicial
pyautogui.FAILSAFE = True  # Mover mouse a esquina superior izquierda para parar
pyautogui.PAUSE = 0.5  # Pausa entre comandos

# Configurar ruta de tesseract (ajustar según tu instalación)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
# pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Linux
# pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'  # macOS

def capturar_pantalla():
    """Captura la pantalla completa"""
    screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

def buscar_texto_en_imagen(imagen, texto_objetivo):
    """Busca un texto específico en la imagen usando OCR"""
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar threshold para mejorar el reconocimiento
    _, threshold = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)
    
    # Configuración de tesseract
    config = '--psm 6'  # Assume uniform block of text
    
    try:
        # Extraer texto con coordenadas
        datos = pytesseract.image_to_data(threshold, config=config, output_type=pytesseract.Output.DICT)
        
        # Buscar el texto objetivo
        for i in range(len(datos['text'])):
            texto_encontrado = datos['text'][i].strip().upper()
            if texto_objetivo.upper() in texto_encontrado:
                x = datos['left'][i]
                y = datos['top'][i]
                w = datos['width'][i]
                h = datos['height'][i]
                
                # Calcular centro del texto/botón
                centro_x = x + w // 2
                centro_y = y + h // 2
                
                return (centro_x, centro_y)
    
    except Exception as e:
        print(f"Error en OCR: {e}")
        return None
    
    return None

def buscar_boton_siguiente():
    """Busca el botón SIGUIENTE en la pantalla actual"""
    print("Capturando pantalla...")
    imagen = capturar_pantalla()
    
    print("Buscando botón 'SIGUIENTE'...")
    coordenadas = buscar_texto_en_imagen(imagen, "SIGUIENTE")
    
    if coordenadas:
        print(f"Botón encontrado en coordenadas: {coordenadas}")
        return coordenadas
    else:
        # Intentar variaciones del texto
        variaciones = ["NEXT", "CONTINUAR", "ADELANTE", "SEGUIR"]
        for variacion in variaciones:
            print(f"Buscando variación: {variacion}")
            coordenadas = buscar_texto_en_imagen(imagen, variacion)
            if coordenadas:
                print(f"Botón encontrado en coordenadas: {coordenadas}")
                return coordenadas
    
    return None

def hacer_click_en_boton(coordenadas):
    """Hace click en las coordenadas especificadas"""
    x, y = coordenadas
    print(f"Haciendo click en ({x}, {y})")
    
    # Mover mouse al centro del botón
    pyautogui.moveTo(x, y, duration=0.3)
    
    # Hacer click
    pyautogui.click()
    print("Click realizado")

def main():
    """Función principal que ejecuta el bucle de clicks"""
    print("=== SCRIPT DE CLICK AUTOMÁTICO EN BOTÓN SIGUIENTE ===")
    print("IMPORTANTE: Mueve el mouse a la esquina superior izquierda para detener")
    print("Iniciando en 3 segundos...")
    
    # Countdown
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    exitos = 0
    fallos = 0
    
    for iteracion in range(1, 21):  # 20 iteraciones
        print(f"\n--- ITERACIÓN {iteracion}/20 ---")
        
        try:
            # Buscar el botón
            coordenadas = buscar_boton_siguiente()
            
            if coordenadas:
                # Hacer click en el botón
                hacer_click_en_boton(coordenadas)
                exitos += 1
                
                # Esperar 1 segundo antes de la siguiente búsqueda
                print("Esperando 1 segundo...")
                time.sleep(1)
                
            else:
                print("❌ Botón 'SIGUIENTE' no encontrado")
                fallos += 1
                
                # Esperar un poco más si no se encuentra el botón
                time.sleep(2)
        
        except pyautogui.FailSafeException:
            print("\n⚠️ FAILSAFE activado - Script detenido por el usuario")
            break
        except Exception as e:
            print(f"❌ Error en iteración {iteracion}: {e}")
            fallos += 1
            time.sleep(2)
    
    # Resumen final
    print(f"\n=== RESUMEN FINAL ===")
    print(f"✅ Clicks exitosos: {exitos}")
    print(f"❌ Fallos: {fallos}")
    print(f"📊 Tasa de éxito: {(exitos/(exitos+fallos)*100):.1f}%" if (exitos+fallos) > 0 else "N/A")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Script interrumpido por el usuario")
    except Exception as e:
        print(f"❌ Error fatal: {e}")
    
    print("\nScript finalizado.")