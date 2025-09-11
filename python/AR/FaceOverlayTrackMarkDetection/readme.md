# Detección y traqueo de una cara

En este apartado pretendemos utilizar la cara como si de un marcador se tratase. No tiene por objetivo utilizar face recognition para enfocar una cámara o contar cuantas personas hay en una foto.

Si no más bien hacer un filtro tipo Instagram / TikTok o Snapchat en los que se ponen unas gafas de sol virtuales sobre el video detectado o un sombrero a modo de realidad aumentada.

---

Diferencias entre términos parecidos (por si necesitas mejorar tu prompt o buscar más documetnación a este respecto):


|Término|Explicación|
|---|---|
|***Face Detection (Detección Facial)***| - Localiza donde está la cara en la imagen o video, y la destaca por ejemplo con una _bounding box_.
-Librerías comunes en Python: OpenCV (Haar cascades, DNN), dlib, mediapipe.|
|***Face Landmark Detection (Deteccion de puntos faciales /landmarks)***| - Identificar puntos clave en la cara (ojos, nariz, boca, contorno).
-Esto permite colocar un filtro de manera precisa en el rostro.
-Librerías: dlib.share_predictor, mediapipe.face_mesh|
|***Face Tracking (Seguimiento Facial)***| - Una vez localizada la cara, seguir sus movimientos a lo largo de los frames del video.
- Evita recalcular todo en cada frame y da estabilidad al filtro.
- Técnicas: optical flow, tracking by detection, Kalma filters.
- Librerías: OpenCV (cv2.TrackerKCF_create(),etc.), mediapipe (ya incorpora seguimiento estable).|
|***Overlay / Augmented Reality (Superposición en realidad aumentada***| - Proyectar un objeto máscara o filtro sobre los landmarks faciales.
-Aquí entra la trransformación geométrica: affine transform o holography para que el filtro siga la perspectiva de la cara.|
