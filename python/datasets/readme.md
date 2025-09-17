# DATASETS

Un **Dataset** es un ***Conjunto de Datos*** organizado y estrucutrado que se utiliza para entrenar y probar modelos de machine learning, iteligecia articial y en nuestro caso: computer vision.


Un dataset está compuesto por:
+ imágenes o videos - como datos principales
+ anotaciones / etiquetas - información sobre lo que hay en cada imagen
+ Metadatos - informaicón adicional como resolución, fecha, camara, etc.
+ Documentación - instrucciones de uso y descripción del contenido


Se utiliza para:
+ Entrenar modelos - Enseñar a un algoritmo a reconocer patrones
+ Validar resultados - Comprobar la calidad de funcionamiento de un modelo
+ Invstigar - Desarrollar nuevas técnicas y metodologías 

Es importante que los datos que componen un dataset sean fiables, precisos y diversos para mejorar los resultados obtenidos. Nunca perder de vista que el dataset que entrenará un modelo debería contar con ejemplos equiparables a las situaciones de detección real.

Características de un buen dataset:
+ Fiables - Anotaciones precisas y consistentes, datos correctos, sin erratas o confusiones
+ Diversos - Variedad de escenarios, ángulos, condiciones climáticas, condicones lumínicas (iluminación), etc.
+ Resolución - Correcta resolución o compresión del archivo. 
+ Cantidad - Contar con una cantidad suficiente de ejemplos en cada categoría.
+ Balance - Distribución equiparada entre las clases.
+ Representatividad - Coherente con los objetivos y representativo de situaciones reales.



# Tipos de anotaciones en Datasets de computer vision

## Clasificación de Imágenes:
```json
imagen_gato.jpg → "gato"
imagen_perro.jpg → "perro"
```

## Detección de objetos:
```json
imagen.jpg → [
  {clase: "persona", x: 100, y: 200, ancho: 50, alto: 100},
  {clase: "coche", x: 300, y: 150, ancho: 200, alto: 80}
]
```

## Segmentación Semántica
Cada pixel se clasifica en una categoría.
```json
// Para una imagen de 640x480 píxeles
{
  "imagen": "calle_urbana.jpg",
  "segmentacion_semantica": {
    "mapa_pixeles": [
      // Matriz 640x480 donde cada valor representa una clase:
      // 0 = fondo/cielo
      // 1 = carretera  
      // 2 = acera
      // 3 = edificio
      // 4 = coche
      // 5 = persona
      // 6 = árbol
      [0,0,0,6,6,1,1,1,4,4,5,2,2,3,3,3,...], //640 valores
      [0,0,6,6,6,1,1,4,4,4,5,5,2,3,3,3,...], //640 valores
      // ... 480 filas más con 640 valores cada una...
    ],
    "clases": {
      0: "cielo",
      1: "carretera", 
      2: "acera",
      3: "edificio",
      4: "coche",
      5: "persona",
      6: "árbol"
    }
  }
}
```


## Segmentación de instancias
Cada objeto individual tiene su propia máscara poligonal
```json
{
  "imagen": "parque.jpg",
  "instancias": [
    {
      "id": 1,
      "clase": "persona",
      "mascara": [[x1,y1], [x2,y2], [x3,y3],...], // Polígono que delimita la persona
      "bbox": [100, 150, 80, 200] // x, y, ancho, alto
    },
    {
      "id": 2, 
      "clase": "persona",
      "mascara": [[x10,y10], [x11,y11], [x12,y12],...], // Otra persona diferente
      "bbox": [300, 160, 75, 190]
    },
    {
      "id": 3,
      "clase": "perro", 
      "mascara": [[x20,y20], [x21,y21], [x22,y22],...],
      "bbox": [200, 300, 120, 80]
    }
  ]
}
```

## Traking - Multi-Object Tracking (MOT)
En tracking, seguimos objetos a través de múltiples frames de video:

```json
{
  "video": "trafico_urbano.mp4",
  "fps": 30,
  "frames": [
    {
      "frame_id": 1,
      "timestamp": 0.033,
      "objetos": [
        {
          "track_id": 101,  // ID único que persiste en el tiempo
          "clase": "coche",
          "bbox": [250, 180, 120, 60],
          "confianza": 0.95
        },
        {
          "track_id": 102,
          "clase": "persona", 
          "bbox": [400, 220, 40, 120],
          "confianza": 0.88
        }
      ]
    },
    {
      "frame_id": 2,
      "timestamp": 0.066,
      "objetos": [
        {
          "track_id": 101,  // El mismo coche, pero en nueva posición
          "clase": "coche",
          "bbox": [260, 178, 118, 62], // Se movió ligeramente
          "confianza": 0.93
        },
        {
          "track_id": 102,  // La misma persona
          "clase": "persona",
          "bbox": [405, 215, 42, 125], // También se movió
          "confianza": 0.90
        },
        {
          "track_id": 103,  // Nueva persona que apareció
          "clase": "persona",
          "bbox": [100, 200, 38, 115],
          "confianza": 0.85
        }
      ]
    },
    {
      "frame_id": 3,
      "timestamp": 0.099,
      "objetos": [
        {
          "track_id": 101,
          "clase": "coche",
          "bbox": [270, 176, 116, 64],
          "confianza": 0.91
        },
        // track_id 102 desaparece (persona salió del frame)
        {
          "track_id": 103,
          "clase": "persona", 
          "bbox": [108, 195, 40, 118],
          "confianza": 0.87
        }
      ]
    }
  ]
}
```

## Tracking con Trayectoria
```json
{
  "trayectorias": {
    "track_101": {
      "clase": "coche",
      "puntos": [
        {"frame": 1, "centro": [310, 210], "timestamp": 0.033},
        {"frame": 2, "centro": [319, 209], "timestamp": 0.066},
        {"frame": 3, "centro": [328, 208], "timestamp": 0.099},
        {"frame": 4, "centro": [337, 207], "timestamp": 0.132}
      ],
      "velocidad_promedio": "15.2 km/h",
      "direccion": "este"
    },
    "track_102": {
      "clase": "persona",
      "puntos": [
        {"frame": 1, "centro": [420, 280], "timestamp": 0.033},
        {"frame": 2, "centro": [426, 275], "timestamp": 0.066}
      ],
      "estado": "perdido_en_frame_3"
    }
  }
}
```


#DATASETS POPULARES
A continuación se listan unas referencias de datasets preexistentes con sus enlaces a:

|Tipo de Enlace     | Descripción                                               |   Qué Ofrece                                                                      |
|-------------------|-----------------------------------------------------------|-----------------------------------------------------------------------------------|
|Web oficial        |Sitio web principal del dataset mantenido por los creadores|Documentación completa, información del dataset, papers, descarga oficial          |
|GitHub             |Repositorio de código en GitHub                            |Scripts de descarga, herramientas, código de ejemplo, APIs para usar el dataset    |
|Kaggle             |Plataforma de competiciones de ML                          |Datasets listos para usar, kernels/notebooks, competiciones relacionadas           |
|Papers with Code   |Plataforma académica                                       |Leaderboards, papers que usan el dataset, comparación de métodos                   |
|TensorFlow         |Catálogo TensorFlow Datasets                               |Fácil carga con tfds.load(), preprocessing automático                              |
|HuggingFace        |Hub de modelos y datasets                                  |Integración con transformers, carga con datasets.load_dataset()                    |
|Roboflow           |Plataforma de computer vision                              |Datasets pre-procesados, formatos YOLO/COCO, herramientas de anotación             |
|Scikit-learn       |Biblioteca de ML de Python                                 |Datasets integrados, carga directa con sklearn                                     |
|AWS Open           |DataRepositorio público de Amazon                          |Datasets alojados en la nube, acceso gratuito via S3                               |

¿Cuál elegir?
-Investigación académica: Web oficial + Papers with Code
-Desarrollo rápido: Kaggle + HuggingFace
-Proyectos con código: GitHub + TensorFlow
-Computer vision: Roboflow + Ultralytics


# Datasets Generales de Detección de Objetos
- **Open Images Dataset** - Dataset masivo de Google con millones de imágenes anotadas
    - Web oficial: https://storage.googleapis.com/openimages/web/index.html
    - GitHub: https://github.com/openimages/dataset
    - TensorFlow: https://www.tensorflow.org/datasets/catalog/open_images_v4
    - Kaggle: https://www.kaggle.com/datasets/bigquery/open-images
    - Papers with Code: https://paperswithcode.com/dataset/openimages-v6

- **Pascal VOC** - Dataset clásico con 20 clases de objetos
    - Web oficial: http://host.robots.ox.ac.uk/pascal/VOC/
    - VOC 2007 Kaggle: https://www.kaggle.com/datasets/zaraks/pascal-voc-2007
    - VOC 2012 Kaggle: https://www.kaggle.com/datasets/gopalbhattrai/pascal-voc-2012-dataset
    - Roboflow: https://public.roboflow.com/object-detection/pascal-voc-2012
    - HuggingFace: https://huggingface.co/datasets/merve/pascal-voc

- **ImageNet** - Más de 14 millones de imágenes clasificadas en miles de categorías
    - Web oficial: https://www.image-net.org/
    - Kaggle: https://www.kaggle.com/c/imagenet-object-localization-challenge

- **Objects365** - 365 categorías de objetos cotidianos
    - Web oficial: https://www.objects365.org/
    - GitHub: https://github.com/megvii-research/Objects365

- **LVIS** - Large Vocabulary Instance Segmentation con más de 1000 categorías
    - Web oficial: https://www.lvisdataset.org/
    - GitHub: https://github.com/lvis-dataset/lvis-api


# Datasets de Segmentación
- Cityscapes - Segmentación semántica urbana para conducción autónoma
- ADE20K - Segmentación de escenas con 150 clases semánticas
- Mapillary Vistas - Dataset de segmentación para navegación urbana
- KITTI - Datasets para vehículos autónomos (detección, segmentación, flujo óptico)

# Datasets de Reconocimiento Facial
- WIDER FACE - Detección de rostros en escenarios diversos
- CelebA - Atributos faciales y landmarks
- LFW - Labeled Faces in the Wild para verificación facial
- VGGFace2 - Dataset a gran escala para reconocimiento facial

# Datasets Médicos
- MIMIC-CXR - Radiografías de tórax con reportes
- NIH Chest X-rays - 100,000+ radiografías de tórax
- ISIC - Imágenes dermatológicas para detección de melanoma
- BraTS - Segmentación de tumores cerebrales

# Datasets de Video y Acción
- Kinetics - Clasificación de acciones humanas en video
- UCF-101 - 101 categorías de acciones
- Something-Something - Interacciones humano-objeto
- YouTube-8M - Dataset masivo de videos de YouTube

# Datasets Especializados
- Fashion-MNIST - Clasificación de prendas de vestir
- Food-101 - Clasificación de 101 tipos de comida
- PlantNet - Identificación de especies de plantas
- iNaturalist - Biodiversidad y especies naturales
- Google Landmarks - Reconocimiento de monumentos mundiales [Web](https://storage.googleapis.com/gld-v2/web/index.html), [Github](https://github.com/cvdfoundation/google-landmark?tab=readme-ov-file)

# Datasets Sintéticos y 3D
- SYNTHIA - Dataset sintético para conducción urbana
- ShapeNet - Modelos 3D categorizados
- ModelNet - Clasificación de modelos 3D
- SceneNet RGB-D - Escenas 3D sintéticas

# Plataformas y Repositorios
- Kaggle Datasets - Miles de datasets de competiciones
- Papers With Code - Datasets organizados por tareas
- AWS Open Data - Datasets públicos en la nube
- Google Dataset Search - Motor de búsqueda de datasets
- HuggingFace Datasets - Datasets fáciles de usar con transformers

# Datasets de Detección Específica
- DOTA - Detección de objetos en imágenes aéreas
- xView - Detección en imágenes satelitales
- nuScenes - Dataset 3D para vehículos autónomos
- Waymo Open Dataset - Conducción autónoma con datos LiDAR


---
#URL, pendientes mezclar de lo de arriba

## Datasets de Segmentación

### Cityscapes
- **Web oficial**: https://www.cityscapes-dataset.com/
- **GitHub**: https://github.com/mcordts/cityscapesScripts

### ADE20K
- **Web oficial**: http://groups.csail.mit.edu/vision/datasets/ADE20K/
- **GitHub**: https://github.com/CSAILVision/ADE20K

### Mapillary Vistas
- **Web oficial**: https://www.mapillary.com/dataset/vistas
- **GitHub**: https://github.com/mapillary/mapillary_vistas

### KITTI
- **Web oficial**: http://www.cvlibs.net/datasets/kitti/
- **Kaggle**: https://www.kaggle.com/datasets/twaldo/kitti-object-detection

## Datasets de Reconocimiento Facial

### WIDER FACE
- **Web oficial**: http://shuoyang1213.me/WIDERFACE/
- **GitHub**: https://github.com/wondervictor/WiderFace-to-TFRecord

### CelebA
- **Web oficial**: http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
- **Kaggle**: https://www.kaggle.com/datasets/jessicali9530/celeba-dataset

### LFW
- **Web oficial**: http://vis-www.cs.umass.edu/lfw/
- **Scikit-learn**: http://scikit-learn.org/stable/datasets/labeled_faces.html

### VGGFace2
- **Web oficial**: https://github.com/ox-vgg/vgg_face2

## Datasets Médicos

### MIMIC-CXR
- **Web oficial**: https://physionet.org/content/mimic-cxr/
- **GitHub**: https://github.com/MIT-LCP/mimic-cxr

### NIH Chest X-rays
- **Web oficial**: https://nihcc.app.box.com/v/ChestXray-NIHCC
- **Kaggle**: https://www.kaggle.com/datasets/nih-chest-xrays/data

### ISIC
- **Web oficial**: https://www.isic-archive.com/
- **Kaggle**: https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic

### BraTS
- **Web oficial**: http://braintumorsegmentation.org/
- **Kaggle**: https://www.kaggle.com/datasets/awsaf49/brats2020-training-data

## Datasets de Video y Acción

### Kinetics
- **Web oficial**: https://deepmind.com/research/open-source/kinetics
- **GitHub**: https://github.com/deepmind/kinetics-i3d

### UCF-101
- **Web oficial**: https://www.crcv.ucf.edu/data/UCF101.php
- **Kaggle**: https://www.kaggle.com/datasets/matthewjansen/ucf101-action-recognition

### Something-Something
- **Web oficial**: https://developer.qualcomm.com/software/ai-datasets/something-something
- **GitHub**: https://github.com/TwentyBN/something-something-v2-baseline

### YouTube-8M
- **Web oficial**: https://research.google.com/youtube8m/
- **Kaggle**: https://www.kaggle.com/c/youtube8m-2019

## Datasets Especializados

### Fashion-MNIST
- **GitHub**: https://github.com/zalandoresearch/fashion-mnist
- **Kaggle**: https://www.kaggle.com/datasets/zalando-research/fashionmnist

### Food-101
- **Web oficial**: https://www.vision.ee.ethz.ch/datasets_extra/food-101/
- **Kaggle**: https://www.kaggle.com/datasets/dansbecker/food-101

### PlantNet
- **Web oficial**: https://plantnet.org/en/
- **Kaggle**: https://www.kaggle.com/c/plantnet-2021-fgvc8

### iNaturalist
- **Web oficial**: https://www.inaturalist.org/pages/developers
- **Kaggle**: https://www.kaggle.com/c/inaturalist-2021

### Google Landmarks
- **Web oficial**: https://storage.googleapis.com/gld-v2/web/index.html
- **GitHub**: https://github.com/cvdfoundation/google-landmark
- **Kaggle**: https://www.kaggle.com/c/landmark-recognition-2021

## Datasets Sintéticos y 3D

### SYNTHIA
- **Web oficial**: https://synthia-dataset.net/
- **GitHub**: https://github.com/mcordts/cityscapesScripts

### ShapeNet
- **Web oficial**: https://www.shapenet.org/
- **GitHub**: https://github.com/laughtervv/DISN

### ModelNet
- **Web oficial**: https://modelnet.cs.princeton.edu/
- **GitHub**: https://github.com/lmb-freiburg/orion

### SceneNet RGB-D
- **Web oficial**: https://robotvault.bitbucket.io/scenenet-rgbd.html
- **GitHub**: https://github.com/jmccormac/SceneNetRGB-D

## Plataformas y Repositorios

### Kaggle Datasets
- **Web oficial**: https://www.kaggle.com/datasets

### Papers With Code
- **Web oficial**: https://paperswithcode.com/datasets

### AWS Open Data
- **Web oficial**: https://registry.opendata.aws/

### Google Dataset Search
- **Web oficial**: https://datasetsearch.research.google.com/

### HuggingFace Datasets
- **Web oficial**: https://huggingface.co/datasets

## Datasets de Detección Específica

### DOTA
- **Web oficial**: https://captain-whu.github.io/DOTA/index.html
- **GitHub**: https://github.com/CAPTAIN-WHU/DOTA_devkit

### xView
- **Web oficial**: http://xviewdataset.org/
- **GitHub**: https://github.com/DIUx-xView

### nuScenes
- **Web oficial**: https://www.nuscenes.org/
- **GitHub**: https://github.com/nutonomy/nuscenes-devkit

### Waymo Open Dataset
- **Web oficial**: https://waymo.com/open/
- **GitHub**: https://github.com/waymo-research/waymo-open-dataset

## Herramientas Adicionales

### COCO Dataset
- **Web oficial**: https://cocodataset.org/
- **GitHub**: https://github.com/cocodataset/cocoapi

### Roboflow
- **Web oficial**: https://roboflow.com/
- **Public datasets**: https://public.roboflow.com/

### Ultralytics Hub
- **Web oficial**: https://hub.ultralytics.com/
