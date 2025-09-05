# Herraminetas de Computer Vision / Visionado por ordenador

# 1. No Code / Low Code (fáciles de usar, sin programar)
| Herramienta                                                          | Tipo                                  | Características principales                         | Ideal para                    |
| -------------------------------------------------------------------- | ------------------------------------- | --------------------------------------------------- | ----------------------------- |
| [Teachable Machine](https://teachablemachine.withgoogle.com/) | Clasificación de imágenes/audio/poses | Entrena modelos con tu webcam y dataset en minutos  | Educación, prototipado rápido |
| [Lobe](https://www.lobe.ai/) (Microsoft)                             | No-code ML                            | Interfaz gráfica para entrenar y exportar modelos   | Profesores, makers            |
| [Roboflow](https://roboflow.com/)                                    | Datasets + Computer Vision            | Anotación, entrenamiento y despliegue en la nube    | Detección de objetos, OCR     |
| [MakeML](https://makeml.app/)                                        | No-code iOS                           | Detección de objetos y segmentación                 | Apps móviles                  |
| [Clarifai](https://www.clarifai.com/)                                | Plataforma de visión                  | Etiquetado automático, clasificación, APIs visuales | Startups sin equipo técnico   |


# 2. Herramientas intermedias (requieren algo de configuración)
| Herramienta                                          | Tipo               | Características                                     | Ideal para                       |
| ---------------------------------------------------- | ------------------ | --------------------------------------------------- | -------------------------------- |
| [OpenCV AI Kit (OAK-D)](https://opencvat.org/)       | Hardware + SDK     | Cámaras inteligentes con visión embebida            | Robótica, IoT                    |
| [MediaPipe](https://developers.google.com/mediapipe) | Framework Google   | Pose estimation, hands, face mesh, gesture tracking | Apps móviles, AR                 |
| \[OpenCV GUI tools (CVAT, LabelImg)]                 | Anotación datasets | Herramientas gráficas para etiquetar imágenes       | Entrenamiento de modelos propios |
| [Edge Impulse](https://edgeimpulse.com/)             | TinyML             | Optimización de visión para microcontroladores      | IoT, dispositivos pequeños       |

# 3. Librerías en Python (Google Colab friendly)
| Librería                                     | Funcionalidad                   | Nivel de complejidad | Ejemplo de uso                        |
| -------------------------------------------- | ------------------------------- | -------------------- | ------------------------------------- |
| OpenCV (`cv2`)                               | Procesamiento de imágenes/vídeo | ⭐⭐                   | Filtros, detección de bordes, rostros |
| Scikit-Image                                 | Procesamiento científico        | ⭐⭐                   | Segmentación, transformadas           |
| TensorFlow / Keras + `tf.keras.applications` | Deep Learning                   | ⭐⭐⭐                  | Clasificación de imágenes             |
| PyTorch + torchvision                        | Deep Learning flexible          | ⭐⭐⭐                  | Redes convolucionales (CNNs)          |
| Detectron2 (Meta)                            | Detección avanzada              | ⭐⭐⭐⭐                 | Segmentación, detección de instancias |
| YOLOv8 (Ultralytics)                         | Detección en tiempo real        | ⭐⭐⭐                  | Detección rápida en Colab             |
| HuggingFace Transformers (visión)            | Modelos pre-entrenados          | ⭐⭐⭐⭐                 | CLIP, visión multimodal               |
| Matplotlib                                   |      |
Yolo
Numpy


# 4. Herramientas experimentales y creativas
| Herramienta                                                   | Tipo                    | Qué hace                                                         |
| ------------------------------------------------------------- | ----------------------- | ---------------------------------------------------------------- |
| [Teachable Machine](https://teachablemachine.withgoogle.com/) | Entrenamiento fácil     | Enseña a tu navegador a reconocer poses, imágenes o sonidos      |
| [AutoDraw](https://www.autodraw.com/)                         | Dibujo asistido         | Reconoce tus garabatos y los convierte en dibujos vectoriales    |
| [LandLines](https://lines.chromeexperiments.com/)             | Dibujo interactivo      | Convierte trazos en animaciones con IA                           |
| DeepDream                                                     | Experimento Google      | Convierte imágenes en visiones psicodélicas con redes neuronales |
| Neural Style Transfer                                         | Transferencia de estilo | Convierte fotos en cuadros (ej. Van Gogh style)                  |
| [Quick, Draw!](https://quickdraw.withgoogle.com/)             | Juego Google            | Reconoce tus dibujos en tiempo real                              |
| [Semantris](https://research.google.com/semantris/)           | Juego Google            | IA que asocia palabras y semántica                               |
👉 Si te gustan estos experimentos puedes encontrar más de todo tipo (no solo computer vision) en: experiments.withgoogle.com

# 5. APIs y servicios en la nube
| Servicio                                                                                                | Función                                     | Ventajas                        | Limitaciones                  |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ------------------------------- | ----------------------------- |
| [Google Cloud Vision](https://cloud.google.com/vision)                                                  | OCR, etiquetas, detección facial, landmarks | Fácil integración vía API       | Coste por uso                 |
| [Vertex AI Vision](https://cloud.google.com/vertex-ai/vision)                                           | Plataforma avanzada de visión               | Integración con pipelines de IA | Más compleja que Cloud Vision |
| [AWS Rekognition](https://aws.amazon.com/rekognition/)                                                  | Detección facial, moderación de contenido   | Escalable                       | Precios variables             |
| [Azure Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/) | OCR, descripción de imágenes                | Integración con MS stack        | Similar a GCP/AWS             |




https://experiments.withgoogle.com/move-mirror
