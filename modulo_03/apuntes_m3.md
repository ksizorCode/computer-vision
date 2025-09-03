# Módulo 03: Principales funciones del visionado por ordenador

## Extracción de características

### Conceptos fundamentales

#### Detección de bordes
- **Operador Sobel**: Calcula el gradiente de la intensidad de la imagen en cada píxel, destacando áreas de alta variación espacial (bordes).
  - Utiliza dos kernels 3x3 para aproximar las derivadas horizontales y verticales.
  - Matemáticamente: G = √(Gx² + Gy²), donde Gx y Gy son los gradientes en x e y.

- **Operador Prewitt**: Similar a Sobel pero con menos énfasis en los píxeles centrales.
  - Más sensible al ruido pero puede detectar bordes más sutiles.
  - Kernels simplificados para cálculos más rápidos.

- **Detector Canny**: Algoritmo multi-etapa que incluye:
  1. Reducción de ruido con filtro gaussiano
  2. Cálculo de gradientes (magnitud y dirección)
  3. Supresión de no-máximos
  4. Umbralización con histéresis usando dos umbrales

#### Detección de esquinas
- **Harris Corner Detector**: 
  - Basado en la matriz de autocorrelación de los gradientes
  - Detecta puntos donde hay cambios significativos en todas las direcciones
  - Fórmula: R = det(M) - k·trace(M)², donde M es la matriz de autocorrelación

- **FAST (Features from Accelerated Segment Test)**:
  - Examina un círculo de 16 píxeles alrededor del punto candidato
  - Compara la intensidad con el píxel central usando un umbral
  - Extremadamente eficiente computacionalmente
  - Ampliamente usado en aplicaciones de tiempo real

#### Descriptores de características
- **SIFT (Scale-Invariant Feature Transform)**:
  - Invariante a escala, rotación, cambios de iluminación y punto de vista
  - Proceso: detección de extremos en el espacio de escala, localización precisa, asignación de orientación y generación de descriptores
  - Vector descriptor de 128 dimensiones
  - Patentado hasta 2020

- **SURF (Speeded-Up Robust Features)**:
  - Versión más rápida de SIFT
  - Usa aproximaciones con imágenes integrales y filtros de caja
  - Descriptor de 64 dimensiones (más compacto)

- **ORB (Oriented FAST and Rotated BRIEF)**:
  - Combinación de detector FAST y descriptor BRIEF
  - Añade información de orientación
  - Alternativa libre de patentes a SIFT/SURF
  - Muy eficiente para aplicaciones en tiempo real

### Implementación práctica

#### Detección de bordes con diferentes operadores
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
img = cv2.imread('imagen.jpg', 0)

# Aplicar diferentes detectores de bordes
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)

# Normalizar para visualización
sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Detector Canny con diferentes parámetros
canny_bajo = cv2.Canny(img, 50, 150)
canny_alto = cv2.Canny(img, 100, 200)

# Visualizar resultados
plt.figure(figsize=(12, 8))
plt.subplot(221), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(222), plt.imshow(sobel, cmap='gray'), plt.title('Sobel')
plt.subplot(223), plt.imshow(canny_bajo, cmap='gray'), plt.title('Canny (umbrales bajos)')
plt.subplot(224), plt.imshow(canny_alto, cmap='gray'), plt.title('Canny (umbrales altos)')
plt.tight_layout()
plt.show()
```

#### Detección y descripción de puntos clave
```python
import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('escena.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detector SIFT
sift = cv2.SIFT_create()
keypoints_sift, descriptors_sift = sift.detectAndCompute(img_gray, None)

# Detector ORB (alternativa libre)
orb = cv2.ORB_create(nfeatures=2000)
keypoints_orb, descriptors_orb = orb.detectAndCompute(img_gray, None)

# Visualizar keypoints
img_sift = cv2.drawKeypoints(img, keypoints_sift, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
img_orb = cv2.drawKeypoints(img, keypoints_orb, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Mostrar resultados
cv2.imshow('SIFT Keypoints', img_sift)
cv2.imshow('ORB Keypoints', img_orb)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Aplicaciones avanzadas

#### Reconocimiento facial con OpenCV
- **Detección facial**: Uso de clasificadores Haar o LBP (Local Binary Patterns)
- **Alineación facial**: Detección de landmarks y transformación afín
- **Extracción de características**: Mediante descriptores o redes neuronales profundas
- **Comparación**: Cálculo de distancias (euclidiana, coseno) entre vectores de características

```python
# Ejemplo simplificado de detección facial
import cv2

# Cargar clasificador pre-entrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturar video de la webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostros
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Dibujar rectángulos alrededor de los rostros
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Mostrar resultado
    cv2.imshow('Detección Facial', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

#### Alineación de imágenes médicas
- **Registro de imágenes**: Alineación de imágenes de diferentes modalidades (CT, MRI, PET)
- **Métodos**:
  - Basados en intensidad: Maximización de información mutua
  - Basados en características: Alineación mediante puntos clave correspondientes
- **Aplicaciones**: Seguimiento de progresión de enfermedades, planificación quirúrgica, fusión multimodal

#### Reconocimiento de objetos basado en características
- **Emparejamiento de características**: Algoritmos como FLANN (Fast Library for Approximate Nearest Neighbors)
- **Estimación de homografía**: Transformación geométrica entre imágenes usando RANSAC
- **Aplicaciones**: Realidad aumentada, reconstrucción 3D, stitching de imágenes panorámicas

## Detección y clasificación de objetos
### Arquitecturas modernas
- **R-CNN**: Primera generación de detectores basados en regiones
- **Faster R-CNN**: Mejora significativa en velocidad y precisión
- **YOLOv8**: Última versión del detector en tiempo real

### Comparativa de modelos
| Modelo | Precisión | Velocidad |
|--------|-----------|-----------|
| R-CNN  | Alta      | Lenta     |
| Faster R-CNN | Muy alta | Media     |
| YOLOv8 | Alta      | Muy rápida |

## Segmentación de imágenes

### Fundamentos de la segmentación

#### Definición y objetivos
- **Segmentación**: Proceso de dividir una imagen en regiones significativas
- **Tipos de segmentación**:
  - **Semántica**: Asigna una clase a cada píxel (sin distinguir instancias)
  - **Instancia**: Identifica y separa objetos individuales de la misma clase
  - **Panóptica**: Combina segmentación semántica e instancia

#### Aplicaciones principales
- **Medicina**: Detección de tumores, segmentación de órganos, análisis celular
- **Conducción autónoma**: Comprensión de escenas, detección de carreteras y obstáculos
- **Análisis de imágenes satelitales**: Cartografía, monitoreo ambiental
- **Realidad aumentada**: Separación de primer plano y fondo

### Técnicas clásicas

#### Métodos basados en umbralización
- **Umbralización global**: Aplicación de un único umbral a toda la imagen
- **Umbralización adaptativa**: Umbrales variables según regiones locales
- **Método de Otsu**: Determinación automática del umbral óptimo

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
img = cv2.imread('imagen.jpg', 0)

# Umbralización global
_, thresh_global = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Umbralización adaptativa
thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 11, 2)

# Umbralización con Otsu
_, thresh_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Visualizar resultados
plt.figure(figsize=(12, 8))
plt.subplot(221), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(222), plt.imshow(thresh_global, cmap='gray'), plt.title('Global')
plt.subplot(223), plt.imshow(thresh_adapt, cmap='gray'), plt.title('Adaptativa')
plt.subplot(224), plt.imshow(thresh_otsu, cmap='gray'), plt.title('Otsu')
plt.tight_layout()
plt.show()
```

#### Métodos basados en regiones
- **Crecimiento de regiones**: Expansión desde píxeles semilla
- **División y fusión**: Subdivisión recursiva y posterior fusión
- **Watershed**: Transformación de línea divisoria de aguas

```python
# Segmentación con Watershed
from scipy import ndimage

# Preprocesamiento
img = cv2.imread('objetos.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)

# Umbralización para obtener marcadores
_, thresh = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Operaciones morfológicas para limpiar ruido
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Transformación de distancia
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)

# Encontrar región desconocida
sure_bg = cv2.dilate(opening, kernel, iterations=3)
unknown = cv2.subtract(sure_bg, sure_fg)

# Etiquetado de marcadores
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Aplicar watershed
markers = cv2.watershed(img, markers)
img[markers == -1] = [0, 0, 255]  # Marcar bordes en rojo

# Visualizar resultado
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Segmentación Watershed')
plt.show()
```

#### Métodos basados en bordes
- **Detección de bordes + cierre de contornos**
- **Contornos activos (Snakes)**
- **Level Set Methods**

### Técnicas avanzadas basadas en deep learning

#### Arquitecturas FCN (Fully Convolutional Networks)
- **Principio**: Adaptación de redes de clasificación para segmentación
- **Características**:
  - Sustitución de capas fully-connected por convolucionales
  - Upsampling mediante deconvolución
  - Skip connections para recuperar detalles espaciales

#### U-NET
- **Arquitectura**: Red en forma de U con camino de contracción y expansión
- **Características principales**:
  - Conexiones de salto (skip connections) entre niveles simétricos
  - Preservación de información espacial
  - Entrenamiento con pocas imágenes mediante data augmentation
- **Aplicaciones**: Originalmente para imágenes biomédicas, ahora de uso general

```python
# Implementación simplificada de U-NET con TensorFlow/Keras
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model

def unet_model(input_size=(256, 256, 1)):
    # Entrada
    inputs = Input(input_size)
    
    # Camino de contracción (encoder)
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(inputs)
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    
    conv2 = Conv2D(128, 3, activation='relu', padding='same')(pool1)
    conv2 = Conv2D(128, 3, activation='relu', padding='same')(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    
    conv3 = Conv2D(256, 3, activation='relu', padding='same')(pool2)
    conv3 = Conv2D(256, 3, activation='relu', padding='same')(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    
    # Puente
    conv4 = Conv2D(512, 3, activation='relu', padding='same')(pool3)
    conv4 = Conv2D(512, 3, activation='relu', padding='same')(conv4)
    
    # Camino de expansión (decoder)
    up5 = Conv2DTranspose(256, 2, strides=(2, 2), padding='same')(conv4)
    concat5 = concatenate([up5, conv3], axis=3)
    conv5 = Conv2D(256, 3, activation='relu', padding='same')(concat5)
    conv5 = Conv2D(256, 3, activation='relu', padding='same')(conv5)
    
    up6 = Conv2DTranspose(128, 2, strides=(2, 2), padding='same')(conv5)
    concat6 = concatenate([up6, conv2], axis=3)
    conv6 = Conv2D(128, 3, activation='relu', padding='same')(concat6)
    conv6 = Conv2D(128, 3, activation='relu', padding='same')(conv6)
    
    up7 = Conv2DTranspose(64, 2, strides=(2, 2), padding='same')(conv6)
    concat7 = concatenate([up7, conv1], axis=3)
    conv7 = Conv2D(64, 3, activation='relu', padding='same')(concat7)
    conv7 = Conv2D(64, 3, activation='relu', padding='same')(conv7)
    
    # Capa de salida
    outputs = Conv2D(1, 1, activation='sigmoid')(conv7)
    
    model = Model(inputs=inputs, outputs=outputs)
    return model

# Crear modelo
model = unet_model()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

#### Mask R-CNN
- **Extensión de Faster R-CNN** para segmentación de instancias
- **Componentes**:
  - Backbone: Extracción de características (ResNet + FPN)
  - RPN: Generación de propuestas de regiones
  - RoI Align: Extracción de características de regiones con alineación precisa
  - Branch de segmentación: Generación de máscaras por instancia
- **Ventajas**: Alta precisión, separación de instancias, múltiples tareas

```python
# Ejemplo de uso de Mask R-CNN pre-entrenado
import mrcnn.model as modellib
from mrcnn import utils
from mrcnn import visualize
from mrcnn.config import Config

# Configuración para inferencia
class InferenceConfig(Config):
    NAME = "coco"
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 81  # COCO tiene 80 clases + fondo

# Crear modelo en modo inferencia
config = InferenceConfig()
model = modellib.MaskRCNN(mode="inference", config=config, model_dir="./")

# Cargar pesos pre-entrenados
model.load_weights("mask_rcnn_coco.h5", by_name=True)

# Clases del dataset COCO
class_names = ['BG', 'person', 'bicycle', 'car', ...]

# Realizar predicción
image = cv2.imread("imagen.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = model.detect([image], verbose=1)
r = results[0]

# Visualizar resultados
visualize.display_instances(
    image, r['rois'], r['masks'], r['class_ids'], 
    class_names, r['scores']
)
```

#### DeepLab
- **Características principales**:
  - Atrous convolutions (dilatadas) para aumentar campo receptivo
  - Atrous Spatial Pyramid Pooling (ASPP) para capturar contexto multi-escala
  - Encoder-decoder con skip connections
- **Versiones**: DeepLabv1, v2, v3, v3+
- **Ventajas**: Excelente precisión, buena gestión de objetos multi-escala

#### SAM (Segment Anything Model)
- **Modelo fundacional** para segmentación desarrollado por Meta AI
- **Características**:
  - Entrenado con 11 millones de imágenes y mil millones de máscaras
  - Arquitectura transformer con encoder de imagen y decoder de máscara
  - Capacidad de segmentar cualquier objeto con mínima supervisión
- **Modos de operación**:
  - Automático: Segmentación de todos los objetos en la imagen
  - Interactivo: Segmentación basada en puntos o cajas proporcionados por el usuario
  - Con texto: Segmentación guiada por descripción textual (con CLIP)

```python
# Ejemplo de uso de SAM
from segment_anything import SamPredictor, sam_model_registry
import numpy as np

# Cargar modelo SAM
sam = sam_model_registry["vit_h"](checkpoint="sam_vit_h_4b8939.pth")
predictor = SamPredictor(sam)

# Cargar imagen
image = cv2.imread("imagen.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Establecer imagen
predictor.set_image(image)

# Segmentación basada en puntos
input_point = np.array([[500, 375]])  # Coordenadas x,y
input_label = np.array([1])  # 1 para punto de primer plano

masks, scores, logits = predictor.predict(
    point_coords=input_point,
    point_labels=input_label,
    multimask_output=True  # Devuelve múltiples máscaras candidatas
)

# Visualizar la mejor máscara
best_mask = masks[np.argmax(scores)]
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.imshow(best_mask, alpha=0.5)  # Superponer máscara con transparencia
plt.axis('off')
plt.show()
```

### Métricas de evaluación

#### Métricas comunes
- **IoU (Intersection over Union)**: Área de intersección / Área de unión
- **Dice Coefficient**: 2 * Área de intersección / (Área de máscara A + Área de máscara B)
- **Precisión y Recall**: Evaluación de píxeles correctamente clasificados
- **mAP (mean Average Precision)**: Para segmentación de instancias

```python
# Cálculo de IoU y Dice
def calculate_iou(mask1, mask2):
    intersection = np.logical_and(mask1, mask2).sum()
    union = np.logical_or(mask1, mask2).sum()
    return intersection / union if union > 0 else 0

def calculate_dice(mask1, mask2):
    intersection = np.logical_and(mask1, mask2).sum()
    return 2 * intersection / (mask1.sum() + mask2.sum()) if (mask1.sum() + mask2.sum()) > 0 else 0
```

### Caso de estudio: Imágenes médicas

#### Segmentación de células cancerígenas
- **Desafíos específicos**:
  - Variabilidad en tinción y preparación
  - Células superpuestas y agrupadas
  - Bordes difusos
  - Heterogeneidad morfológica

#### Pipeline de procesamiento
1. **Preprocesamiento**:
   - Normalización de color (Macenko, Reinhard)
   - Mejora de contraste
   - Filtrado de ruido

2. **Segmentación**:
   - U-NET entrenada con imágenes histopatológicas
   - Post-procesamiento con operaciones morfológicas
   - Separación de células superpuestas mediante watershed

3. **Análisis**:
   - Extracción de características morfológicas
   - Clasificación de células (normal vs. cancerígena)
   - Cuantificación de densidad celular

#### Implementación con StarDist
StarDist es un método especializado para segmentación de células que maneja bien las superposiciones.

```python
from stardist.models import StarDist2D

# Cargar modelo pre-entrenado para células
model = StarDist2D.from_pretrained('2D_versatile_fluo')

# Predecir máscaras de células
labels, details = model.predict_instances(img)

# Visualizar resultados
from stardist.plot import render_label
fig = plt.figure(figsize=(8, 8))
plt.subplot(121); plt.imshow(img if img.ndim==2 else img[...,0])
plt.subplot(122); plt.imshow(render_label(labels, img=img))
plt.tight_layout()
plt.show()
```

### Aplicaciones avanzadas

#### Segmentación en tiempo real
- **Arquitecturas eficientes**: ENet, BiSeNet, Fast-SCNN
- **Optimizaciones**: Pruning, cuantización, distilación de conocimiento
- **Hardware especializado**: GPUs, TPUs, aceleradores de edge

#### Segmentación 3D
- **Extensión a volúmenes**: U-Net 3D, V-Net
- **Aplicaciones**: Segmentación de órganos en CT/MRI, análisis de volúmenes cerebrales

#### Segmentación de video
- **Métodos**: Propagación temporal, redes recurrentes, atención espacio-temporal
- **Aplicaciones**: Edición de video, efectos visuales, seguimiento de objetos

## Análisis de vídeo

### Fundamentos del análisis de vídeo

#### Diferencias entre análisis de imágenes y vídeo
- **Dimensión temporal**: El vídeo añade información sobre movimiento y cambios
- **Volumen de datos**: Mayor cantidad de información a procesar
- **Coherencia temporal**: Aprovechamiento de la continuidad entre frames
- **Desafíos adicionales**: Oclusiones, cambios de iluminación, movimiento de cámara

#### Representación de vídeo
- **Secuencia de frames**: Tratamiento como imágenes individuales
- **Volumen espacio-temporal**: Consideración del vídeo como un cubo 3D
- **Flujo óptico**: Representación del movimiento aparente

### Pipeline típico de análisis

#### 1. Adquisición y preprocesamiento
- **Captura**: Cámaras, archivos de vídeo, streaming
- **Decodificación**: Conversión de formatos comprimidos (H.264, VP9) a frames
- **Preprocesamiento**:
  - Redimensionamiento y recorte
  - Normalización de color e iluminación
  - Estabilización (opcional)

```python
import cv2

# Abrir vídeo
cap = cv2.VideoCapture('video.mp4')

# Verificar apertura correcta
if not cap.isOpened():
    print("Error al abrir el vídeo")
    exit()

# Obtener propiedades
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(f"FPS: {fps}, Resolución: {width}x{height}, Frames: {num_frames}")

# Configurar salida (opcional)
out = cv2.VideoWriter('output.mp4', 
                     cv2.VideoWriter_fourcc(*'mp4v'), 
                     fps, (width, height))

# Procesar frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Preprocesamiento
    frame = cv2.resize(frame, (640, 480))  # Redimensionar
    frame = cv2.GaussianBlur(frame, (5, 5), 0)  # Suavizado
    
    # Aquí iría el procesamiento principal
    # ...
    
    # Guardar frame procesado
    out.write(frame)
    
    # Mostrar resultado
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()
```

#### 2. Extracción de características
- **Por frame**: Aplicación de técnicas de procesamiento de imágenes
- **Temporales**: Diferencia entre frames, flujo óptico
- **Espacio-temporales**: Descriptores 3D, cuboides

```python
# Cálculo de flujo óptico
import numpy as np

prev_frame = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if prev_frame is not None:
        # Calcular flujo óptico con Farneback
        flow = cv2.calcOpticalFlowFarneback(prev_frame, gray, 
                                           None, 0.5, 3, 15, 3, 5, 1.2, 0)
        
        # Convertir a coordenadas polares
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        
        # Visualizar magnitud del flujo
        norm_mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        flow_mag = np.uint8(norm_mag)
        flow_color = cv2.applyColorMap(flow_mag, cv2.COLORMAP_JET)
        
        cv2.imshow('Flujo óptico', flow_color)
    
    prev_frame = gray.copy()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

#### 3. Análisis y procesamiento
- **Detección y tracking**: Seguimiento de objetos a lo largo del tiempo
- **Reconocimiento de acciones**: Clasificación de actividades
- **Segmentación espacio-temporal**: Separación de objetos en movimiento
- **Análisis de comportamiento**: Detección de patrones y anomalías

#### 4. Post-procesamiento y visualización
- **Filtrado temporal**: Suavizado de resultados entre frames
- **Agregación**: Estadísticas y métricas a nivel de vídeo
- **Visualización**: Anotaciones, heatmaps, trayectorias

### Técnicas avanzadas

#### Redes neuronales para vídeo
- **Redes 3D convolucionales**: Extensión de CNNs con filtros 3D
  - C3D, I3D, SlowFast Networks

- **Redes recurrentes**: Modelado de dependencias temporales
  - LSTM, GRU aplicadas a características visuales

- **Arquitecturas híbridas**: Combinación de componentes espaciales y temporales
  - CNN + LSTM, CNN + Transformer

#### Reconocimiento de acciones
- **Clasificación de acciones**: Identificar actividades en clips de vídeo
- **Detección temporal**: Localizar cuándo ocurre una acción
- **Detección espacio-temporal**: Localizar dónde y cuándo ocurre una acción

```python
# Ejemplo simplificado de clasificación de acciones con I3D pre-entrenado
import torch
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from pytorchvideo.models.hub import i3d_r50

# Cargar modelo pre-entrenado
model = i3d_r50(pretrained=True)
model.eval()

# Preprocesamiento
transform = Compose([
    Resize(256),
    CenterCrop(224),
    ToTensor(),
    Normalize(mean=[0.45, 0.45, 0.45], std=[0.225, 0.225, 0.225]),
])

# Extraer clips de vídeo (simplificado)
clips = []
for i in range(0, num_frames, 16):
    if i + 16 > num_frames:
        break
    
    clip = []
    for j in range(16):  # 16 frames por clip
        cap.set(cv2.CAP_PROP_POS_FRAMES, i + j)
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = transform(frame)
            clip.append(frame)
    
    if len(clip) == 16:
        clip_tensor = torch.stack(clip, dim=0)  # [16, 3, 224, 224]
        clips.append(clip_tensor)

# Inferencia
with torch.no_grad():
    for clip in clips:
        # Añadir dimensiones de batch
        clip = clip.unsqueeze(0)  # [1, 16, 3, 224, 224]
        # Reorganizar para modelo I3D: [batch, channel, time, height, width]
        clip = clip.permute(0, 2, 1, 3, 4)  
        
        # Predicción
        output = model(clip)
        
        # Obtener clase predicha
        pred_class = torch.argmax(output, dim=1).item()
        print(f"Acción predicha: {pred_class}")
```

## Seguimiento de objetos (Tracking)

### Fundamentos del tracking

#### Definición y objetivos
- **Tracking**: Localización de objetos a lo largo del tiempo en una secuencia de vídeo
- **Objetivos**:
  - Mantener identidades consistentes
  - Manejar oclusiones y reapariciones
  - Predecir trayectorias futuras

#### Taxonomía de métodos de tracking
- **Single Object Tracking (SOT)**: Seguimiento de un único objeto
- **Multiple Object Tracking (MOT)**: Seguimiento de múltiples objetos simultáneamente
- **Visual Object Tracking (VOT)**: Seguimiento basado en apariencia visual

### Algoritmos clásicos

#### Filtros bayesianos
- **Filtro de Kalman**: Estimación óptima para sistemas lineales con ruido gaussiano
- **Filtro de partículas**: Aproximación no paramétrica para sistemas no lineales

#### Métodos basados en apariencia
- **Mean-shift y Camshift**: Tracking basado en histogramas de color
- **Correlation filters**: MOSSE, KCF, DCF
- **Tracking-by-detection**: Detección en cada frame + asociación

### Algoritmos modernos basados en deep learning

#### SORT (Simple Online and Realtime Tracking)
- **Componentes**:
  - Detector de objetos (típicamente Faster R-CNN o YOLO)
  - Filtro de Kalman para predicción de movimiento
  - Asociación de datos mediante IoU
- **Ventajas**: Simple, rápido, eficiente
- **Limitaciones**: Dificultad con oclusiones largas

#### DeepSORT
- **Extensión de SORT** con características de apariencia profundas
- **Componentes adicionales**:
  - Red neuronal para extracción de características de apariencia
  - Métrica de similitud para asociación de identidades
  - Cascade matching para recuperación de identidades
- **Ventajas**: Mejor manejo de oclusiones, identidades más estables

```python
# Ejemplo simplificado de DeepSORT con YOLOv8
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# Inicializar detector y tracker
model = YOLO('yolov8n.pt')
tracker = DeepSort(max_age=30, n_init=3, 
                  max_cosine_distance=0.3,
                  nn_budget=100)

# Procesar vídeo
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detección con YOLOv8
    results = model(frame)
    
    # Extraer detecciones
    detections = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            
            # Solo considerar personas (clase 0)
            if cls == 0 and conf > 0.5:
                detections.append(([x1, y1, x2-x1, y2-y1], conf, 'person'))
    
    # Actualizar tracker
    tracks = tracker.update_tracks(detections, frame=frame)
    
    # Dibujar tracks
    for track in tracks:
        if not track.is_confirmed():
            continue
        
        track_id = track.track_id
        ltrb = track.to_ltrb()
        
        x1, y1, x2, y2 = map(int, ltrb)
        
        # Dibujar bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Mostrar ID
        cv2.putText(frame, f"ID: {track_id}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Mostrar resultado
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

#### ByteTrack
- **Innovación principal**: Aprovechamiento de detecciones de baja confianza
- **Componentes**:
  - YOLOX como detector base
  - Asociación en dos etapas: alta confianza primero, baja confianza después
  - Filtro de Kalman para predicción de movimiento
- **Ventajas**: Estado del arte en benchmarks MOT, robusto en escenas concurridas

#### OC-SORT (Observation-Centric SORT)
- **Mejoras sobre SORT**:
  - Corrección de la velocidad basada en observaciones
  - Recuperación de trayectorias mediante asociación de observaciones
  - Estimación de velocidad adaptativa
- **Ventajas**: Mejor manejo de movimientos no lineales y oclusiones

### Aplicaciones del tracking

#### Videovigilancia
- **Seguimiento de personas**: Monitoreo de actividades y comportamientos
- **Análisis de multitudes**: Estimación de densidad y flujos de movimiento
- **Detección de intrusiones**: Identificación de personas en zonas restringidas

#### Deportes
- **Análisis de rendimiento**: Seguimiento de jugadores y balón
- **Estadísticas automáticas**: Distancia recorrida, mapas de calor, posesión
- **Transmisiones mejoradas**: Gráficos superpuestos, seguimiento automático

#### Conducción autónoma
- **Seguimiento de vehículos**: Predicción de trayectorias
- **Detección de peatones**: Anticipación de movimientos
- **Planificación de ruta**: Navegación en entornos dinámicos

#### Interacción humano-computadora
- **Seguimiento de gestos**: Control mediante movimientos
- **Realidad aumentada**: Superposición de elementos virtuales
- **Captura de movimiento**: Animación y análisis biomecánico

## Modelo YOLO

### Evolución del modelo

#### Fundamentos de YOLO
- **Concepto**: "You Only Look Once" - detección en una sola pasada
- **Innovación principal**: Reformula la detección como un problema de regresión directa
- **Ventajas**: Extremadamente rápido, razonamiento global sobre la imagen

#### YOLOv1 (2016)
- **Arquitectura**: Red convolucional inspirada en GoogLeNet
- **Funcionamiento**: 
  - Divide la imagen en una cuadrícula S×S
  - Cada celda predice B bounding boxes y C probabilidades de clase
  - Cada bounding box incluye (x, y, w, h, confianza)
- **Limitaciones**: Dificultad con objetos pequeños y agrupados

#### YOLOv2/YOLO9000 (2017)
- **Mejoras**:
  - Batch normalization
  - Clasificador de mayor resolución
  - Anchor boxes
  - Dimensiones de clusters
  - Fine-grained features
- **YOLO9000**: Capaz de detectar más de 9000 categorías mediante jerarquía WordTree

#### YOLOv3 (2018)
- **Mejoras**:
  - Backbone: Darknet-53 con conexiones residuales
  - Predicciones a tres escalas diferentes
  - Mejor rendimiento en objetos pequeños
  - Función de pérdida mejorada

#### YOLOv4 (2020)
- **Innovaciones**:
  - Backbone: CSPDarknet53
  - Técnicas de aumento de datos: Mosaic, CutMix
  - Bag of Freebies (BoF) y Bag of Specials (BoS)
  - Mejoras en NMS: DIoU-NMS

#### YOLOv5 (2020)
- **Características**:
  - Implementación en PyTorch
  - Modelos de diferentes tamaños (nano a extra-large)
  - Hiperparámetros optimizados automáticamente
  - Integración con herramientas modernas (TensorBoard, MLflow)

#### YOLOv6 y YOLOv7 (2022)
- **YOLOv6**:
  - Desarrollado por Meituan
  - Optimizado para aplicaciones industriales
  - Backbone: EfficientRep

- **YOLOv7**:
  - Estado del arte en velocidad/precisión
  - E-ELAN (Extended Efficient Layer Aggregation Network)
  - Entrenamiento auxiliar y asignación de etiquetas dinámicas

#### YOLOv8 (2023)
- **Desarrollador**: Ultralytics
- **Mejoras arquitectónicas**:
  - Backbone y neck mejorados
  - Cabezas de detección desacopladas
  - Anclaje libre (anchor-free)
- **Nuevas tareas**:
  - Detección
  - Segmentación
  - Clasificación
  - Pose estimation
  - Tracking

### Arquitectura detallada de YOLOv8

#### Componentes principales

1. **Backbone**: Extracción de características
   - Basado en CSPDarknet
   - Bloques C2f (Cross-Stage Partial con conexiones residuales)
   - Captura características a diferentes escalas

2. **Neck**: Fusión de características multi-escala
   - Estructura FPN (Feature Pyramid Network) + PAN (Path Aggregation Network)
   - Permite detección de objetos a diferentes tamaños
   - Conexiones ascendentes y descendentes

3. **Head**: Predicción final
   - Detección anchor-free
   - Predicción de clases y bounding boxes
   - Decodificación directa de coordenadas

#### Innovaciones técnicas
- **Función de pérdida**: Combinación de:
  - Pérdida de clasificación (BCE - Binary Cross Entropy)
  - Pérdida de bounding box (CIoU - Complete IoU)
  - Pérdida de dualidad (DFL - Distribution Focal Loss)

- **Técnicas de entrenamiento**:
  - Mosaic y MixUp para aumento de datos
  - Warmup coseno
  - EMA (Exponential Moving Average)

### Implementación en tiempo real

#### Instalación y configuración
```bash
# Instalación de Ultralytics
pip install ultralytics
```

#### Detección básica
```python
from ultralytics import YOLO
import cv2

# Cargar modelo pre-entrenado
model = YOLO('yolov8n.pt')  # 'n' para nano, otras opciones: s, m, l, x

# Inferencia en imagen
results = model('imagen.jpg')

# Mostrar resultados
for r in results:
    im_array = r.plot()  # Imagen con detecciones
    cv2.imshow("Detección YOLOv8", im_array)
    cv2.waitKey(0)
```

#### Procesamiento de video en tiempo real
```python
from ultralytics import YOLO
import cv2
import time

# Cargar modelo
model = YOLO('yolov8n.pt')

# Abrir webcam o video
cap = cv2.VideoCapture(0)  # 0 para webcam, o ruta a archivo de video

# Configurar FPS counter
fps_start_time = 0
fps = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Calcular FPS
    fps_end_time = time.time()
    time_diff = fps_end_time - fps_start_time
    if time_diff > 1.0:
        fps = 1.0 / time_diff
        fps_start_time = fps_end_time
    
    # Inferencia
    results = model(frame)
    
    # Visualizar resultados
    annotated_frame = results[0].plot()
    
    # Mostrar FPS
    cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Mostrar frame
    cv2.imshow("YOLOv8 Detección", annotated_frame)
    
    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

#### Entrenamiento personalizado
```python
from ultralytics import YOLO

# Cargar modelo base
model = YOLO('yolov8n.pt')

# Entrenar modelo con dataset personalizado
results = model.train(
    data='config.yaml',  # Archivo de configuración del dataset
    epochs=100,          # Número de épocas
    imgsz=640,           # Tamaño de imagen
    batch=16,            # Tamaño de batch
    name='mi_modelo'     # Nombre del experimento
)

# Evaluar modelo
metrics = model.val()

# Exportar modelo para inferencia
model.export(format='onnx')  # Exportar a ONNX
```

#### Estructura del archivo de configuración (config.yaml)
```yaml
# Dataset config
path: /ruta/al/dataset  # Ruta al dataset
train: images/train     # Imágenes de entrenamiento
val: images/val         # Imágenes de validación

# Clases
nc: 3                   # Número de clases
names: ['persona', 'coche', 'bicicleta']  # Nombres de clases
```

### Aplicaciones prácticas

#### Conteo de personas y vehículos
```python
from ultralytics import YOLO
import cv2
import numpy as np
from collections import defaultdict

# Cargar modelo
model = YOLO('yolov8n.pt')

# Definir línea de conteo
line_start = (50, 500)
line_end = (1230, 500)

# Diccionarios para conteo
count = defaultdict(int)
counted_ids = set()

# Inicializar tracker
tracker = model.track

# Abrir video
cap = cv2.VideoCapture('traffic.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Tracking con YOLOv8
    results = model.track(frame, persist=True)
    
    # Dibujar línea de conteo
    cv2.line(frame, line_start, line_end, (0, 255, 0), 2)
    
    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
        track_ids = results[0].boxes.id.cpu().numpy().astype(int)
        clss = results[0].boxes.cls.cpu().numpy().astype(int)
        
        for box, track_id, cls in zip(boxes, track_ids, clss):
            # Obtener centro del objeto
            x1, y1, x2, y2 = box
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            
            # Dibujar centro y ID
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Verificar si cruza la línea
            if line_start[0] <= cx <= line_end[0]:
                if abs(cy - line_start[1]) < 15 and track_id not in counted_ids:
                    count[model.names[cls]] += 1
                    counted_ids.add(track_id)
    
    # Mostrar conteo
    y_offset = 50
    for cls, cnt in count.items():
        cv2.putText(frame, f"{cls}: {cnt}", (50, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        y_offset += 40
    
    # Mostrar resultado
    cv2.imshow("Conteo de objetos", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

#### Análisis de ocupación de espacios
```python
# Definir zonas de interés (ROIs)
rois = {
    "zona_a": [(100, 100), (300, 100), (300, 300), (100, 300)],
    "zona_b": [(400, 100), (600, 100), (600, 300), (400, 300)]
}

# Función para verificar si un punto está dentro de un polígono
def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(1, n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
            if p1x == p2x or x <= xinters:
                inside = not inside
        p1x, p1y = p2x, p2y
    return inside

# En el bucle principal
occupancy = {zone: 0 for zone in rois}

# Procesar detecciones
for box, cls in zip(boxes, clss):
    if model.names[cls] == 'person':  # Solo contar personas
        x1, y1, x2, y2 = box
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        
        # Verificar en qué zona está
        for zone, polygon in rois.items():
            if point_in_polygon((cx, cy), polygon):
                occupancy[zone] += 1

# Visualizar zonas y ocupación
for zone, polygon in rois.items():
    # Convertir a formato numpy para OpenCV
    pts = np.array(polygon, np.int32).reshape((-1, 1, 2))
    
    # Color basado en ocupación (verde->amarillo->rojo según densidad)
    max_capacity = 10  # Definir capacidad máxima
    ratio = min(1.0, occupancy[zone] / max_capacity)
    color = (0, 255 * (1 - ratio), 255 * ratio)
    
    # Dibujar zona y mostrar ocupación
    cv2.polylines(frame, [pts], True, color, 2)
    cv2.putText(frame, f"{zone}: {occupancy[zone]}", 
                (polygon[0][0], polygon[0][1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
```

### Comparación con otros modelos de detección

#### YOLO vs. Detectores de dos etapas

| Aspecto | YOLO | Faster R-CNN |
|---------|------|-------------|
| **Velocidad** | Muy rápido (30-60 FPS) | Moderado (5-10 FPS) |
| **Precisión** | Buena, especialmente en versiones recientes | Muy alta |
| **Objetos pequeños** | Rendimiento mejorado en v3+ | Excelente |
| **Objetos agrupados** | Dificultad moderada | Buen rendimiento |
| **Uso de memoria** | Eficiente | Mayor consumo |
| **Entrenamiento** | Más rápido | Más lento, multi-etapa |
| **Despliegue** | Sencillo, optimizado | Más complejo |

#### Ventajas de YOLOv8
- **Velocidad**: Ideal para aplicaciones en tiempo real
- **Precisión competitiva**: Comparable a detectores más lentos
- **Versatilidad**: Múltiples tareas con la misma arquitectura
- **Facilidad de uso**: API intuitiva y bien documentada
- **Comunidad activa**: Amplio soporte y recursos

#### Limitaciones
- **Objetos muy pequeños**: Aún presenta dificultades en algunos casos
- **Objetos muy juntos**: Puede fallar en escenas muy concurridas
- **Transferencia a dominios específicos**: Puede requerir fine-tuning extensivo
- **Explicabilidad**: Como modelo de caja negra, difícil de interpretar

## Recursos adicionales

### Libros y publicaciones académicas

#### Libros fundamentales
- **"Computer Vision: Algorithms and Applications"** por Richard Szeliski
  - Referencia completa que cubre desde fundamentos hasta aplicaciones avanzadas
  - Disponible gratuitamente en línea: http://szeliski.org/Book/

- **"Deep Learning"** por Ian Goodfellow, Yoshua Bengio y Aaron Courville
  - Capítulos dedicados a visión por computador y redes convolucionales
  - Disponible en: https://www.deeplearningbook.org/

- **"Digital Image Processing"** por Rafael C. Gonzalez y Richard E. Woods
  - Fundamentos clásicos de procesamiento de imágenes
  - Excelente para comprender técnicas tradicionales

#### Artículos científicos clave
- **Detección de objetos**:
  - "Rich feature hierarchies for accurate object detection and semantic segmentation" (R-CNN)
  - "You Only Look Once: Unified, Real-Time Object Detection" (YOLO)
  - "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks"

- **Segmentación**:
  - "U-Net: Convolutional Networks for Biomedical Image Segmentation"
  - "Mask R-CNN"
  - "Segment Anything" (SAM)

- **Tracking**:
  - "Simple Online and Realtime Tracking" (SORT)
  - "Simple Online and Realtime Tracking with a Deep Association Metric" (DeepSORT)
  - "ByteTrack: Multi-Object Tracking by Associating Every Detection Box"

### Cursos y tutoriales online

#### Cursos universitarios abiertos
- **CS231n: Convolutional Neural Networks for Visual Recognition** (Stanford)
  - Curso completo sobre CNN aplicadas a visión por computador
  - Materiales disponibles en: http://cs231n.stanford.edu/

- **Computer Vision Course** (Universidad de Washington)
  - Impartido por Steve Seitz y otros expertos en el campo
  - Cubre desde calibración de cámaras hasta reconstrucción 3D

#### Plataformas de aprendizaje
- **Coursera**: "Deep Learning Specialization" por Andrew Ng (incluye módulo de CNN)
- **Udacity**: "Computer Vision Nanodegree"
- **edX**: "Computer Vision and Image Analysis" por Microsoft

#### Tutoriales y blogs
- **PyImageSearch**: Tutoriales prácticos sobre visión por computador
- **LearnOpenCV**: Recursos educativos por Satya Mallick
- **Papers With Code**: Implementaciones de artículos científicos

### Herramientas y bibliotecas

#### Bibliotecas de visión por computador
- **OpenCV**: Biblioteca completa y madura para visión por computador
  - Implementa cientos de algoritmos clásicos y modernos
  - Interfaces para C++, Python, Java y más
  - Documentación: https://docs.opencv.org/

- **scikit-image**: Biblioteca Python para procesamiento de imágenes
  - Enfoque en algoritmos clásicos y facilidad de uso
  - Integración perfecta con el ecosistema científico de Python

- **Kornia**: Biblioteca diferenciable de visión por computador para PyTorch
  - Permite integrar operaciones de visión en pipelines de deep learning

#### Frameworks de deep learning para visión
- **TensorFlow/Keras**: Ecosistema completo con modelos pre-entrenados
  - TF-Vision: Colección de modelos y herramientas para visión

- **PyTorch**: Framework flexible con fuerte soporte para investigación
  - TorchVision: Modelos, transformaciones y datasets para visión

- **Ultralytics**: Implementación de YOLO y herramientas asociadas
  - API unificada para entrenamiento, inferencia y despliegue

#### Herramientas de anotación
- **LabelImg**: Herramienta para anotación de bounding boxes
- **CVAT**: Computer Vision Annotation Tool, plataforma completa
- **Supervisely**: Plataforma end-to-end para datos de visión por computador

#### Plataformas de despliegue
- **NVIDIA Triton**: Servidor de inferencia optimizado
- **TensorRT**: Optimización de modelos para inferencia en GPUs NVIDIA
- **OpenVINO**: Toolkit de Intel para optimización en CPUs y aceleradores
- **TF Lite / CoreML**: Despliegue en dispositivos móviles

### Conjuntos de datos públicos

#### Detección y clasificación
- **COCO (Common Objects in Context)**: 330K imágenes, 80 categorías
- **ImageNet**: Más de 14 millones de imágenes, 20K categorías
- **Pascal VOC**: Conjunto de referencia para detección de objetos

#### Segmentación
- **Cityscapes**: Segmentación semántica en escenas urbanas
- **ADE20K**: Más de 20K imágenes con segmentación de escenas
- **KITTI**: Dataset para aplicaciones de conducción autónoma

#### Video y tracking
- **MOT Challenge**: Benchmark para tracking multi-objeto
- **YouTube-VOS**: Segmentación de objetos en video
- **UCF101**: Reconocimiento de acciones en videos