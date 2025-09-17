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



# Datasets Generales de Detección de Objetos
- Open Images Dataset - Dataset masivo de Google con millones de imágenes anotadas
- Pascal VOC - Dataset clásico con 20 clases de objetos
- ImageNet - Más de 14 millones de imágenes clasificadas en miles de categorías
- Objects365 - 365 categorías de objetos cotidianos
- LVIS - Large Vocabulary Instance Segmentation con más de 1000 categorías

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