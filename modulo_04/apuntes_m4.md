# Módulo 04: Sistemas de Visión 3D Artificial

## Visión 3D vs. 2D: Diferencias Fundamentales y Ventajas del Análisis Tridimensional

### Diferencias fundamentales

| Característica | Visión 2D | Visión 3D |
|---------------|-----------|----------|
| Dimensiones | Trabaja con imágenes planas (X, Y) | Incorpora información de profundidad (X, Y, Z) |
| Información | Limitada a color, textura y formas bidimensionales | Incluye volumen, profundidad, posición espacial real |
| Oclusiones | Difícil manejo de objetos parcialmente ocultos | Mejor manejo de oclusiones parciales |
| Perspectiva | Distorsiones difíciles de compensar | Representación más fiel a la realidad física |

### Ventajas del análisis tridimensional

- **Mediciones precisas**: Capacidad para obtener dimensiones reales de objetos
- **Reconocimiento robusto**: Menor sensibilidad a cambios de iluminación y perspectiva
- **Interacción espacial**: Comprensión de relaciones espaciales entre objetos
- **Navegación**: Capacidad mejorada para sistemas autónomos (robots, vehículos)
- **Reconstrucción**: Posibilidad de crear modelos digitales precisos de objetos y entornos reales

## Captura de Datos 3D: Técnicas de Adquisición y Procesamiento

### Técnicas activas

- **Escáner láser (LiDAR)**
  - Principio: Medición del tiempo de vuelo de pulsos láser
  - Aplicaciones: Vehículos autónomos, cartografía, arquitectura
  - Ventajas: Alta precisión, largo alcance
  - Desventajas: Coste elevado, problemas con superficies reflectantes

- **Luz estructurada**
  - Principio: Proyección de patrones conocidos y análisis de deformaciones
  - Aplicaciones: Escáneres 3D de corto alcance, sistemas de control de calidad
  - Ventajas: Alta resolución, buena precisión a corta distancia
  - Desventajas: Limitado alcance, sensible a condiciones de iluminación

- **Time-of-Flight (ToF)**
  - Principio: Medición del tiempo que tarda la luz en rebotar en objetos
  - Aplicaciones: Cámaras de profundidad, sistemas de reconocimiento gestual
  - Ventajas: Captura en tiempo real, compacto
  - Desventajas: Menor resolución que otras técnicas

### Técnicas pasivas

- **Visión estéreo**
  - Principio: Triangulación basada en dos o más cámaras
  - Aplicaciones: Robótica, realidad aumentada
  - Ventajas: No requiere emisores, similar al sistema visual humano
  - Desventajas: Dificultades en superficies sin textura

- **Fotogrametría**
  - Principio: Reconstrucción 3D a partir de múltiples fotografías 2D
  - Aplicaciones: Modelado 3D, arqueología, topografía
  - Ventajas: Bajo coste, alta fidelidad de color y textura
  - Desventajas: Proceso computacionalmente intensivo

- **Structure from Motion (SfM)**
  - Principio: Reconstrucción 3D a partir de secuencias de imágenes en movimiento
  - Aplicaciones: Mapeo 3D, realidad virtual
  - Ventajas: Funciona con cámaras convencionales
  - Desventajas: Requiere suficiente movimiento y textura

### Procesamiento de datos 3D

- **Registro (Alignment)**
  - Alineación de múltiples capturas en un sistema de coordenadas común
  - Algoritmos: ICP (Iterative Closest Point), NDT (Normal Distributions Transform)

- **Filtrado y reducción de ruido**
  - Eliminación de outliers y suavizado de superficies
  - Técnicas: Filtros estadísticos, Moving Least Squares

- **Reconstrucción de superficies**
  - Conversión de nubes de puntos a mallas poligonales
  - Métodos: Triangulación de Delaunay, Poisson Surface Reconstruction

```python
# Ejemplo de procesamiento de nube de puntos con Open3D
import open3d as o3d
import numpy as np

# Cargar nube de puntos
pcd = o3d.io.read_point_cloud("ejemplo.pcd")

# Filtrado de outliers estadísticos
pcd_filtered, _ = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)

# Estimación de normales (necesario para reconstrucción)
pcd_filtered.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))

# Reconstrucción de superficie usando Poisson
mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd_filtered, depth=9)

# Visualización
o3d.visualization.draw_geometries([mesh])

```python

## Representación y Modelado: 3D CNNs, Poisson Surface Reconstruction y Point Cloud Processing
### Redes Neuronales Convolucionales 3D (3D CNNs)
- Fundamentos
  
  - Extensión de CNNs 2D a datos volumétricos
  - Convoluciones 3D: filtros que operan en tres dimensiones
  - Aplicaciones: análisis de vóxeles, secuencias temporales, datos médicos (CT, MRI)
- Arquitecturas populares
  
  - 3D U-Net: segmentación volumétrica
  - VoxNet: reconocimiento de objetos en vóxeles
  - PointNet/PointNet++: procesamiento directo de nubes de puntos

  ```# Ejemplo simplificado de una CNN 3D con TensorFlow/Keras
import tensorflow as tf
from tensorflow.keras import layers

def create_3d_cnn_model(input_shape, num_classes):
    inputs = tf.keras.Input(input_shape)
    
    # Bloque convolucional 3D
    x = layers.Conv3D(32, kernel_size=3, activation="relu")(inputs)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)
    
    x = layers.Conv3D(64, kernel_size=3, activation="relu")(x)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)
    
    # Clasificación
    x = layers.GlobalAveragePooling3D()(x)
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)
    
    return tf.keras.Model(inputs, outputs)

# Crear modelo para volúmenes 3D de 64x64x64 con 1 canal
model = create_3d_cnn_model((64, 64, 64, 1), num_classes=10)
model.summary()
```


### Poisson Surface Reconstruction
- Fundamentos
  
  - Técnica matemática para reconstruir superficies a partir de nubes de puntos orientadas
  - Resuelve una ecuación de Poisson para encontrar una función implícita cuyo gradiente se ajuste a los vectores normales
- Proceso
  
  1. Estimación de normales en cada punto
  2. Definición de una función indicadora (dentro/fuera)
  3. Resolución de la ecuación de Poisson
  4. Extracción de isosuperficie mediante Marching Cubes
- Ventajas y limitaciones
  
  - Ventajas: Reconstrucción suave, robusta al ruido, manejo de huecos
  - Limitaciones: Requiere normales precisas, puede crear artefactos en datos incompletos
### Point Cloud Processing
- Representación
  
  - Nubes de puntos: conjuntos de puntos 3D (x,y,z) con atributos adicionales (color, normal, etc.)
  - Estructuras de datos: KD-trees, octrees para búsquedas eficientes
- Operaciones fundamentales
  
  - Registro (alineación de múltiples nubes)
  - Segmentación (agrupación de puntos por características)
  - Clasificación (etiquetado de puntos según categorías)
  - Downsampling (reducción de densidad manteniendo características)

```python
# Ejemplo de procesamiento de nubes de puntos con PyTorch3D
import torch
from pytorch3d.structures import Pointclouds
from pytorch3d.ops import sample_points_from_meshes
from pytorch3d.loss import chamfer_distance

# Crear nubes de puntos sintéticas
points_a = torch.rand(1, 1000, 3)  # batch_size=1, 1000 puntos, 3 coordenadas
points_b = torch.rand(1, 1000, 3)

# Crear estructuras de nubes de puntos
pcl_a = Pointclouds(points=points_a)
pcl_b = Pointclouds(points=points_b)

# Calcular distancia de Chamfer entre nubes de puntos
loss, _ = chamfer_distance(pcl_a.points_padded(), pcl_b.points_padded())
print(f"Distancia de Chamfer: {loss.item()}")
```

## Aplicaciones a la Vida Cotidiana: Medicina, Videojuegos, Robótica
### Medicina
- Diagnóstico por imagen 3D
  
  - Reconstrucción volumétrica de CT y MRI
  - Segmentación de órganos y tejidos
  - Planificación quirúrgica personalizada
- Cirugía asistida por ordenador
  
  - Navegación quirúrgica con realidad aumentada
  - Simulación de procedimientos
  - Robótica quirúrgica guiada por visión 3D
- Prótesis y ortesis personalizadas
  
  - Escaneo 3D de miembros
  - Diseño adaptado a la anatomía del paciente
  - Fabricación mediante impresión 3D
### Videojuegos y Entretenimiento
- Captura de movimiento
  
  - Digitalización de actores para animación realista
  - Seguimiento facial para expresiones
  - Interacción corporal con sistemas de juego
- Modelado 3D
  
  - Escaneo de objetos reales para entornos virtuales
  - Reconstrucción de escenarios para juegos basados en localizaciones reales
- Interfaces naturales
  
  - Control gestual mediante cámaras de profundidad
  - Seguimiento corporal sin marcadores
  - Experiencias inmersivas en VR/AR
### Robótica
- Navegación autónoma
  
  - Mapeo 3D del entorno (SLAM - Simultaneous Localization and Mapping)
  - Detección y evasión de obstáculos
  - Planificación de rutas en entornos complejos
- Manipulación de objetos
  
  - Reconocimiento 3D para identificación de objetos
  - Estimación de pose para agarre preciso
  - Interacción con objetos deformables
- Robótica colaborativa
  
  - Percepción espacial para trabajo seguro junto a humanos
  - Comprensión de gestos y postura humana
  - Transferencia de habilidades mediante demostración

```python
# Ejemplo simplificado de SLAM visual con Python
import cv2
import numpy as np
import g2o

# Clase simplificada para Visual SLAM
class SimpleVisualSLAM:
    def __init__(self):
        self.poses = []  # Historial de poses de cámara
        self.points_3d = []  # Puntos 3D del mapa
        self.optimizer = g2o.SparseOptimizer()
        # Configuración del optimizador...
        
    def process_frame(self, frame, depth):
        # Extraer características
        orb = cv2.ORB_create()
        keypoints, descriptors = orb.detectAndCompute(frame, None)
        
        if len(self.poses) > 0:
            # Hacer matching con frame anterior
            # Estimar movimiento
            # Actualizar pose
            # Triangular nuevos puntos 3D
            # Optimizar mapa (bundle adjustment)
            pass
        else:
            # Inicializar primera pose
            self.poses.append(np.eye(4))
        
        return self.poses[-1], self.points_3d

# Uso (pseudocódigo)
# slam = SimpleVisualSLAM()
# for frame, depth in camera.read_frames():
#     pose, map_points = slam.process_frame(frame, depth)
#     visualize(frame, pose, map_points)
```


## Visión Artificial para Fusionar Mundo Real y Elementos Virtuales: Realidad Aumentada
### Fundamentos de la Realidad Aumentada
- Componentes clave
  
  - Seguimiento (tracking): localización precisa de la cámara en el espacio
  - Reconocimiento: identificación de objetos, superficies o marcadores
  - Renderizado: superposición de elementos virtuales con perspectiva correcta
- Tipos de tracking
  
  - Basado en marcadores: reconocimiento de patrones específicos
  - Markerless: SLAM visual, detección de características naturales
  - Híbrido: combinación de sensores (cámara, IMU, GPS)
### Tecnologías habilitadoras
- SLAM (Simultaneous Localization and Mapping)
  
  - Construcción de mapa 3D mientras se estima la posición
  - Variantes: MonoSLAM, ORB-SLAM, LSD-SLAM, PTAM
- Detección de planos y superficies
  
  - Segmentación de planos en nubes de puntos
  - Estimación de normales y límites
  - Anclaje de objetos virtuales a superficies reales
- Oclusión y sombreado realista
  
  - Mapas de profundidad para oclusión correcta
  - Estimación de iluminación para sombreado coherente
  - Interacción física simulada entre objetos reales y virtuales
### Frameworks y herramientas
- ARKit (Apple)
  
  - Tracking visual-inercial
  - Detección de planos y estimación de iluminación
  - People Occlusion y Motion Capture
- ARCore (Google)
  
  - Environmental understanding
  - Motion tracking y estimación de luz
  - Anchors y Cloud Anchors para experiencias compartidas
- Bibliotecas multiplataforma
  
  - OpenCV + OpenGL: solución personalizada de bajo nivel
  - Vuforia: reconocimiento de imágenes y objetos
  - AR.js: realidad aumentada para web


  ```python
  // Ejemplo simplificado de AR.js para web
<!DOCTYPE html>
<html>
<head>
    <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
    <script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar.js"></script>
</head>
<body style="margin: 0; overflow: hidden;">
    <a-scene embedded arjs="sourceType: webcam; debugUIEnabled: false;">
        <!-- Definir un marcador -->
        <a-marker preset="hiro">
            <!-- Contenido 3D que aparecerá sobre el marcador -->
            <a-box position="0 0.5 0" material="color: red;"></a-box>
        </a-marker>
        
        <!-- Configuración de cámara -->
        <a-entity camera></a-entity>
    </a-scene>
</body>
</html>
````

### Aplicaciones de la Realidad Aumentada
- Industria y manufactura
  
  - Asistencia en montaje y mantenimiento
  - Visualización de instrucciones superpuestas
  - Formación de personal técnico
- Comercio y marketing
  
  - Prueba virtual de productos (muebles, ropa, maquillaje)
  - Catálogos interactivos
  - Experiencias de marca inmersivas
- Educación y formación
  
  - Modelos 3D interactivos para ciencias
  - Simulaciones de laboratorio
  - Visualización de conceptos abstractos
- Navegación y turismo
  
  - Información contextual superpuesta
  - Reconstrucción virtual de sitios históricos
  - Traducción visual de señales y textos
## Recursos Adicionales
### Bibliotecas y frameworks
- Open3D : Biblioteca de código abierto para procesamiento 3D
- PCL (Point Cloud Library) : Procesamiento avanzado de nubes de puntos
- PyTorch3D : Herramientas de deep learning para datos 3D
- OpenCV 3D : Módulos de visión estéreo y reconstrucción 3D
- ARKit/ARCore : SDKs para desarrollo de realidad aumentada
### Datasets públicos
- ShapeNet : Gran colección de modelos 3D categorizados
- ScanNet : Dataset de escaneos RGB-D de interiores
- KITTI : Dataset para aplicaciones de conducción autónoma
- ModelNet : Modelos 3D para clasificación y segmentación
### Tutoriales y cursos
- Cursos online : Computer Vision and 3D Geometry (Stanford), 3D Computer Vision (TUM)
- Libros : "Multiple View Geometry in Computer Vision" (Hartley & Zisserman), "3D Deep Learning with Python" (Elgendy)
### Herramientas de visualización
- MeshLab : Procesamiento y edición de mallas 3D
- CloudCompare : Análisis de nubes de puntos
- Blender : Modelado, renderizado y animación 3D
## Conclusiones
- La visión 3D representa un salto cualitativo respecto a los sistemas 2D tradicionales
- Las técnicas de captura 3D permiten digitalizar el mundo real con precisión creciente
- Los avances en deep learning 3D están mejorando el procesamiento de datos volumétricos
- Las aplicaciones abarcan múltiples sectores, desde medicina hasta entretenimiento
- La realidad aumentada constituye un puente entre lo real y lo virtual, con aplicaciones transformadoras

