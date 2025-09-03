<!-- Tabla de contenidos -->
- [Tecnologías principales en visión por ordenador](#tecnologías-principales-en-visión-por-ordenador)
  - [1. TensorFlow](#1-tensorflow)
    - [1.1 Ecosistema y componentes](#11-ecosistema-y-componentes)
    - [1.2 Fortalezas en visión](#12-fortalezas-en-visión)
    - [1.3 Facilidad de desarrollo](#13-facilidad-de-desarrollo)
    - [1.4 Escalabilidad y despliegue](#14-escalabilidad-y-despliegue)
  - [2. OpenCV (Open Source Computer Vision Library)](#2-opencv-open-source-computer-vision-library)
    - [2.1 Base y algoritmos clásicos](#21-base-y-algoritmos-clásicos)
    - [2.2 Integración multiplataforma](#22-integración-multiplataforma)
    - [2.3 Casos de uso y ejemplos “friky”](#23-casos-de-uso-y-ejemplos-friky)
    - [2.4 Preprocesamiento para deep learning](#24-preprocesamiento-para-deep-learning)
  - [3. PyTorch](#3-pytorch)
    - [3.1 Filosofía “define-by-run”](#31-filosofía-define-by-run)
    - [3.2 Ecosistema TorchVision](#32-ecosistema-torchvision)
    - [3.3 Transición a producción](#33-transición-a-producción)
  - [4. Otras tecnologías relevantes](#4-otras-tecnologías-relevantes)
    - [4.1 Scikit-image y PIL/Pillow](#41-scikit-image-y-pilpillow)
    - [4.2 YOLO (You Only Look Once)](#42-yolo-you-only-look-once)
    - [4.3 MediaPipe](#43-mediapipe)
    - [4.4 Detectron2](#44-detectron2)
    - [4.5 Hugging Face Transformers (visión)](#45-hugging-face-transformers-visión)
  - [5. Integración y flujos de trabajo típicos](#5-integración-y-flujos-de-trabajo-típicos)
    - [5.1 Pipeline híbrido](#51-pipeline-híbrido)
    - [5.2 Desarrollo iterativo: Investigación → Producción](#52-desarrollo-iterativo-investigación-→-producción)
    - [5.3 Optimización en dispositivos embebidos](#53-optimización-en-dispositivos-embebidos)
    - [5.4 Cloud computing y despliegue](#54-cloud-computing-y-despliegue)
- [Apéndice: Esquema general de un proyecto de visión por ordenador](#apéndice-esquema-general-de-un-proyecto-de-visión-por-ordenador)

---

# Tecnologías principales en visión por ordenador

Este documento adapta y amplía los apuntes originales, estructurándolos en **Markdown** para GitHub. Hemos añadido tablas comparativas, ejemplos “friky” (basados en el cine y videojuegos) y un esquema para facilitar el estudio. ¡Que la Fuerza Friky te acompañe! 🎬👾

---

## 1. TensorFlow

TensorFlow es la plataforma de machine learning más utilizada a nivel mundial (o al menos la más mencionada en foros de StackOverflow durante la última década). Desarrollada por Google, ofrece un ecosistema muy completo:

### 1.1 Ecosistema y componentes

| Componente        | Descripción                                                                 | Analogia Friky                                 |
|-------------------|------------------------------------------------------------------------------|------------------------------------------------|
| **TensorFlow Core**   | Biblioteca central para diseñar, entrenar y ejecutar modelos de deep learning. | El “Reactor Arc” de Iron Man: potencia todo     |
| **TensorFlow Lite**   | Versión ligera para dispositivos móviles y microcontroladores.                 | El “Batarang” de Batman: pequeño pero letal     |
| **TensorFlow.js**     | Para ejecutar y entrenar modelos directamente en el navegador.                | ¿Recuerdas Skeletor invadiendo Internet?        |
| **TensorFlow Hub**    | Repositorio de modelos pre-entrenados (ResNet, EfficientNet, YOLO, etc.).    | La “Biblioteca Jedi” con paquetes listos para usar |
| **Keras (integrado)** | API de alto nivel para construir redes, más intuitiva que leer un manual de Inception. | La Capa del Olor de Narciso (fácil de poner)  |

#### Resumen rápido

- **Ecosistema integral**: Desde el Core hasta TensorFlow Lite/JS.
- **Modelos preentrenados**: ResNet, EfficientNet, MobileNet, YOLO en TF Hub.
- **Despliegue en nube**: Integración nativa con Google Cloud AI Platform.

### 1.2 Fortalezas en visión

- **Colección de modelos**: Disponibles en TF Hub, cubren clasificación, detección de objetos, segmentación, etc.
- **TensorFlow Object Detection API**:  
  - Bibliotecas y ejemplos listos para detectar personas, coches, animales.  
  - Tutoriales y notebooks oficiales que parecen salir de “El laboratorio de Dexter”.
- **Eager Execution**: Debugging más interactivo, ¡como si Jarvis te respondiera al instante!
- **tf.data**:  
  - Pipelines optimizados para cargar, transformar y alimentar imágenes.  
  - Ventaja: procesamiento paralelo en CPU/GPU, ideal para datasets con millones de imágenes (piensa en los planos de “El Señor de los Anillos”: toneladas de datos).

### 1.3 Facilidad de desarrollo

- **Keras integrado**:  
  - API de alto nivel con clases `Sequential` y `Model`.  
  - Similar a armar una partida de Lego: encajas bloques de capas y ya funciona.
- **Eager Execution por defecto**:  
  - Similar al “Modo Dios” en videojuegos: ves los valores de los tensores al vuelo.  
  - Facilita prototipado rápido.
- **tf.keras.callbacks**:  
  - Callbacks como EarlyStopping, ModelCheckpoint, TensorBoard (visualización tipo “The Matrix”).  

### 1.4 Escalabilidad y despliegue

- **Entrenamiento distribuido**:  
  - `tf.distribute.Strategy` para múltiples GPUs/TPUs.  
  - “Red Eyeshield 21” entrenando en varios GPUs a la vez.  
- **TPUs de Google**:  
  - Hardware especializado para operaciones tensóricas.  
  - Igualito que subirte al Halcón Milenario para hacer warp speed en tu entrenamiento.
- **Google Cloud Platform (GCP)**:  
  - Integración nativa con AI Platform, AI Notebooks y Dataflow.  
  - Despliegue tipo “Tony Stark” con un clic.
  
---

## 2. OpenCV (Open Source Computer Vision Library)

OpenCV existe desde hace más de 20 años y es la piedra angular de la visión tradicional. Si TensorFlow es el Quijote del deep learning, OpenCV es Sancho Panza en la visión clásica.

### 2.1 Base y algoritmos clásicos

- **Filtrado de imágenes**:  
  - Filtros espaciales (blur, GaussianBlur, medianBlur), detección de bordes (Canny), etc.  
  - Ejemplo friky: aplicar un filtro de Canny y parecer el “Ojo del Sauron”.
- **Transformaciones geométricas**:  
  - Rotaciones, escalados, transformaciones afines y perspectiva (warpPerspective).  
  - Es como cambiar la cámara en “Resident Evil”: giras la vista para explorar.
- **Calibración de cámaras**:  
  - Estimación de parámetros intrínsecos y extrínsecos con tableros de ajedrez.  
  - Piensa en la escena de "Up": alineando múltiples perspectivas para hacer el efecto de profundidad.
- **Detección de bordes y características**:  
  - Harris, Shi-Tomasi (goodFeaturesToTrack), SIFT (si tienes licencia), SURF, ORB.  
  - Ejemplo: detectar esquinas como si fuera el “Mapa del Troll” en “Harry Potter”.

### 2.2 Integración multiplataforma

| Lenguaje     | Plataformas Soportadas                  | Casos de Uso Más Comunes                                 |
|--------------|-----------------------------------------|----------------------------------------------------------|
| **C++**      | Windows, Linux, macOS, Android, iOS     | Aplicaciones embebidas en robótica (ROS), sistemas de cámaras de seguridad. |
| **Python**   | Windows, Linux, macOS                   | Prototipo rápido, scripting en pipelines de visión.      |
| **Java/Android** | Android                              | Apps móviles que usan la cámara para escanear códigos o reconocer objetos. |
| **Java (desktop)** | Windows, Linux, macOS              | Aplicaciones empresariales de visión industrial.         |
| **Otros (C#, MATLAB, etc.)** | Mediante wrappers                | Integraciones con entornos académicos o empresariales.   |

- **Rendimiento en tiempo real**:  
  - Buenas implementaciones en C++ con optimizaciones SSE/NEON.  
  - Permite procesar streams de vídeo a 30–60 FPS sin despeinarse (incluso en Raspberry Pi, el Frodón de los SBC).

### 2.3 Casos de uso y ejemplos “friky”

- **SLAM (Simultaneous Localization And Mapping)**:  
  - Librería `cv::aruco` para marcadores, `ORB-SLAM2`.  
  - Ejemplo: “Pac-Man” construyendo el mapa mientras come bolitas.
- **Stereo vision**:  
  - Calcular disparidad con `StereoBM` o `StereoSGBM`.  
  - Ejemplo “friky”: Mida la distancia del Dr. Robotnik con dos “ojos” como C-3PO.
- **Optical Flow**:  
  - Lucas-Kanade, Farneback.  
  - Ejemplo: seguimiento de la pelota en un partido de “FIFA” para analizar la trayectoria.
- **Reconocimiento facial (Eigenfaces/Fisherfaces)**:  
  - Un clásico que te hace sentir en una película de los 90 (“Men In Black”).
  
### 2.4 Preprocesamiento para deep learning

- **Detección y corrección de iluminación**:  
  - Ecualización de histogramas (CLAHE), corrección gamma.  
  - Como los “contras” en TMNT: ajustan la iluminación para que todo brille.
- **Ajuste de tamaño y normalización**:  
  - `cv2.resize`, conversión a tensores para TensorFlow/PyTorch.  
  - ¡Cómo convertir una cámara VHS en formato digital HD!
- **Segmentación clásica**:  
  - Umbralización, K-means en espacio de color HSV, Watershed.  
  - Ejemplo: “Mario Kart” segmentando la pista de carrera del fondo.
  
---

## 3. PyTorch

PyTorch, desarrollado por Facebook (Meta), es el framework “hipster” de los investigadores de deep learning. Si TensorFlow es Tony Stark, PyTorch es Doctor Strange: dinámico, flexible y perfecto para experimentos surrealistas.

### 3.1 Filosofía “define-by-run”

- **Grafos dinámicos**:  
  - Cada operación se construye en tiempo de ejecución.  
  - Control total en cada iteración, como jugar con “The Legend of Zelda” y poder girar el mundo a tu antojo.
- **Facilidad de debugging**:  
  - Inspeccionas tensores con `print()` o `pdb.set_trace()` sin complicaciones.  
  - Comparación: como usar el “Modo Dios” en “Skyrim” para ver valores internos.

### 3.2 Ecosistema TorchVision

- **Datasets predefinidos**:  
  - `CIFAR10`, `ImageNet`, `COCO`, etc.  
  - Cargas con un par de líneas:  
    ```python
    from torchvision import datasets, transforms
    transform = transforms.Compose([transforms.Resize(224), transforms.ToTensor()])
    trainset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
    ```
- **Transformaciones optimizadas**:  
  - `transforms.RandomCrop`, `transforms.ColorJitter`, `transforms.Normalize`.  
  - Como un mod de “Fallout” que transforma texturas al vuelo.
- **Modelos preentrenados**:  
  - `resnet50`, `densenet121`, `vgg16`, `efficientnet_b0`, Vision Transformers (ViT).  
  - Listos para usar con transferencia de aprendizaje.

### 3.3 Transición a producción

- **TorchScript**:  
  - Convierte tu modelo dinámico a un grafo estático optimizado.  
  - Canon: “Conviértete a hierro, modelito de AI”, al estilo de “Transformers”.
- **TorchServe**:  
  - Servidor para desplegar modelos como endpoints REST.  
  - Perfecto para montar tu propio Jarvis al estilo Tony Stark en la nube.
- **PyTorch Lightning** (opcional):  
  - Estructura el código para separar entrenamiento, validación y testing.  
  - Si eres fan de “The Avengers”, te ayuda a coordinar a todos los héroes en un solo plan.

---

## 4. Otras tecnologías relevantes

Además de los grandes protagonistas, existen muchas librerías y frameworks que pueden complementar tu proyecto de visión por ordenador. A continuación, una lista con sus principales características y ejemplos frikis.

### 4.1 Scikit-image y PIL/Pillow

| Biblioteca       | Enfoque                   | Lenguaje  | Funciones clave                                  | Ejemplo friky                                            |
|------------------|---------------------------|-----------|--------------------------------------------------|----------------------------------------------------------|
| **Scikit-image** | Procesamiento científico  | Python    | Segmentación (Otsu, SLIC), análisis de regiones, métricas de calidad | Como el “Hechizo Patronus” en Harry Potter: detecta lo bueno de lo malo. |
| **PIL/Pillow**   | Manipulación básica de imágenes | Python | Redimensionar, rotar, recortar, conversión de formatos | Como un editor de texto en “The Legend of Zelda”: simple pero esencial. |

- **Scikit-image**:  
  - Ideal para análisis de imágenes médicas o científicas.  
  - Funciones avanzadas como transformada de Hough (detectar líneas y círculos), etiquetas de objetos.
- **PIL/Pillow**:  
  - Sencillo, rápido.  
  - Carga/guarda en JPG, PNG, GIF, BMP.  
  - Útil para pipelines de preprocesamiento ligero antes de soltar el data en TensorFlow o PyTorch.

### 4.2 YOLO (You Only Look Once)

- **Arquitectura de detección en tiempo real**:  
  - Detecta y clasifica objetos en una sola pasada (versus R-CNN que va de dos en dos).  
  - Como el Flash en The Flash: ve todo en un solo vistazo.
- **Versiones más populares**:  
  - **YOLOv5**: PyTorch, ligero, rápido (~45 FPS en GPU moderada).  
  - **YOLOv8**: Ultraligero, mejoras de precisión y velocidad.  
  - **YOLOv11** (comunidad): Experimentaciones con detectores más rápidos.  
- **Tabla comparativa de YOLO vs R-CNN**:

| Característica              | YOLOv5                                 | Faster R-CNN                          |
|-----------------------------|----------------------------------------|---------------------------------------|
| Velocidad (FPS)             | ≈45 FPS en GPU moderada                | ≈5–10 FPS                             |
| Precisión (mAP COCO)        | 45–55 (depende de la versión)          | 42–52                                 |
| Complejidad de entrenamiento| Más sencillo, scripts oficiales ligeros| Requiere pasos: region proposals + clasificación |
| Uso en friky-world          | Juegos en tiempo real (detección de enemigos al vuelo) | Análisis forense de vídeo (CSI style) |

### 4.3 MediaPipe

- **Framework de Google para análisis multimedia**:  
  - Preconfigurado para detección de pose humana, reconocimiento facial, seguimiento de manos, segmentación de selfies.  
  - Listo para móvil (Android/iOS).  
- **Casos de uso friky**:  
  - Realidad aumentada: poner máscara de Darth Vader en tu cara.  
  - Seguimiento de manos: simular hechizos de “Dragon Ball” con tus movimientos.  
  - Detección de pose: recrear la coreografía de “Thriller” de Michael Jackson.

### 4.4 Detectron2

- **Plataforma de investigación de Facebook (Meta)**:  
  - Implementa state-of-the-art en detección y segmentación: Mask R-CNN, RetinaNet, DensePose.  
  - Modular y rápido para experimentar con arquitecturas nuevas.  
- **Ejemplo friky**:  
  - Usarlo para segmentar personajes en la escena final de “Avengers: Endgame” y analizarlos por separado.

### 4.5 Hugging Face Transformers (visión)

- **Origen en NLP, ahora multimodal**:  
  - Modelos como ViT (Vision Transformer), CLIP (visión + lenguaje).  
  - Facilita acceso a checkpoints entrenados en grandes datasets (ImageNet, LAION).  
- **Aplicaciones**:  
  - Búsqueda de imágenes semántica (“¿Dónde está el Halcón Milenario?”).  
  - Clasificación de escenas al estilo “Cazafantasmas”: identifica si hay “proto-hombre” en la imagen.
- **Integración sencilla**:  
  - Con un par de líneas cargas un ViT y lo aplicas a clasificar tus propias capturas de pantalla de videojuegos.

---

## 5. Integración y flujos de trabajo típicos

### 5.1 Pipeline híbrido

La mayoría de proyectos combinan varias herramientas para aprovechar fortalezas de cada una. A continuación, un **esquema** (mermaid) de un flujo de trabajo típico:

```mermaid
flowchart TD
  A[📷 Captura de video/imágenes] --> B[⚙️ Preprocesamiento (OpenCV, PIL)]
  B --> C[🔍 Detección clásica / Segmentación inicial (OpenCV, Scikit-image)]
  C --> D[🤖 Inferencia Deep Learning (TensorFlow / PyTorch)]
  D --> E[🔄 Post-procesamiento (OpenCV, custom scripts)]
  E --> F[🚀 Despliegue (API REST, App móvil, Embedded)]
```

  	A → B:
	Captura de cámara en vivo o carga de dataset (OpenCV).
	Ajuste de tamaño, corrección de color, aumento de datos.
	B → C:
	Aplicar filtros, detección de contornos, máscaras para aislar regiones de interés.
	Ejemplo: en “Ghostbusters”, primero aislas la “Depredador” (ecto-plasma) antes de analizarlo con un modelo.
	C → D:
	Entrenamiento o inferencia de un modelo CNN/CNN 3D/Transformer.
	Ejemplo friky: tu modelo detecta al T-800 (Terminator) en un plano retroiluminado.
	D → E:
	Filtrado de falsos positivos, tracking de objetos (DeepSORT).
	Ejemplo: en “The Last of Us Part II”, rastreas al enemigo cazador en plena noche.
	E → F:
	Devolver coordenadas, bounding boxes o máscaras.
	Despliegue en un API (TorchServe, TensorFlow Serving) o sube a un dispositivo móvil (TensorFlow Lite, PyTorch Mobile).



5.2 Desarrollo iterativo: Investigación → Producción

| Fase                          | Herramientas típicas                                        | Objetivo                                                          |
|-------------------------------|-------------------------------------------------------------|-------------------------------------------------------------------|
| I. Prototipado                | PyTorch (rápido), Jupyter Notebooks, OpenCV                 | Explorar ideas, probar arquitecturas, debugging “on the fly”      |
| II. Entrenamiento a gran escala | TensorFlow (distribuido en TPUs/GPU), PyTorch con DDP       | Escalar al dataset completo, optimizar hiperparámetros            |
| III. Validación y benchmarking | TensorBoard, MLflow, comet.ml                                | Monitorizar métricas: accuracy, mAP, IOU, F1-score               |
| IV. Conversión de modelo       | TorchScript, ONNX, TensorFlow SavedModel                     | Obtener formato optimizado para producción                         |
| V. Despliegue                  | TensorFlow Serving, TorchServe, Flask/FastAPI, Docker, Kubernetes | Servir como microservicio, empaquetar en contenedores             |
| VI. Mantenimiento              | ML Monitoring Tools (Prometheus, Grafana)                    | Vigilar drift, rendimiento en producción                           |



	•	Ejemplo friky:
	1.	En Phase I, tu modelo detecta Pokémons en pantallas de Mario.
	2.	En Phase II, entrenas en cientos de horas de gameplay de Twitch.
	3.	En Phase III, comparas métricas con v1.
	4.	En Phase IV, conviertes tu modelo para que corra en un smartphone (TensorFlow Lite + GPU delegado).
	5.	En Phase V, lo lanzas como app de AR que detecta Pokémons en la calle.
	6.	En Phase VI, monitoreas la tasa de falsos positivos cuando sale un Charizard nuevos en la Galar Region.

5.3 Optimización en dispositivos embebidos
	•	TensorFlow Lite:
	•	Conversión .tflite, cuantización (int8, float16), delegados de GPU (Android), Coral Edge TPU.
	•	Ejemplo: tu Raspberry Pi 4 interpretando señales de Mario Kart en HD.
	•	PyTorch Mobile:
	•	torch.quantization, conversión a TorchScript, arquitectura optimizada.
	•	Ideal para iOS/Android (XCode, Android Studio).
	•	OpenCV compilado para ARM:
	•	Utiliza NEON, V4L2 para captura en tiempo real.
	•	Ejemplo “friky”: Detección de intrusos al estilo “Silent Hill” con una cámara Pi Zero.

5.4 Cloud computing y despliegue
	•	AWS SageMaker, GCP AI Platform, Azure ML:
	•	Entrena sin preocuparte de la infraestructura (como si el jefe final ya estuviera resuelto).
	•	Paga por instancia solo cuando entrenas (¡adiós a los semáforos eternos!).
	•	Serverless Inference:
	•	AWS Lambda + AWS SageMaker Endpoint, GCP Cloud Functions + Vertex AI.
	•	Ejecución a demanda, escalado automático.
	•	Edge Computing:
	•	Google Coral, NVIDIA Jetson Nano, Intel Movidius.
	•	Ideal para robótica, drones o vehículos autónomos (KITT en un Ford Mustang).

⸻

Apéndice: Esquema general de un proyecto de visión por ordenador

Para ayudar a memorizar y estudiar, presentamos un esquema con los pasos principales, como si fuera un cheat sheet de videojuegos:

1. Definición del problema
   ├─ Tipo de tarea: clasificación, detección, segmentación, tracking
   ├─ Dataset: tamaño, formato, etiquetas
   └─ Métricas: accuracy, mAP, IOU, F1-score

2. Recolección y preprocesamiento de datos
   ├─ Captura de imágenes/vídeo (OpenCV, cámaras)
   ├─ Limpieza y etiquetado (LabelImg, CVAT)
   ├─ Aumento de datos (rotaciones, flip, cambios de brillo)
   └─ División en entrenamiento/validación/test

3. Selección de arquitectura
   ├─ Modelos clásicos: SVM, HOG+SVM, Haar Cascades (OpenCV)
   ├─ Modelos CNN: ResNet, MobileNet, EfficientNet
   ├─ Modelos de detección: YOLO, SSD, Faster R-CNN
   └─ Modelos de segmentación: U-Net, Mask R-CNN

4. Entrenamiento
   ├─ Framework: PyTorch (define-by-run) o TensorFlow (estático/dinámico)
   ├─ Configuración: tasas de aprendizaje, optimizadores (Adam, SGD)
   ├─ Callbacks/Checkpoints (TensorBoard, ModelCheckpoint)
   └─ Validación temprana (EarlyStopping)

5. Evaluación y ajuste
   ├─ Métricas clave: matriz de confusión, curvas ROC, PR
   ├─ Ajuste de hiperparámetros (Grid Search, Bayesian Search)
   ├─ Data Augmentation adicional si hay overfitting
   └─ Pruebas en dataset real (robustez en escenarios “no perfectos”)

6. Conversión y optimización
   ├─ PyTorch → TorchScript → Podar y cuantizar
   ├─ TensorFlow → SavedModel → .tflite + cuantización
   ├─ ONNX como puente entre frameworks
   └─ Benchmarking en hardware objetivo

7. Despliegue
   ├─ Microservicios: TorchServe, TensorFlow Serving, FastAPI
   ├─ Contenedores: Docker + Kubernetes (yak, minikube)
   ├─ Edge: TensorFlow Lite, PyTorch Mobile, OpenCV compilado
   └─ Monitoreo y mantenimiento (Prometheus, Grafana)

8. Mantenimiento y escalado
   ├─ Re-entrenamiento con datos nuevos (drift detection)
   ├─ Monitoreo de métricas en producción
   ├─ Actualizaciones periódicas del modelo
   └─ Documentación y versión de código (GitHub, DVC)