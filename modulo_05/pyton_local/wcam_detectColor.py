import cv2
import numpy as np

# Inicializa la webcam
cap = cv2.VideoCapture(0)

# Limites de valores HSV para detectar el color rojo
redBajo1=np.array([0,50,50],np.uint8)
redAlto1=np.array([20,255,255],np.uint8)

redBajo2=np.array([150,50,50],np.uint8)
redAlto2=np.array([179,255,255],np.uint8)

while True:
    ret,frame=cap.read()
    if ret==True:
        framesHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # Convertir a espacio de color HSV
        maskRed1=cv2.inRange(framesHSV,redBajo1,redAlto1) # Crear una mascara con los valores
        maskRed2=cv2.inRange(framesHSV,redBajo2,redAlto2) # Crear otra mascara con los valores
        maskRed=maskRed1+maskRed2 # Sumar las dos mascaras


    maskRedInv = cv2.bitwise_not(maskRed) # Invertir la máscara
    maskRedvis = cv2.bitwise_and(frame,frame,mask=maskRed) # Aplicar la mascara a la imagen original
    maskRedvis2 = cv2.bitwise_and(frame,frame,mask=maskRedInv) # Aplicar la mascara a la imagen original
    cv2.imshow('maskRedvis',maskRedvis) # Mostrar la mascara de color rojo
    cv2.imshow('maskRedvis2',maskRedvis2) # Mostrar la mascara de color rojo invertida
    cv2.imshow('maskRed',maskRed) # Mostrar la mascara de color rojo
    cv2.imshow('maskRed_invertida',maskRedInv) # Mostrar la máscara invertida
    cv2.imshow('Video Color',frame) # Mostrar la imagen original

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()                           # Liberar la webcam
cv2.destroyAllWindows()                 # Cerrar todas las ventanas