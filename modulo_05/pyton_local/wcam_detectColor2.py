import cv2
import numpy as np

# Función vacía para los trackbars
def nothing(x):
    pass

# Inicializar la webcam
cap = cv2.VideoCapture(0)

# Crear ventana para la imagen y controles
cv2.namedWindow('image')

# Crear trackbars para cambio de color
# El Hue va de 0-179 en OpenCV
cv2.createTrackbar('HMin', 'image', 0, 179, nothing)
cv2.createTrackbar('SMin', 'image', 0, 255, nothing)
cv2.createTrackbar('VMin', 'image', 0, 255, nothing)
cv2.createTrackbar('HMax', 'image', 0, 179, nothing)
cv2.createTrackbar('SMax', 'image', 0, 255, nothing)
cv2.createTrackbar('VMax', 'image', 0, 255, nothing)

# Establecer valores por defecto para los trackbars Max HSV
cv2.setTrackbarPos('HMax', 'image', 179)
cv2.setTrackbarPos('SMax', 'image', 255)
cv2.setTrackbarPos('VMax', 'image', 255)

# Trackbar adicional para modo de visualización
cv2.createTrackbar('Vista', 'image', 0, 3, nothing)

# Inicializar valores HSV min/max
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

print("Controles:")
print("- Ajusta los valores HSV con las barras deslizantes")
print("- Vista: 0=Máscara, 1=Original, 2=Color detectado, 3=Fondo sin color")
print("- Presiona 'q' para salir")
print("- Presiona 'p' para imprimir valores actuales")
print("- Presiona 'r' para resetear valores")

waitTime = 33

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Obtener valores actuales de los trackbars
    hMin = cv2.getTrackbarPos('HMin', 'image')
    sMin = cv2.getTrackbarPos('SMin', 'image')
    vMin = cv2.getTrackbarPos('VMin', 'image')
    hMax = cv2.getTrackbarPos('HMax', 'image')
    sMax = cv2.getTrackbarPos('SMax', 'image')
    vMax = cv2.getTrackbarPos('VMax', 'image')
    vista = cv2.getTrackbarPos('Vista', 'image')
    
    # Configurar límites min y max HSV
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])
    
    # Convertir a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Crear máscara HSV
    mask = cv2.inRange(hsv, lower, upper)
    
    # Aplicar operaciones morfológicas para limpiar la máscara
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Aplicar máscara a la imagen original
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Crear máscara invertida y aplicarla
    mask_inv = cv2.bitwise_not(mask)
    background = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Mostrar según el modo de vista seleccionado
    if vista == 0:  # Máscara
        output = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    elif vista == 1:  # Original
        output = frame
    elif vista == 2:  # Color detectado
        output = result
    else:  # Fondo sin color
        output = background
    
    # Mostrar información de valores en la imagen
    cv2.putText(output, f'H: {hMin}-{hMax}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    cv2.putText(output, f'S: {sMin}-{sMax}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    cv2.putText(output, f'V: {vMin}-{vMax}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    
    # Mostrar la imagen
    cv2.imshow('image', output)
    
    # Solo imprimir si los valores han cambiado (para evitar spam en consola)
    if (phMin != hMin) or (psMin != sMin) or (pvMin != vMin) or (phMax != hMax) or (psMax != sMax) or (pvMax != vMax):
        print(f"HSV Ranges: H({hMin}-{hMax}), S({sMin}-{sMax}), V({vMin}-{vMax})")
        phMin = hMin; psMin = sMin; pvMin = vMin
        phMax = hMax; psMax = sMax; pvMax = vMax
    
    # Manejar entrada de teclado
    key = cv2.waitKey(waitTime) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('p'):  # Imprimir valores actuales
        print(f"\n--- Valores HSV actuales ---")
        print(f"lower = np.array([{hMin}, {sMin}, {vMin}])")
        print(f"upper = np.array([{hMax}, {sMax}, {vMax}])")
        print(f"Rango H: {hMin}-{hMax}")
        print(f"Rango S: {sMin}-{sMax}")
        print(f"Rango V: {vMin}-{vMax}")
    elif key == ord('r'):  # Reset valores
        cv2.setTrackbarPos('HMin', 'image', 0)
        cv2.setTrackbarPos('SMin', 'image', 0)
        cv2.setTrackbarPos('VMin', 'image', 0)
        cv2.setTrackbarPos('HMax', 'image', 179)
        cv2.setTrackbarPos('SMax', 'image', 255)
        cv2.setTrackbarPos('VMax', 'image', 255)
        print("Valores reseteados a rango completo")

# Cleanup
cap.release()
cv2.destroyAllWindows()