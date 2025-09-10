Funcionalidades principales:

Captura la pantalla automáticamente
Busca el texto "SIGUIENTE" usando OCR (Reconocimiento Óptico de Caracteres)
Calcula el centro del botón y hace click en esas coordenadas
Espera 1 segundo entre cada click
Repite el proceso 20 veces en bucle
Incluye variaciones del texto ("NEXT", "CONTINUAR", etc.)

Características de seguridad:

FAILSAFE: Si mueves el mouse a la esquina superior izquierda, el script se detiene automáticamente
Control de errores robusto
Contador de éxitos y fallos
Pausa configurable entre acciones

Instalación de dependencias necesarias:
bashpip install pyautogui opencv-python pytesseract pillow numpy
Para Tesseract OCR:

Windows: Descargar desde https://github.com/UB-Mannheim/tesseract/wiki
macOS: brew install tesseract
Ubuntu/Linux: sudo apt-get install tesseract-ocr

Uso:

Asegúrate de que la ventana con los botones "SIGUIENTE" esté visible
Ejecuta el script: python nombre_del_archivo.py
El script cuenta 3 segundos antes de empezar
Para detenerlo en cualquier momento, mueve el mouse a la esquina superior izquierda

El script es inteligente y adaptativo - si la pantalla cambia entre clicks, volverá a buscar el botón en la nueva ubicación automáticamente.