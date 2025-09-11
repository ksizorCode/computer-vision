# Detección y traqueo de una cara

En este apartado pretendemos utilizar la cara como si de un marcador se tratase. No tiene por objetivo utilizar face recognition para enfocar una cámara o contar cuantas personas hay en una foto.

Si no más bien hacer un filtro tipo Instagram / TikTok o Snapchat en los que se ponen unas gafas de sol virtuales sobre el video detectado o un sombrero a modo de realidad aumentada.

---

Diferencias entre términos que significan lo mismo (por si necesitas mejorar tu prompt o buscar más documetnación a este respecto):


|Término|Explicación|
|---|---|
|**Face Detection (Detección Facial)**| - Localiza donde está la cara en la imagen o video, y la destaca por ejemplo con una _bounding box_.
-Librerías comunes en Python: OpenCV (Haar cascades, DNN), dlib, mediapipe.|
|***Face Landmark Detection (Deteccion de puntos faciales /landmarks)***|
|