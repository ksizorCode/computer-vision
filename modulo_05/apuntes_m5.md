
# Módulo 05: Ventajas de la Visión Artificial

## Importancia de esta tecnología: precisión, calidad, rentabilidad, sostenibilidad y seguridad

La visión artificial se ha convertido en una tecnología transformadora en múltiples sectores debido a sus numerosas ventajas:

### Precisión
- **Mediciones exactas**: Capacidad para realizar mediciones con precisión submilimétrica
- **Consistencia**: Resultados reproducibles sin la variabilidad del factor humano
- **Detección de detalles**: Identificación de características imperceptibles para el ojo humano

### Calidad
- **Inspección al 100%**: Posibilidad de examinar todos los productos, no solo muestras
- **Detección temprana**: Identificación de defectos en fases iniciales del proceso productivo
- **Trazabilidad**: Registro completo del proceso de inspección para auditorías

### Rentabilidad
- **Reducción de costes operativos**: Menor necesidad de personal para tareas repetitivas
- **Disminución de errores**: Menos rechazos y devoluciones por defectos no detectados
- **Mayor productividad**: Velocidad de inspección superior a la humana
- **ROI cuantificable**: Ejemplo de cálculo:

```python
# Ejemplo simplificado de cálculo de ROI para un sistema de visión artificial
def calcular_roi_vision_artificial(coste_sistema, ahorro_anual, vida_util):
    roi = (ahorro_anual * vida_util - coste_sistema) / coste_sistema * 100
    return roi

# Parámetros de ejemplo
coste_sistema = 50000  # Coste de implementación del sistema en €
ahorro_anual = 20000   # Ahorro anual en costes de personal, reducción de errores, etc.
vida_util = 5          # Vida útil estimada en años

roi = calcular_roi_vision_artificial(coste_sistema, ahorro_anual, vida_util)
print(f"ROI estimado: {roi:.2f}%")
# Resultado: ROI estimado: 100.00%
```


### Sostenibilidad
- Optimización de recursos : Menor desperdicio de materiales y energía
- Reducción de desechos : Detección temprana evita procesamiento innecesario
- Eficiencia energética : Sistemas modernos con bajo consumo energético
- Impacto ambiental : Reducción de la huella de carbono en procesos industriales
### Seguridad
- Entornos peligrosos : Inspección remota en ambientes hostiles o tóxicos
- Prevención de accidentes : Detección de situaciones de riesgo en tiempo real
- Seguridad alimentaria : Identificación de contaminantes o cuerpos extraños
- Ciberseguridad : Sistemas de reconocimiento biométrico para acceso seguro
## Posicionamiento preciso
### Técnicas: detección de marcadores visuales con cámara y sensores en tiempo real Marcadores fiduciales
- Marcadores ArUco : Patrones binarios cuadrados para posicionamiento preciso
- AprilTags : Alta precisión incluso con cámaras de baja resolución
- QR y códigos de barras 2D : Para identificación y posicionamiento simultáneo


```python
# Ejemplo de detección de marcadores ArUco con OpenCV
import cv2
import numpy as np
from cv2 import aruco

def detectar_marcadores(imagen):
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Definir el diccionario de marcadores
    diccionario = aruco.Dictionary_get(aruco.DICT_6X6_250)
    
    # Parámetros para la detección
    parametros = aruco.DetectorParameters_create()
    
    # Detectar marcadores
    esquinas, ids, rechazados = aruco.detectMarkers(gris, diccionario, parameters=parametros)
    
    # Dibujar marcadores detectados
    imagen_marcada = imagen.copy()
    if ids is not None:
        aruco.drawDetectedMarkers(imagen_marcada, esquinas, ids)
        
        # Calcular posición 3D (requiere calibración de cámara)
        for i, esquina in enumerate(esquinas):
            # Extraer las 4 esquinas del marcador
            c = esquina[0]
            # Calcular el centro del marcador
            centro_x = int(np.mean(c[:, 0]))
            centro_y = int(np.mean(c[:, 1]))
            cv2.circle(imagen_marcada, (centro_x, centro_y), 5, (0, 255, 0), -1)
            cv2.putText(imagen_marcada, f"ID: {ids[i][0]}", (centro_x, centro_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return imagen_marcada, esquinas, ids

# Uso (comentado para evitar errores de ejecución)
# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# imagen_resultado, esquinas, ids = detectar_marcadores(frame)
# cv2.imshow('Marcadores detectados', imagen_resultado)
```

Sistemas de posicionamiento visual
- Visual SLAM (Simultaneous Localization and Mapping) : Construcción de mapa y localización simultánea
- Structure from Motion : Reconstrucción 3D a partir de múltiples vistas 2D
- Visual-Inertial Odometry : Combinación de cámaras con sensores inerciales (IMU) Calibración y precisión
- Calibración de cámaras : Corrección de distorsiones para mediciones precisas
- Triangulación : Determinación de coordenadas 3D mediante múltiples cámaras
- Fusión sensorial : Combinación de datos visuales con otros sensores (láser, ultrasonido)
### Aplicaciones en robótica, logística y almacenamiento Robótica
- Navegación autónoma : Robots móviles que se desplazan usando referencias visuales
- Pick and place : Brazos robóticos que localizan y manipulan objetos con precisión
- Ensamblaje preciso : Posicionamiento exacto de componentes en fabricación Logística
- Seguimiento de inventario : Localización de productos mediante marcadores visuales
- Clasificación automática : Sistemas de ordenación basados en códigos visuales
- Carga/descarga autónoma : Vehículos guiados por visión (AGVs) Almacenamiento
- Gestión de almacenes : Optimización del espacio mediante mapeo visual
- Picking automatizado : Robots que seleccionan productos específicos
- Inventario en tiempo real : Monitorización continua de existencias
Caso de estudio: Sistema de almacenamiento automatizado

Un centro logístico implementó un sistema de visión artificial para la gestión de su almacén:

- 50 robots autónomos equipados con cámaras estéreo
- Marcadores ArUco en estanterías y zonas de tránsito
- Precisión de posicionamiento: ±5mm
- Resultados:
  - Reducción del 40% en tiempos de picking
  - Disminución del 60% en errores de inventario
  - Aumento del 25% en capacidad de almacenamiento
## Identificación de productos y personas
### Técnicas: reconocimiento de patrones y formas Reconocimiento basado en características
- Detección de bordes : Algoritmos Sobel, Canny para definir contornos
- Descriptores de forma : Momentos de Hu, descriptores de Fourier
- Características locales : SIFT, SURF, ORB para puntos de interés invariantes

```python
# Ejemplo de extracción de características ORB y matching
import cv2
import numpy as np

def comparar_imagenes(img1, img2):
    # Inicializar el detector ORB
    orb = cv2.ORB_create(nfeatures=1000)
    
    # Encontrar keypoints y descriptores
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    
    # Crear matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    # Realizar matching
    matches = bf.match(des1, des2)
    
    # Ordenar por distancia
    matches = sorted(matches, key=lambda x: x.distance)
    
    # Dibujar los mejores matches
    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], None, 
                                 flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    # Calcular puntuación de similitud (menor distancia = mayor similitud)
    if len(matches) > 0:
        similitud = 1.0 - sum(m.distance for m in matches[:50]) / (50 * 100)
        similitud = max(0, min(1, similitud))  # Normalizar entre 0 y 1
    else:
        similitud = 0.0
        
    return img_matches, similitud

# Uso (comentado)
# img1 = cv2.imread('producto_referencia.jpg', cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread('producto_test.jpg', cv2.IMREAD_GRAYSCALE)
# img_resultado, similitud = comparar_imagenes(img1, img2)
# print(f"Similitud: {similitud:.2%}")
```

Técnicas basadas en aprendizaje profundo
- Redes neuronales convolucionales (CNN) : Clasificación de imágenes
- Siamese Networks : Comparación de similitud entre imágenes
- Detección de objetos : YOLO, SSD, Faster R-CNN para localización e identificación Reconocimiento óptico de caracteres (OCR)
- Lectura de códigos y texto : Identificación de números de serie, lotes, fechas
- Verificación de etiquetas : Comprobación de información impresa
- Documentación automática : Digitalización de información en papel
### Aplicaciones en reconocimiento facial y de huellas dactilares Reconocimiento facial
- Verificación de identidad : Comparación 1:1 para confirmar identidad
- Identificación : Búsqueda 1:N para determinar identidad entre múltiples personas
- Análisis de atributos : Estimación de edad, género, expresión
Proceso típico de reconocimiento facial:

1. Detección de rostro en la imagen
2. Alineación facial basada en puntos de referencia (ojos, nariz, boca)
3. Extracción de características mediante CNN
4. Comparación con base de datos de embeddings faciales


```python
# Ejemplo conceptual de reconocimiento facial con dlib
import dlib
import cv2
import numpy as np
from scipy.spatial.distance import cosine

def reconocimiento_facial(imagen, base_datos_embeddings):
    # Detector de rostros y predictor de landmarks
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    
    # Modelo de reconocimiento facial
    reconocedor = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
    
    # Detectar rostros
    rostros = detector(imagen)
    resultados = []
    
    for rostro in rostros:
        # Obtener landmarks faciales
        landmarks = predictor(imagen, rostro)
        
        # Calcular embedding facial (vector de 128 dimensiones)
        embedding = reconocedor.compute_face_descriptor(imagen, landmarks)
        embedding = np.array(embedding)
        
        # Buscar coincidencia en la base de datos
        mejor_coincidencia = None
        menor_distancia = 0.6  # Umbral de similitud (menor = más similar)
        
        for persona, emb_conocido in base_datos_embeddings.items():
            distancia = cosine(embedding, emb_conocido)  # Distancia del coseno
            if distancia < menor_distancia:
                menor_distancia = distancia
                mejor_coincidencia = persona
        
        # Dibujar resultado
        x1, y1, x2, y2 = rostro.left(), rostro.top(), rostro.right(), rostro.bottom()
        cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        if mejor_coincidencia:
            etiqueta = f"{mejor_coincidencia} ({1-menor_distancia:.2%})"
        else:
            etiqueta = "Desconocido"
            
        cv2.putText(imagen, etiqueta, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        resultados.append((mejor_coincidencia, 1-menor_distancia))
    
    return imagen, resultados
    ``` 


    Reconocimiento de huellas dactilares
- Extracción de minucias : Identificación de puntos característicos (terminaciones, bifurcaciones)
- Matching de huellas : Algoritmos de comparación basados en patrones de minucias
- Clasificación : Agrupación por tipos (arco, lazo, espiral) Consideraciones éticas y de privacidad
- Consentimiento informado : Necesidad de autorización para recopilar datos biométricos
- Seguridad de datos : Protección de información sensible mediante cifrado
- Sesgos algorítmicos : Evaluación y mitigación de discriminación potencial
- Normativas : Cumplimiento de GDPR, CCPA y otras regulaciones de privacidad
## Verificación de calidad y cumplimiento de normas
### Técnicas: comparación con modelos de referencia y análisis de diferencias Inspección basada en modelos
- Golden sample : Comparación con una muestra perfecta de referencia
- CAD matching : Verificación contra modelos de diseño asistido por ordenador
- Análisis estadístico : Detección de anomalías basada en distribuciones normales


```python
# Ejemplo de verificación de calidad mediante comparación de imágenes
import cv2
import numpy as np

def verificar_calidad(imagen_test, imagen_referencia, umbral=0.85):
    # Asegurar mismo tamaño
    imagen_test = cv2.resize(imagen_test, (imagen_referencia.shape[1], imagen_referencia.shape[0]))
    
    # Convertir a escala de grises
    gris_test = cv2.cvtColor(imagen_test, cv2.COLOR_BGR2GRAY)
    gris_ref = cv2.cvtColor(imagen_referencia, cv2.COLOR_BGR2GRAY)
    
    # Calcular diferencia absoluta
    diff = cv2.absdiff(gris_test, gris_ref)
    
    # Umbralizar para destacar diferencias significativas
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    
    # Aplicar operaciones morfológicas para reducir ruido
    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    
    # Encontrar contornos de las diferencias
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Dibujar contornos en la imagen original
    resultado = imagen_test.copy()
    cv2.drawContours(resultado, contornos, -1, (0, 0, 255), 2)
    
    # Calcular porcentaje de similitud
    pixeles_diferentes = np.count_nonzero(thresh)
    total_pixeles = thresh.shape[0] * thresh.shape[1]
    similitud = 1.0 - (pixeles_diferentes / total_pixeles)
    
    # Determinar si pasa la verificación
    pasa_verificacion = similitud >= umbral
    
    # Añadir texto con resultado
    texto = f"PASA: {similitud:.2%}" if pasa_verificacion else f"FALLA: {similitud:.2%}"
    cv2.putText(resultado, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                (0, 255, 0) if pasa_verificacion else (0, 0, 255), 2)
    
    return resultado, pasa_verificacion, similitud
    ```

    Técnicas avanzadas de inspección
- Segmentación semántica : Clasificación a nivel de píxel para identificar componentes
- Detección de anomalías : Modelos no supervisados para identificar patrones inusuales
- Análisis espectral : Inspección en rangos no visibles (infrarrojo, ultravioleta) Métricas de calidad
- Precisión y recall : Balance entre falsos positivos y falsos negativos
- Curvas ROC : Evaluación del rendimiento a diferentes umbrales
- Matrices de confusión : Análisis detallado de clasificaciones correctas e incorrectas
### Aplicaciones en control de producción y sistemas de seguridad Control de producción
- Inspección en línea : Verificación de productos durante la fabricación
- Control estadístico de procesos : Monitorización de tendencias y variaciones
- Trazabilidad : Seguimiento de productos a lo largo de la cadena de producción Sistemas de seguridad
- Verificación de documentos : Detección de falsificaciones en pasaportes, billetes
- Control de acceso : Autenticación mediante características biométricas
- Videovigilancia inteligente : Detección de comportamientos anómalos o sospechosos
Caso de estudio: Sistema de inspección de PCBs

Una empresa de electrónica implementó un sistema de visión artificial para la inspección de placas de circuito impreso:

- Cámaras de alta resolución (20MP) con iluminación especializada
- Inspección de soldaduras, componentes y posicionamiento
- Verificación contra diseños CAD
- Resultados:
  - Reducción del 95% en defectos no detectados
  - Aumento del 30% en velocidad de producción
  - ROI alcanzado en 8 meses
## Medición precisa
### Técnicas: fotogrametría, visión estéreo y sensores de profundidad Fotogrametría
- Principios : Reconstrucción de medidas a partir de fotografías
- Fotogrametría de corto alcance : Mediciones precisas en objetos cercanos
- Aerofotogrametría : Mediciones a partir de imágenes aéreas o satelitales Visión estéreo
- Principio de triangulación : Cálculo de profundidad mediante disparidad
- Calibración de sistemas estéreo : Determinación de parámetros intrínsecos y extrínsecos
- Mapas de disparidad : Representación visual de la profundidad de escena


```python
# Ejemplo de cálculo de mapa de disparidad con OpenCV
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcular_mapa_disparidad(img_izquierda, img_derecha):
    # Convertir a escala de grises
    gris_izq = cv2.cvtColor(img_izquierda, cv2.COLOR_BGR2GRAY)
    gris_der = cv2.cvtColor(img_derecha, cv2.COLOR_BGR2GRAY)
    
    # Crear objeto StereoBM
    stereo = cv2.StereoBM_create(numDisparities=128, blockSize=15)
    
    # Calcular mapa de disparidad
    disparidad = stereo.compute(gris_izq, gris_der)
    
    # Normalizar para visualización
    disparidad_norm = cv2.normalize(disparidad, None, alpha=0, beta=255, 
                                  norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    # Colorear mapa de disparidad
    disparidad_color = cv2.applyColorMap(disparidad_norm, cv2.COLORMAP_JET)
    
    return disparidad, disparidad_norm, disparidad_color

# Función para calcular distancia real a partir de disparidad
def disparidad_a_distancia(disparidad, f, B, escala=16.0):
    # f: distancia focal en píxeles
    # B: línea base (distancia entre cámaras) en metros
    # escala: factor de escala usado en el cálculo de disparidad
    
    # Evitar división por cero
    disparidad_ajustada = disparidad / escala
    mask = disparidad_ajustada > 0
    
    # Calcular distancia: Z = f*B/d
    distancia = np.zeros_like(disparidad, dtype=np.float32)
    distancia[mask] = f * B / disparidad_ajustada[mask]
    
    return distancia
    ```


    Trae

Used 1 context

Voy a crear un archivo para el módulo 4 sobre sistemas de visión 3D artificial, basándome en el contenido proporcionado por el usuario. Necesito verificar primero si existe alguna estructura de carpeta para el módulo 4 y luego crear el archivo con el contenido estructurado.

visionado/modulo_04

# Creación de archivo para el Módulo 04
Voy a crear un archivo de apuntes completo para el Módulo 04 sobre sistemas de visión 3D artificial, siguiendo el formato de los otros módulos del proyecto.

```
# Módulo 04: Sistemas de Visión 3D Artificial

## Visión 3D vs. 2D: Diferencias Fundamentales y 
Ventajas del Análisis Tridimensional

### Diferencias fundamentales

| Característica | Visión 2D | Visión 3D |
|---------------|-----------|----------|
| Dimensiones | Trabaja con imágenes planas (X, Y) 
| Incorpora información de profundidad (X, Y, Z) |
| Información | Limitada a color, textura y formas 
bidimensionales | Incluye volumen, profundidad, 
posición espacial real |
| Oclusiones | Difícil manejo de objetos 
parcialmente ocultos | Mejor manejo de oclusiones 
parciales |
| Perspectiva | Distorsiones difíciles de 
compensar | Representación más fiel a la realidad 
física |

### Ventajas del análisis tridimensional

- **Mediciones precisas**: Capacidad para obtener 
dimensiones reales de objetos
- **Reconocimiento robusto**: Menor sensibilidad a 
cambios de iluminación y perspectiva
- **Interacción espacial**: Comprensión de 
relaciones espaciales entre objetos
- **Navegación**: Capacidad mejorada para sistemas 
autónomos (robots, vehículos)
- **Reconstrucción**: Posibilidad de crear modelos 
digitales precisos de objetos y entornos reales

## Captura de Datos 3D: Técnicas de Adquisición y 
Procesamiento

### Técnicas activas

- **Escáner láser (LiDAR)**
  - Principio: Medición del tiempo de vuelo de 
pulsos láser
  - Aplicaciones: Vehículos autónomos, 
cartografía, arquitectura
  - Ventajas: Alta precisión, largo alcance
  - Desventajas: Coste elevado, problemas con 
superficies reflectantes

- **Luz estructurada**
  - Principio: Proyección de patrones conocidos y 
análisis de deformaciones
  - Aplicaciones: Escáneres 3D de corto alcance, 
sistemas de control de calidad
  - Ventajas: Alta resolución, buena precisión a 
corta distancia
  - Desventajas: Limitado alcance, sensible a 
condiciones de iluminación

- **Time-of-Flight (ToF)**
  - Principio: Medición del tiempo que tarda la 
luz en rebotar en objetos
  - Aplicaciones: Cámaras de profundidad, sistemas 
de reconocimiento gestual
  - Ventajas: Captura en tiempo real, compacto
  - Desventajas: Menor resolución que otras 
técnicas

### Técnicas pasivas

- **Visión estéreo**
  - Principio: Triangulación basada en dos o más 
cámaras
  - Aplicaciones: Robótica, realidad aumentada
  - Ventajas: No requiere emisores, similar al 
sistema visual humano
  - Desventajas: Dificultades en superficies sin 
textura

- **Fotogrametría**
  - Principio: Reconstrucción 3D a partir de 
múltiples fotografías 2D
  - Aplicaciones: Modelado 3D, arqueología, 
topografía
  - Ventajas: Bajo coste, alta fidelidad de color 
y textura
  - Desventajas: Proceso computacionalmente 
intensivo

- **Structure from Motion (SfM)**
  - Principio: Reconstrucción 3D a partir de 
secuencias de imágenes en movimiento
  - Aplicaciones: Mapeo 3D, realidad virtual
  - Ventajas: Funciona con cámaras convencionales
  - Desventajas: Requiere suficiente movimiento y 
textura

### Procesamiento de datos 3D

- **Registro (Alignment)**
  - Alineación de múltiples capturas en un sistema 
de coordenadas común
  - Algoritmos: ICP (Iterative Closest Point), NDT 
(Normal Distributions Transform)

- **Filtrado y reducción de ruido**
  - Eliminación de outliers y suavizado de 
superficies
  - Técnicas: Filtros estadísticos, Moving Least 
Squares

- **Reconstrucción de superficies**
  - Conversión de nubes de puntos a mallas 
poligonales
  - Métodos: Triangulación de Delaunay, Poisson 
Surface Reconstruction

```python
# Ejemplo de procesamiento de nube de puntos con 
Open3D
import open3d as o3d
import numpy as np

# Cargar nube de puntos
pcd = o3d.io.read_point_cloud("ejemplo.pcd")

# Filtrado de outliers estadísticos
pcd_filtered, _ = 
pcd.remove_statistical_outlier(nb_neighbors=20, 
std_ratio=2.0)

# Estimación de normales (necesario para 
reconstrucción)
pcd_filtered.estimate_normals(search_param=o3d.geo
metry.KDTreeSearchParamHybrid(radius=0.1, 
max_nn=30))

# Reconstrucción de superficie usando Poisson
mesh, densities = 
o3d.geometry.TriangleMesh.create_from_point_cloud_
poisson(pcd_filtered, depth=9)

# Visualización
o3d.visualization.draw_geometries([mesh])
```
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
```
# Ejemplo simplificado de una CNN 3D con 
TensorFlow/Keras
import tensorflow as tf
from tensorflow.keras import layers

def create_3d_cnn_model(input_shape, num_classes):
    inputs = tf.keras.Input(input_shape)
    
    # Bloque convolucional 3D
    x = layers.Conv3D(32, kernel_size=3, 
activation="relu")(inputs)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)
    
    x = layers.Conv3D(64, kernel_size=3, 
activation="relu")(x)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)
    
    # Clasificación
    x = layers.GlobalAveragePooling3D()(x)
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, 
activation="softmax")(x)
    
    return tf.keras.Model(inputs, outputs)

# Crear modelo para volúmenes 3D de 64x64x64 con 1 
canal
model = create_3d_cnn_model((64, 64, 64, 1), 
num_classes=10)
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
```
# Ejemplo de procesamiento de nubes de puntos con 
PyTorch3D
import torch
from pytorch3d.structures import Pointclouds
from pytorch3d.ops import 
sample_points_from_meshes
from pytorch3d.loss import chamfer_distance

# Crear nubes de puntos sintéticas
points_a = torch.rand(1, 1000, 3)  # batch_size=1, 
1000 puntos, 3 coordenadas
points_b = torch.rand(1, 1000, 3)

# Crear estructuras de nubes de puntos
pcl_a = Pointclouds(points=points_a)
pcl_b = Pointclouds(points=points_b)

# Calcular distancia de Chamfer entre nubes de 
puntos
loss, _ = chamfer_distance(pcl_a.points_padded(), 
pcl_b.points_padded())
print(f"Distancia de Chamfer: {loss.item()}")
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
```
# Ejemplo simplificado de SLAM visual con Python
import cv2
import numpy as np
import g2o

# Clase simplificada para Visual SLAM
class SimpleVisualSLAM:
    def __init__(self):
        self.poses = []  # Historial de poses de 
cámara
        self.points_3d = []  # Puntos 3D del mapa
        self.optimizer = g2o.SparseOptimizer()
        # Configuración del optimizador...
        
    def process_frame(self, frame, depth):
        # Extraer características
        orb = cv2.ORB_create()
        keypoints, descriptors = 
orb.detectAndCompute(frame, None)
        
        if len(self.poses) > 0:
            # Hacer matching con frame anterior
            # Estimar movimiento
            # Actualizar pose
            # Triangular nuevos puntos 3D
            # Optimizar mapa (bundle adjustment)
            pass
        else:
            # Inicializar primera pose
            self.poses.append(np.eye(4))
        
        return self.poses[-1], self.points_3d

# Uso (pseudocódigo)
# slam = SimpleVisualSLAM()
# for frame, depth in camera.read_frames():
#     pose, map_points = slam.process_frame(frame, 
depth)
#     visualize(frame, pose, map_points)
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
```
// Ejemplo simplificado de AR.js para web
<!DOCTYPE html>
<html>
<head>
    <script 
src="https://aframe.io/releases/1.2.0/aframe.min.j
s"></script>
    <script src="https://raw.githack.com/AR-js-
org/AR.js/master/aframe/build/aframe-ar.js">
</script>
</head>
<body style="margin: 0; overflow: hidden;">
    <a-scene embedded arjs="sourceType: webcam; 
debugUIEnabled: false;">
        <!-- Definir un marcador -->
        <a-marker preset="hiro">
            <!-- Contenido 3D que aparecerá sobre 
el marcador -->
            <a-box position="0 0.5 0" 
material="color: red;"></a-box>
        </a-marker>
        
        <!-- Configuración de cámara -->
        <a-entity camera></a-entity>
    </a-scene>
</body>
</html>
```
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
```

He creado un archivo completo para el Módulo 04 
sobre sistemas de visión 3D artificial, siguiendo 
la estructura que indicaste. El archivo incluye:

1. Comparación detallada entre visión 2D y 3D
2. Técnicas de captura de datos 3D (activas y 
pasivas)
3. Representación y modelado 3D (CNNs 3D, Poisson, 
nubes de puntos)
4. Aplicaciones prácticas en medicina, videojuegos 
y robótica
5. Sección sobre realidad aumentada
6. Recursos adicionales para profundizar

Cada sección incluye ejemplos de código relevantes 
y explicaciones técnicas. El archivo se ha 
guardado como `apuntes_m4.md` en la carpeta 
`modulo_04`.
```

ksizorCode

Copy

Delete

vamos a por el módulo 5

crea apuntes para el archivo apuntes_m5.md basado en este temario:

## Módulo 05: Ventajas (95 horas)

- Importancia de esta tecnología: precisión, calidad, rentabilidad, sostenibilidad y seguridad.

- Posicionamiento preciso:

- Técnicas: detección de marcadores visuales con cámara y sensores en tiempo real.

- Aplicaciones en robótica, logística y almacenamiento.

- Identificación de productos y personas:

- Técnicas: reconocimiento de patrones y formas.

- Aplicaciones en reconocimiento facial y de huellas dactilares.

- Verificación de calidad y cumplimiento de normas:

- Técnicas: comparación con modelos de referencia y análisis de diferencias.

- Aplicaciones en control de producción y sistemas de seguridad.

- Medición precisa:

- Técnicas: fotogrametría, visión estéreo y sensores de profundidad.

- Aplicaciones en control de calidad, medición de movimiento y velocidad en vídeo.

- Detección de defectos en productos y personas:

- Técnicas: análisis de patrones y texturas.

- Aplicaciones en control de fabricación y detección de anomalías médicas.

- Soluciones de visión:

- Técnicas: cámaras y sensores especializados.

- Aplicaciones en dispositivos médicos y automatización de procesos.

Trae

Voy a crear contenido detallado para el archivo apuntes_m5.md basado en el temario proporcionado sobre las ventajas de la visión artificial. Primero verificaré si el archivo ya existe y su contenido actual.

modulo_05/apuntes_m5.md

# Módulo 05: Ventajas de la Visión Artificial
Voy a desarrollar el contenido para el archivo apuntes_m5.md basado en el temario proporcionado, expandiendo cada sección con información detallada, ejemplos prácticos y código relevante.

```
# Módulo 05: Ventajas de la Visión Artificial

## Importancia de esta tecnología: precisión, 
calidad, rentabilidad, sostenibilidad y seguridad

La visión artificial se ha convertido en una 
tecnología transformadora en múltiples sectores 
debido a sus numerosas ventajas:

### Precisión
- **Mediciones exactas**: Capacidad para realizar 
mediciones con precisión submilimétrica
- **Consistencia**: Resultados reproducibles sin 
la variabilidad del factor humano
- **Detección de detalles**: Identificación de 
características imperceptibles para el ojo humano

### Calidad
- **Inspección al 100%**: Posibilidad de examinar 
todos los productos, no solo muestras
- **Detección temprana**: Identificación de 
defectos en fases iniciales del proceso productivo
- **Trazabilidad**: Registro completo del proceso 
de inspección para auditorías

### Rentabilidad
- **Reducción de costes operativos**: Menor 
necesidad de personal para tareas repetitivas
- **Disminución de errores**: Menos rechazos y 
devoluciones por defectos no detectados
- **Mayor productividad**: Velocidad de inspección 
superior a la humana
- **ROI cuantificable**: Ejemplo de cálculo:

```python
# Ejemplo simplificado de cálculo de ROI para un 
sistema de visión artificial
def calcular_roi_vision_artificial(coste_sistema, 
ahorro_anual, vida_util):
    roi = (ahorro_anual * vida_util - 
coste_sistema) / coste_sistema * 100
    return roi

# Parámetros de ejemplo
coste_sistema = 50000  # Coste de implementación 
del sistema en €
ahorro_anual = 20000   # Ahorro anual en costes de 
personal, reducción de errores, etc.
vida_util = 5          # Vida útil estimada en 
años

roi = 
calcular_roi_vision_artificial(coste_sistema, 
ahorro_anual, vida_util)
print(f"ROI estimado: {roi:.2f}%")
# Resultado: ROI estimado: 100.00%
```
### Sostenibilidad
- Optimización de recursos : Menor desperdicio de materiales y energía
- Reducción de desechos : Detección temprana evita procesamiento innecesario
- Eficiencia energética : Sistemas modernos con bajo consumo energético
- Impacto ambiental : Reducción de la huella de carbono en procesos industriales
### Seguridad
- Entornos peligrosos : Inspección remota en ambientes hostiles o tóxicos
- Prevención de accidentes : Detección de situaciones de riesgo en tiempo real
- Seguridad alimentaria : Identificación de contaminantes o cuerpos extraños
- Ciberseguridad : Sistemas de reconocimiento biométrico para acceso seguro
## Posicionamiento preciso
### Técnicas: detección de marcadores visuales con cámara y sensores en tiempo real Marcadores fiduciales
- Marcadores ArUco : Patrones binarios cuadrados para posicionamiento preciso
- AprilTags : Alta precisión incluso con cámaras de baja resolución
- QR y códigos de barras 2D : Para identificación y posicionamiento simultáneo
```
# Ejemplo de detección de marcadores ArUco con 
OpenCV
import cv2
import numpy as np
from cv2 import aruco

def detectar_marcadores(imagen):
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, 
cv2.COLOR_BGR2GRAY)
    
    # Definir el diccionario de marcadores
    diccionario = 
aruco.Dictionary_get(aruco.DICT_6X6_250)
    
    # Parámetros para la detección
    parametros = aruco.DetectorParameters_create()
    
    # Detectar marcadores
    esquinas, ids, rechazados = 
aruco.detectMarkers(gris, diccionario, 
parameters=parametros)
    
    # Dibujar marcadores detectados
    imagen_marcada = imagen.copy()
    if ids is not None:
        aruco.drawDetectedMarkers(imagen_marcada, 
esquinas, ids)
        
        # Calcular posición 3D (requiere 
calibración de cámara)
        for i, esquina in enumerate(esquinas):
            # Extraer las 4 esquinas del marcador
            c = esquina[0]
            # Calcular el centro del marcador
            centro_x = int(np.mean(c[:, 0]))
            centro_y = int(np.mean(c[:, 1]))
            cv2.circle(imagen_marcada, (centro_x, 
centro_y), 5, (0, 255, 0), -1)
            cv2.putText(imagen_marcada, f"ID: 
{ids[i][0]}", (centro_x, centro_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 
0.5, (0, 255, 0), 2)
    
    return imagen_marcada, esquinas, ids

# Uso (comentado para evitar errores de ejecución)
# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# imagen_resultado, esquinas, ids = 
detectar_marcadores(frame)
# cv2.imshow('Marcadores detectados', 
imagen_resultado)
``` Sistemas de posicionamiento visual
- Visual SLAM (Simultaneous Localization and Mapping) : Construcción de mapa y localización simultánea
- Structure from Motion : Reconstrucción 3D a partir de múltiples vistas 2D
- Visual-Inertial Odometry : Combinación de cámaras con sensores inerciales (IMU) Calibración y precisión
- Calibración de cámaras : Corrección de distorsiones para mediciones precisas
- Triangulación : Determinación de coordenadas 3D mediante múltiples cámaras
- Fusión sensorial : Combinación de datos visuales con otros sensores (láser, ultrasonido)
### Aplicaciones en robótica, logística y almacenamiento Robótica
- Navegación autónoma : Robots móviles que se desplazan usando referencias visuales
- Pick and place : Brazos robóticos que localizan y manipulan objetos con precisión
- Ensamblaje preciso : Posicionamiento exacto de componentes en fabricación Logística
- Seguimiento de inventario : Localización de productos mediante marcadores visuales
- Clasificación automática : Sistemas de ordenación basados en códigos visuales
- Carga/descarga autónoma : Vehículos guiados por visión (AGVs) Almacenamiento
- Gestión de almacenes : Optimización del espacio mediante mapeo visual
- Picking automatizado : Robots que seleccionan productos específicos
- Inventario en tiempo real : Monitorización continua de existencias
Caso de estudio: Sistema de almacenamiento automatizado

Un centro logístico implementó un sistema de visión artificial para la gestión de su almacén:

- 50 robots autónomos equipados con cámaras estéreo
- Marcadores ArUco en estanterías y zonas de tránsito
- Precisión de posicionamiento: ±5mm
- Resultados:
  - Reducción del 40% en tiempos de picking
  - Disminución del 60% en errores de inventario
  - Aumento del 25% en capacidad de almacenamiento
## Identificación de productos y personas
### Técnicas: reconocimiento de patrones y formas Reconocimiento basado en características
- Detección de bordes : Algoritmos Sobel, Canny para definir contornos
- Descriptores de forma : Momentos de Hu, descriptores de Fourier
- Características locales : SIFT, SURF, ORB para puntos de interés invariantes
```
# Ejemplo de extracción de características ORB y 
matching
import cv2
import numpy as np

def comparar_imagenes(img1, img2):
    # Inicializar el detector ORB
    orb = cv2.ORB_create(nfeatures=1000)
    
    # Encontrar keypoints y descriptores
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    
    # Crear matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, 
crossCheck=True)
    
    # Realizar matching
    matches = bf.match(des1, des2)
    
    # Ordenar por distancia
    matches = sorted(matches, key=lambda x: 
x.distance)
    
    # Dibujar los mejores matches
    img_matches = cv2.drawMatches(img1, kp1, img2, 
kp2, matches[:30], None, 
                                 
flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    # Calcular puntuación de similitud (menor 
distancia = mayor similitud)
    if len(matches) > 0:
        similitud = 1.0 - sum(m.distance for m in 
matches[:50]) / (50 * 100)
        similitud = max(0, min(1, similitud))  # 
Normalizar entre 0 y 1
    else:
        similitud = 0.0
        
    return img_matches, similitud

# Uso (comentado)
# img1 = cv2.imread('producto_referencia.jpg', 
cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread('producto_test.jpg', 
cv2.IMREAD_GRAYSCALE)
# img_resultado, similitud = 
comparar_imagenes(img1, img2)
# print(f"Similitud: {similitud:.2%}")
``` Técnicas basadas en aprendizaje profundo
- Redes neuronales convolucionales (CNN) : Clasificación de imágenes
- Siamese Networks : Comparación de similitud entre imágenes
- Detección de objetos : YOLO, SSD, Faster R-CNN para localización e identificación Reconocimiento óptico de caracteres (OCR)
- Lectura de códigos y texto : Identificación de números de serie, lotes, fechas
- Verificación de etiquetas : Comprobación de información impresa
- Documentación automática : Digitalización de información en papel
### Aplicaciones en reconocimiento facial y de huellas dactilares Reconocimiento facial
- Verificación de identidad : Comparación 1:1 para confirmar identidad
- Identificación : Búsqueda 1:N para determinar identidad entre múltiples personas
- Análisis de atributos : Estimación de edad, género, expresión
Proceso típico de reconocimiento facial:

1. Detección de rostro en la imagen
2. Alineación facial basada en puntos de referencia (ojos, nariz, boca)
3. Extracción de características mediante CNN
4. Comparación con base de datos de embeddings faciales
```
# Ejemplo conceptual de reconocimiento facial con 
dlib
import dlib
import cv2
import numpy as np
from scipy.spatial.distance import cosine

def reconocimiento_facial(imagen, 
base_datos_embeddings):
    # Detector de rostros y predictor de landmarks
    detector = dlib.get_frontal_face_detector()
    predictor = 
dlib.shape_predictor("shape_predictor_68_face_land
marks.dat")
    
    # Modelo de reconocimiento facial
    reconocedor = 
dlib.face_recognition_model_v1("dlib_face_recognit
ion_resnet_model_v1.dat")
    
    # Detectar rostros
    rostros = detector(imagen)
    resultados = []
    
    for rostro in rostros:
        # Obtener landmarks faciales
        landmarks = predictor(imagen, rostro)
        
        # Calcular embedding facial (vector de 128 
dimensiones)
        embedding = 
reconocedor.compute_face_descriptor(imagen, 
landmarks)
        embedding = np.array(embedding)
        
        # Buscar coincidencia en la base de datos
        mejor_coincidencia = None
        menor_distancia = 0.6  # Umbral de 
similitud (menor = más similar)
        
        for persona, emb_conocido in 
base_datos_embeddings.items():
            distancia = cosine(embedding, 
emb_conocido)  # Distancia del coseno
            if distancia < menor_distancia:
                menor_distancia = distancia
                mejor_coincidencia = persona
        
        # Dibujar resultado
        x1, y1, x2, y2 = rostro.left(), 
rostro.top(), rostro.right(), rostro.bottom()
        cv2.rectangle(imagen, (x1, y1), (x2, y2), 
(0, 255, 0), 2)
        
        if mejor_coincidencia:
            etiqueta = f"{mejor_coincidencia} ({1-
menor_distancia:.2%})"
        else:
            etiqueta = "Desconocido"
            
        cv2.putText(imagen, etiqueta, (x1, y1-10), 
cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        resultados.append((mejor_coincidencia, 1-
menor_distancia))
    
    return imagen, resultados
``` Reconocimiento de huellas dactilares
- Extracción de minucias : Identificación de puntos característicos (terminaciones, bifurcaciones)
- Matching de huellas : Algoritmos de comparación basados en patrones de minucias
- Clasificación : Agrupación por tipos (arco, lazo, espiral) Consideraciones éticas y de privacidad
- Consentimiento informado : Necesidad de autorización para recopilar datos biométricos
- Seguridad de datos : Protección de información sensible mediante cifrado
- Sesgos algorítmicos : Evaluación y mitigación de discriminación potencial
- Normativas : Cumplimiento de GDPR, CCPA y otras regulaciones de privacidad
## Verificación de calidad y cumplimiento de normas
### Técnicas: comparación con modelos de referencia y análisis de diferencias Inspección basada en modelos
- Golden sample : Comparación con una muestra perfecta de referencia
- CAD matching : Verificación contra modelos de diseño asistido por ordenador
- Análisis estadístico : Detección de anomalías basada en distribuciones normales
```
# Ejemplo de verificación de calidad mediante 
comparación de imágenes
import cv2
import numpy as np

def verificar_calidad(imagen_test, 
imagen_referencia, umbral=0.85):
    # Asegurar mismo tamaño
    imagen_test = cv2.resize(imagen_test, 
(imagen_referencia.shape[1], 
imagen_referencia.shape[0]))
    
    # Convertir a escala de grises
    gris_test = cv2.cvtColor(imagen_test, 
cv2.COLOR_BGR2GRAY)
    gris_ref = cv2.cvtColor(imagen_referencia, 
cv2.COLOR_BGR2GRAY)
    
    # Calcular diferencia absoluta
    diff = cv2.absdiff(gris_test, gris_ref)
    
    # Umbralizar para destacar diferencias 
significativas
    _, thresh = cv2.threshold(diff, 30, 255, 
cv2.THRESH_BINARY)
    
    # Aplicar operaciones morfológicas para 
reducir ruido
    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.morphologyEx(thresh, 
cv2.MORPH_OPEN, kernel)
    
    # Encontrar contornos de las diferencias
    contornos, _ = cv2.findContours(thresh, 
cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Dibujar contornos en la imagen original
    resultado = imagen_test.copy()
    cv2.drawContours(resultado, contornos, -1, (0, 
0, 255), 2)
    
    # Calcular porcentaje de similitud
    pixeles_diferentes = np.count_nonzero(thresh)
    total_pixeles = thresh.shape[0] * 
thresh.shape[1]
    similitud = 1.0 - (pixeles_diferentes / 
total_pixeles)
    
    # Determinar si pasa la verificación
    pasa_verificacion = similitud >= umbral
    
    # Añadir texto con resultado
    texto = f"PASA: {similitud:.2%}" if 
pasa_verificacion else f"FALLA: {similitud:.2%}"
    cv2.putText(resultado, texto, (10, 30), 
cv2.FONT_HERSHEY_SIMPLEX, 1, 
                (0, 255, 0) if pasa_verificacion 
else (0, 0, 255), 2)
    
    return resultado, pasa_verificacion, similitud
``` Técnicas avanzadas de inspección
- Segmentación semántica : Clasificación a nivel de píxel para identificar componentes
- Detección de anomalías : Modelos no supervisados para identificar patrones inusuales
- Análisis espectral : Inspección en rangos no visibles (infrarrojo, ultravioleta) Métricas de calidad
- Precisión y recall : Balance entre falsos positivos y falsos negativos
- Curvas ROC : Evaluación del rendimiento a diferentes umbrales
- Matrices de confusión : Análisis detallado de clasificaciones correctas e incorrectas
### Aplicaciones en control de producción y sistemas de seguridad Control de producción
- Inspección en línea : Verificación de productos durante la fabricación
- Control estadístico de procesos : Monitorización de tendencias y variaciones
- Trazabilidad : Seguimiento de productos a lo largo de la cadena de producción Sistemas de seguridad
- Verificación de documentos : Detección de falsificaciones en pasaportes, billetes
- Control de acceso : Autenticación mediante características biométricas
- Videovigilancia inteligente : Detección de comportamientos anómalos o sospechosos
Caso de estudio: Sistema de inspección de PCBs

Una empresa de electrónica implementó un sistema de visión artificial para la inspección de placas de circuito impreso:

- Cámaras de alta resolución (20MP) con iluminación especializada
- Inspección de soldaduras, componentes y posicionamiento
- Verificación contra diseños CAD
- Resultados:
  - Reducción del 95% en defectos no detectados
  - Aumento del 30% en velocidad de producción
  - ROI alcanzado en 8 meses
## Medición precisa
### Técnicas: fotogrametría, visión estéreo y sensores de profundidad Fotogrametría
- Principios : Reconstrucción de medidas a partir de fotografías
- Fotogrametría de corto alcance : Mediciones precisas en objetos cercanos
- Aerofotogrametría : Mediciones a partir de imágenes aéreas o satelitales Visión estéreo
- Principio de triangulación : Cálculo de profundidad mediante disparidad
- Calibración de sistemas estéreo : Determinación de parámetros intrínsecos y extrínsecos
- Mapas de disparidad : Representación visual de la profundidad de escena
```
# Ejemplo de cálculo de mapa de disparidad con 
OpenCV
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcular_mapa_disparidad(img_izquierda, 
img_derecha):
    # Convertir a escala de grises
    gris_izq = cv2.cvtColor(img_izquierda, 
cv2.COLOR_BGR2GRAY)
    gris_der = cv2.cvtColor(img_derecha, 
cv2.COLOR_BGR2GRAY)
    
    # Crear objeto StereoBM
    stereo = 
cv2.StereoBM_create(numDisparities=128, 
blockSize=15)
    
    # Calcular mapa de disparidad
    disparidad = stereo.compute(gris_izq, 
gris_der)
    
    # Normalizar para visualización
    disparidad_norm = cv2.normalize(disparidad, 
None, alpha=0, beta=255, 
                                  
norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    # Colorear mapa de disparidad
    disparidad_color = 
cv2.applyColorMap(disparidad_norm, 
cv2.COLORMAP_JET)
    
    return disparidad, disparidad_norm, 
disparidad_color

# Función para calcular distancia real a partir de 
disparidad
def disparidad_a_distancia(disparidad, f, B, 
escala=16.0):
    # f: distancia focal en píxeles
    # B: línea base (distancia entre cámaras) en 
metros
    # escala: factor de escala usado en el cálculo 
de disparidad
    
    # Evitar división por cero
    disparidad_ajustada = disparidad / escala
    mask = disparidad_ajustada > 0
    
    # Calcular distancia: Z = f*B/d
    distancia = np.zeros_like(disparidad, 
dtype=np.float32)
    distancia[mask] = f * B / 
disparidad_ajustada[mask]
    
    return distancia
``` Sensores de profundidad
- Time-of-Flight (ToF) : Medición basada en tiempo de vuelo de señales
- Luz estructurada : Proyección de patrones conocidos para calcular profundidad
- LiDAR : Escaneo láser para mediciones de alta precisión
### Aplicaciones en control de calidad, medición de movimiento y velocidad en vídeo Control de calidad dimensional
- Verificación de tolerancias : Comprobación de dimensiones críticas
- Inspección de ensamblajes : Verificación de ajustes y alineaciones
- Metrología 3D : Reconstrucción completa de superficies para análisis Análisis de movimiento
- Seguimiento de objetos : Medición de trayectorias y velocidades
- Análisis biomecánico : Estudio de movimientos humanos
- Vibrometría : Detección y cuantificación de vibraciones Medición de velocidad en vídeo
- Flujo óptico : Estimación de movimiento entre frames consecutivos
- Tracking multi-objeto : Seguimiento simultáneo de múltiples elementos
- Calibración espacio-temporal : Conversión de píxeles a unidades reales


```python
# Ejemplo de cálculo de flujo óptico con OpenCV
import cv2
import numpy as np

def calcular_flujo_optico(frame1, frame2):
    # Convertir a escala de grises
    gris1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gris2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # Calcular flujo óptico denso Farneback
    flujo = cv2.calcOpticalFlowFarneback(gris1, gris2, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    # Convertir a coordenadas polares
    mag, ang = cv2.cartToPolar(flujo[..., 0], flujo[..., 1])
    
    # Crear imagen HSV para visualización
    hsv = np.zeros_like(frame1)
    hsv[..., 0] = ang * 180 / np.pi / 2  # Matiz según dirección
    hsv[..., 1] = 255                     # Saturación máxima
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)  # Valor según magnitud
    
    # Convertir a BGR para visualización
    flujo_color = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return flujo, flujo_color, mag, ang

# Función para estimar velocidad de objetos
def estimar_velocidad(flujo, mascara_objeto, escala_pixel_metro, fps):
    # Extraer flujo solo en la región del objeto
    flujo_objeto = flujo[mascara_objeto > 0]
    
    # Calcular velocidad media en píxeles/frame
    if len(flujo_objeto) > 0:
        vel_x = np.mean(flujo_objeto[:, 0])
        vel_y = np.mean(flujo_objeto[:, 1])
        vel_magnitud = np.sqrt(vel_x**2 + vel_y**2)
        
        # Convertir a metros/segundo
        vel_metros_segundo = vel_magnitud * escala_pixel_metro * fps
        return vel_metros_segundo, (vel_x, vel_y)
    else:
        return 0, (0, 0)
```

Trae

Used 1 context

Voy a crear un archivo para el módulo 4 sobre sistemas de visión 3D artificial, basándome en el contenido proporcionado por el usuario. Necesito verificar primero si existe alguna estructura de carpeta para el módulo 4 y luego crear el archivo con el contenido estructurado.

visionado/modulo_04

# Creación de archivo para el Módulo 04
Voy a crear un archivo de apuntes completo para el Módulo 04 sobre sistemas de visión 3D artificial, siguiendo el formato de los otros módulos del proyecto.

```
# Módulo 04: Sistemas de Visión 3D Artificial

## Visión 3D vs. 2D: Diferencias Fundamentales y 
Ventajas del Análisis Tridimensional

### Diferencias fundamentales

| Característica | Visión 2D | Visión 3D |
|---------------|-----------|----------|
| Dimensiones | Trabaja con imágenes planas (X, Y) 
| Incorpora información de profundidad (X, Y, Z) |
| Información | Limitada a color, textura y formas 
bidimensionales | Incluye volumen, profundidad, 
posición espacial real |
| Oclusiones | Difícil manejo de objetos 
parcialmente ocultos | Mejor manejo de oclusiones 
parciales |
| Perspectiva | Distorsiones difíciles de 
compensar | Representación más fiel a la realidad 
física |

### Ventajas del análisis tridimensional

- **Mediciones precisas**: Capacidad para obtener 
dimensiones reales de objetos
- **Reconocimiento robusto**: Menor sensibilidad a 
cambios de iluminación y perspectiva
- **Interacción espacial**: Comprensión de 
relaciones espaciales entre objetos
- **Navegación**: Capacidad mejorada para sistemas 
autónomos (robots, vehículos)
- **Reconstrucción**: Posibilidad de crear modelos 
digitales precisos de objetos y entornos reales

## Captura de Datos 3D: Técnicas de Adquisición y 
Procesamiento

### Técnicas activas

- **Escáner láser (LiDAR)**
  - Principio: Medición del tiempo de vuelo de 
pulsos láser
  - Aplicaciones: Vehículos autónomos, 
cartografía, arquitectura
  - Ventajas: Alta precisión, largo alcance
  - Desventajas: Coste elevado, problemas con 
superficies reflectantes

- **Luz estructurada**
  - Principio: Proyección de patrones conocidos y 
análisis de deformaciones
  - Aplicaciones: Escáneres 3D de corto alcance, 
sistemas de control de calidad
  - Ventajas: Alta resolución, buena precisión a 
corta distancia
  - Desventajas: Limitado alcance, sensible a 
condiciones de iluminación

- **Time-of-Flight (ToF)**
  - Principio: Medición del tiempo que tarda la 
luz en rebotar en objetos
  - Aplicaciones: Cámaras de profundidad, sistemas 
de reconocimiento gestual
  - Ventajas: Captura en tiempo real, compacto
  - Desventajas: Menor resolución que otras 
técnicas

### Técnicas pasivas

- **Visión estéreo**
  - Principio: Triangulación basada en dos o más 
cámaras
  - Aplicaciones: Robótica, realidad aumentada
  - Ventajas: No requiere emisores, similar al 
sistema visual humano
  - Desventajas: Dificultades en superficies sin 
textura

- **Fotogrametría**
  - Principio: Reconstrucción 3D a partir de 
múltiples fotografías 2D
  - Aplicaciones: Modelado 3D, arqueología, 
topografía
  - Ventajas: Bajo coste, alta fidelidad de color 
y textura
  - Desventajas: Proceso computacionalmente 
intensivo

- **Structure from Motion (SfM)**
  - Principio: Reconstrucción 3D a partir de 
secuencias de imágenes en movimiento
  - Aplicaciones: Mapeo 3D, realidad virtual
  - Ventajas: Funciona con cámaras convencionales
  - Desventajas: Requiere suficiente movimiento y 
textura

### Procesamiento de datos 3D

- **Registro (Alignment)**
  - Alineación de múltiples capturas en un sistema 
de coordenadas común
  - Algoritmos: ICP (Iterative Closest Point), NDT 
(Normal Distributions Transform)

- **Filtrado y reducción de ruido**
  - Eliminación de outliers y suavizado de 
superficies
  - Técnicas: Filtros estadísticos, Moving Least 
Squares

- **Reconstrucción de superficies**
  - Conversión de nubes de puntos a mallas 
poligonales
  - Métodos: Triangulación de Delaunay, Poisson 
Surface Reconstruction

```python
# Ejemplo de procesamiento de nube de puntos con 
Open3D
import open3d as o3d
import numpy as np

# Cargar nube de puntos
pcd = o3d.io.read_point_cloud("ejemplo.pcd")

# Filtrado de outliers estadísticos
pcd_filtered, _ = 
pcd.remove_statistical_outlier(nb_neighbors=20, 
std_ratio=2.0)

# Estimación de normales (necesario para 
reconstrucción)
pcd_filtered.estimate_normals(search_param=o3d.geo
metry.KDTreeSearchParamHybrid(radius=0.1, 
max_nn=30))

# Reconstrucción de superficie usando Poisson
mesh, densities = 
o3d.geometry.TriangleMesh.create_from_point_cloud_
poisson(pcd_filtered, depth=9)

# Visualización
o3d.visualization.draw_geometries([mesh])
```
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
```
# Ejemplo simplificado de una CNN 3D con 
TensorFlow/Keras
import tensorflow as tf
from tensorflow.keras import layers

def create_3d_cnn_model(input_shape, num_classes):
    inputs = tf.keras.Input(input_shape)
    
    # Bloque convolucional 3D
    x = layers.Conv3D(32, kernel_size=3, 
activation="relu")(inputs)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)
    
    x = layers.Conv3D(64, kernel_size=3, 
activation="relu")(x)
    x = layers.MaxPool3D(pool_size=2)(x)
    x = layers.BatchNormalization()(x)
    
    # Clasificación
    x = layers.GlobalAveragePooling3D()(x)
    x = layers.Dense(128, activation="relu")(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, 
activation="softmax")(x)
    
    return tf.keras.Model(inputs, outputs)

# Crear modelo para volúmenes 3D de 64x64x64 con 1 
canal
model = create_3d_cnn_model((64, 64, 64, 1), 
num_classes=10)
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
```
# Ejemplo de procesamiento de nubes de puntos con 
PyTorch3D
import torch
from pytorch3d.structures import Pointclouds
from pytorch3d.ops import 
sample_points_from_meshes
from pytorch3d.loss import chamfer_distance

# Crear nubes de puntos sintéticas
points_a = torch.rand(1, 1000, 3)  # batch_size=1, 
1000 puntos, 3 coordenadas
points_b = torch.rand(1, 1000, 3)

# Crear estructuras de nubes de puntos
pcl_a = Pointclouds(points=points_a)
pcl_b = Pointclouds(points=points_b)

# Calcular distancia de Chamfer entre nubes de 
puntos
loss, _ = chamfer_distance(pcl_a.points_padded(), 
pcl_b.points_padded())
print(f"Distancia de Chamfer: {loss.item()}")
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
```
# Ejemplo simplificado de SLAM visual con Python
import cv2
import numpy as np
import g2o

# Clase simplificada para Visual SLAM
class SimpleVisualSLAM:
    def __init__(self):
        self.poses = []  # Historial de poses de 
cámara
        self.points_3d = []  # Puntos 3D del mapa
        self.optimizer = g2o.SparseOptimizer()
        # Configuración del optimizador...
        
    def process_frame(self, frame, depth):
        # Extraer características
        orb = cv2.ORB_create()
        keypoints, descriptors = 
orb.detectAndCompute(frame, None)
        
        if len(self.poses) > 0:
            # Hacer matching con frame anterior
            # Estimar movimiento
            # Actualizar pose
            # Triangular nuevos puntos 3D
            # Optimizar mapa (bundle adjustment)
            pass
        else:
            # Inicializar primera pose
            self.poses.append(np.eye(4))
        
        return self.poses[-1], self.points_3d

# Uso (pseudocódigo)
# slam = SimpleVisualSLAM()
# for frame, depth in camera.read_frames():
#     pose, map_points = slam.process_frame(frame, 
depth)
#     visualize(frame, pose, map_points)
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
```
// Ejemplo simplificado de AR.js para web
<!DOCTYPE html>
<html>
<head>
    <script 
src="https://aframe.io/releases/1.2.0/aframe.min.j
s"></script>
    <script src="https://raw.githack.com/AR-js-
org/AR.js/master/aframe/build/aframe-ar.js">
</script>
</head>
<body style="margin: 0; overflow: hidden;">
    <a-scene embedded arjs="sourceType: webcam; 
debugUIEnabled: false;">
        <!-- Definir un marcador -->
        <a-marker preset="hiro">
            <!-- Contenido 3D que aparecerá sobre 
el marcador -->
            <a-box position="0 0.5 0" 
material="color: red;"></a-box>
        </a-marker>
        
        <!-- Configuración de cámara -->
        <a-entity camera></a-entity>
    </a-scene>
</body>
</html>
```
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
```

He creado un archivo completo para el Módulo 04 
sobre sistemas de visión 3D artificial, siguiendo 
la estructura que indicaste. El archivo incluye:

1. Comparación detallada entre visión 2D y 3D
2. Técnicas de captura de datos 3D (activas y 
pasivas)
3. Representación y modelado 3D (CNNs 3D, Poisson, 
nubes de puntos)
4. Aplicaciones prácticas en medicina, videojuegos 
y robótica
5. Sección sobre realidad aumentada
6. Recursos adicionales para profundizar

Cada sección incluye ejemplos de código relevantes 
y explicaciones técnicas. El archivo se ha 
guardado como `apuntes_m4.md` en la carpeta 
`modulo_04`.
```

ksizorCode

Copy

Delete

vamos a por el módulo 5

crea apuntes para el archivo apuntes_m5.md basado en este temario:

## Módulo 05: Ventajas (95 horas)

- Importancia de esta tecnología: precisión, calidad, rentabilidad, sostenibilidad y seguridad.

- Posicionamiento preciso:

- Técnicas: detección de marcadores visuales con cámara y sensores en tiempo real.

- Aplicaciones en robótica, logística y almacenamiento.

- Identificación de productos y personas:

- Técnicas: reconocimiento de patrones y formas.

- Aplicaciones en reconocimiento facial y de huellas dactilares.

- Verificación de calidad y cumplimiento de normas:

- Técnicas: comparación con modelos de referencia y análisis de diferencias.

- Aplicaciones en control de producción y sistemas de seguridad.

- Medición precisa:

- Técnicas: fotogrametría, visión estéreo y sensores de profundidad.

- Aplicaciones en control de calidad, medición de movimiento y velocidad en vídeo.

- Detección de defectos en productos y personas:

- Técnicas: análisis de patrones y texturas.

- Aplicaciones en control de fabricación y detección de anomalías médicas.

- Soluciones de visión:

- Técnicas: cámaras y sensores especializados.

- Aplicaciones en dispositivos médicos y automatización de procesos.

Trae

Voy a crear contenido detallado para el archivo apuntes_m5.md basado en el temario proporcionado sobre las ventajas de la visión artificial. Primero verificaré si el archivo ya existe y su contenido actual.

modulo_05/apuntes_m5.md

# Módulo 05: Ventajas de la Visión Artificial
Voy a desarrollar el contenido para el archivo apuntes_m5.md basado en el temario proporcionado, expandiendo cada sección con información detallada, ejemplos prácticos y código relevante.

```
# Módulo 05: Ventajas de la Visión Artificial

## Importancia de esta tecnología: precisión, 
calidad, rentabilidad, sostenibilidad y seguridad

La visión artificial se ha convertido en una 
tecnología transformadora en múltiples sectores 
debido a sus numerosas ventajas:

### Precisión
- **Mediciones exactas**: Capacidad para realizar 
mediciones con precisión submilimétrica
- **Consistencia**: Resultados reproducibles sin 
la variabilidad del factor humano
- **Detección de detalles**: Identificación de 
características imperceptibles para el ojo humano

### Calidad
- **Inspección al 100%**: Posibilidad de examinar 
todos los productos, no solo muestras
- **Detección temprana**: Identificación de 
defectos en fases iniciales del proceso productivo
- **Trazabilidad**: Registro completo del proceso 
de inspección para auditorías

### Rentabilidad
- **Reducción de costes operativos**: Menor 
necesidad de personal para tareas repetitivas
- **Disminución de errores**: Menos rechazos y 
devoluciones por defectos no detectados
- **Mayor productividad**: Velocidad de inspección 
superior a la humana
- **ROI cuantificable**: Ejemplo de cálculo:

```python
# Ejemplo simplificado de cálculo de ROI para un 
sistema de visión artificial
def calcular_roi_vision_artificial(coste_sistema, 
ahorro_anual, vida_util):
    roi = (ahorro_anual * vida_util - 
coste_sistema) / coste_sistema * 100
    return roi

# Parámetros de ejemplo
coste_sistema = 50000  # Coste de implementación 
del sistema en €
ahorro_anual = 20000   # Ahorro anual en costes de 
personal, reducción de errores, etc.
vida_util = 5          # Vida útil estimada en 
años

roi = 
calcular_roi_vision_artificial(coste_sistema, 
ahorro_anual, vida_util)
print(f"ROI estimado: {roi:.2f}%")
# Resultado: ROI estimado: 100.00%
```
### Sostenibilidad
- Optimización de recursos : Menor desperdicio de materiales y energía
- Reducción de desechos : Detección temprana evita procesamiento innecesario
- Eficiencia energética : Sistemas modernos con bajo consumo energético
- Impacto ambiental : Reducción de la huella de carbono en procesos industriales
### Seguridad
- Entornos peligrosos : Inspección remota en ambientes hostiles o tóxicos
- Prevención de accidentes : Detección de situaciones de riesgo en tiempo real
- Seguridad alimentaria : Identificación de contaminantes o cuerpos extraños
- Ciberseguridad : Sistemas de reconocimiento biométrico para acceso seguro
## Posicionamiento preciso
### Técnicas: detección de marcadores visuales con cámara y sensores en tiempo real Marcadores fiduciales
- Marcadores ArUco : Patrones binarios cuadrados para posicionamiento preciso
- AprilTags : Alta precisión incluso con cámaras de baja resolución
- QR y códigos de barras 2D : Para identificación y posicionamiento simultáneo
```
# Ejemplo de detección de marcadores ArUco con 
OpenCV
import cv2
import numpy as np
from cv2 import aruco

def detectar_marcadores(imagen):
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, 
cv2.COLOR_BGR2GRAY)
    
    # Definir el diccionario de marcadores
    diccionario = 
aruco.Dictionary_get(aruco.DICT_6X6_250)
    
    # Parámetros para la detección
    parametros = aruco.DetectorParameters_create()
    
    # Detectar marcadores
    esquinas, ids, rechazados = 
aruco.detectMarkers(gris, diccionario, 
parameters=parametros)
    
    # Dibujar marcadores detectados
    imagen_marcada = imagen.copy()
    if ids is not None:
        aruco.drawDetectedMarkers(imagen_marcada, 
esquinas, ids)
        
        # Calcular posición 3D (requiere 
calibración de cámara)
        for i, esquina in enumerate(esquinas):
            # Extraer las 4 esquinas del marcador
            c = esquina[0]
            # Calcular el centro del marcador
            centro_x = int(np.mean(c[:, 0]))
            centro_y = int(np.mean(c[:, 1]))
            cv2.circle(imagen_marcada, (centro_x, 
centro_y), 5, (0, 255, 0), -1)
            cv2.putText(imagen_marcada, f"ID: 
{ids[i][0]}", (centro_x, centro_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 
0.5, (0, 255, 0), 2)
    
    return imagen_marcada, esquinas, ids

# Uso (comentado para evitar errores de ejecución)
# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# imagen_resultado, esquinas, ids = 
detectar_marcadores(frame)
# cv2.imshow('Marcadores detectados', 
imagen_resultado)
``` Sistemas de posicionamiento visual
- Visual SLAM (Simultaneous Localization and Mapping) : Construcción de mapa y localización simultánea
- Structure from Motion : Reconstrucción 3D a partir de múltiples vistas 2D
- Visual-Inertial Odometry : Combinación de cámaras con sensores inerciales (IMU) Calibración y precisión
- Calibración de cámaras : Corrección de distorsiones para mediciones precisas
- Triangulación : Determinación de coordenadas 3D mediante múltiples cámaras
- Fusión sensorial : Combinación de datos visuales con otros sensores (láser, ultrasonido)
### Aplicaciones en robótica, logística y almacenamiento Robótica
- Navegación autónoma : Robots móviles que se desplazan usando referencias visuales
- Pick and place : Brazos robóticos que localizan y manipulan objetos con precisión
- Ensamblaje preciso : Posicionamiento exacto de componentes en fabricación Logística
- Seguimiento de inventario : Localización de productos mediante marcadores visuales
- Clasificación automática : Sistemas de ordenación basados en códigos visuales
- Carga/descarga autónoma : Vehículos guiados por visión (AGVs) Almacenamiento
- Gestión de almacenes : Optimización del espacio mediante mapeo visual
- Picking automatizado : Robots que seleccionan productos específicos
- Inventario en tiempo real : Monitorización continua de existencias
Caso de estudio: Sistema de almacenamiento automatizado

Un centro logístico implementó un sistema de visión artificial para la gestión de su almacén:

- 50 robots autónomos equipados con cámaras estéreo
- Marcadores ArUco en estanterías y zonas de tránsito
- Precisión de posicionamiento: ±5mm
- Resultados:
  - Reducción del 40% en tiempos de picking
  - Disminución del 60% en errores de inventario
  - Aumento del 25% en capacidad de almacenamiento
## Identificación de productos y personas
### Técnicas: reconocimiento de patrones y formas Reconocimiento basado en características
- Detección de bordes : Algoritmos Sobel, Canny para definir contornos
- Descriptores de forma : Momentos de Hu, descriptores de Fourier
- Características locales : SIFT, SURF, ORB para puntos de interés invariantes
```
# Ejemplo de extracción de características ORB y 
matching
import cv2
import numpy as np

def comparar_imagenes(img1, img2):
    # Inicializar el detector ORB
    orb = cv2.ORB_create(nfeatures=1000)
    
    # Encontrar keypoints y descriptores
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    
    # Crear matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, 
crossCheck=True)
    
    # Realizar matching
    matches = bf.match(des1, des2)
    
    # Ordenar por distancia
    matches = sorted(matches, key=lambda x: 
x.distance)
    
    # Dibujar los mejores matches
    img_matches = cv2.drawMatches(img1, kp1, img2, 
kp2, matches[:30], None, 
                                 
flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    # Calcular puntuación de similitud (menor 
distancia = mayor similitud)
    if len(matches) > 0:
        similitud = 1.0 - sum(m.distance for m in 
matches[:50]) / (50 * 100)
        similitud = max(0, min(1, similitud))  # 
Normalizar entre 0 y 1
    else:
        similitud = 0.0
        
    return img_matches, similitud

# Uso (comentado)
# img1 = cv2.imread('producto_referencia.jpg', 
cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread('producto_test.jpg', 
cv2.IMREAD_GRAYSCALE)
# img_resultado, similitud = 
comparar_imagenes(img1, img2)
# print(f"Similitud: {similitud:.2%}")
``` Técnicas basadas en aprendizaje profundo
- Redes neuronales convolucionales (CNN) : Clasificación de imágenes
- Siamese Networks : Comparación de similitud entre imágenes
- Detección de objetos : YOLO, SSD, Faster R-CNN para localización e identificación Reconocimiento óptico de caracteres (OCR)
- Lectura de códigos y texto : Identificación de números de serie, lotes, fechas
- Verificación de etiquetas : Comprobación de información impresa
- Documentación automática : Digitalización de información en papel
### Aplicaciones en reconocimiento facial y de huellas dactilares Reconocimiento facial
- Verificación de identidad : Comparación 1:1 para confirmar identidad
- Identificación : Búsqueda 1:N para determinar identidad entre múltiples personas
- Análisis de atributos : Estimación de edad, género, expresión
Proceso típico de reconocimiento facial:

1. Detección de rostro en la imagen
2. Alineación facial basada en puntos de referencia (ojos, nariz, boca)
3. Extracción de características mediante CNN
4. Comparación con base de datos de embeddings faciales
```
# Ejemplo conceptual de reconocimiento facial con 
dlib
import dlib
import cv2
import numpy as np
from scipy.spatial.distance import cosine

def reconocimiento_facial(imagen, 
base_datos_embeddings):
    # Detector de rostros y predictor de landmarks
    detector = dlib.get_frontal_face_detector()
    predictor = 
dlib.shape_predictor("shape_predictor_68_face_land
marks.dat")
    
    # Modelo de reconocimiento facial
    reconocedor = 
dlib.face_recognition_model_v1("dlib_face_recognit
ion_resnet_model_v1.dat")
    
    # Detectar rostros
    rostros = detector(imagen)
    resultados = []
    
    for rostro in rostros:
        # Obtener landmarks faciales
        landmarks = predictor(imagen, rostro)
        
        # Calcular embedding facial (vector de 128 
dimensiones)
        embedding = 
reconocedor.compute_face_descriptor(imagen, 
landmarks)
        embedding = np.array(embedding)
        
        # Buscar coincidencia en la base de datos
        mejor_coincidencia = None
        menor_distancia = 0.6  # Umbral de 
similitud (menor = más similar)
        
        for persona, emb_conocido in 
base_datos_embeddings.items():
            distancia = cosine(embedding, 
emb_conocido)  # Distancia del coseno
            if distancia < menor_distancia:
                menor_distancia = distancia
                mejor_coincidencia = persona
        
        # Dibujar resultado
        x1, y1, x2, y2 = rostro.left(), 
rostro.top(), rostro.right(), rostro.bottom()
        cv2.rectangle(imagen, (x1, y1), (x2, y2), 
(0, 255, 0), 2)
        
        if mejor_coincidencia:
            etiqueta = f"{mejor_coincidencia} ({1-
menor_distancia:.2%})"
        else:
            etiqueta = "Desconocido"
            
        cv2.putText(imagen, etiqueta, (x1, y1-10), 
cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        resultados.append((mejor_coincidencia, 1-
menor_distancia))
    
    return imagen, resultados
``` Reconocimiento de huellas dactilares
- Extracción de minucias : Identificación de puntos característicos (terminaciones, bifurcaciones)
- Matching de huellas : Algoritmos de comparación basados en patrones de minucias
- Clasificación : Agrupación por tipos (arco, lazo, espiral) Consideraciones éticas y de privacidad
- Consentimiento informado : Necesidad de autorización para recopilar datos biométricos
- Seguridad de datos : Protección de información sensible mediante cifrado
- Sesgos algorítmicos : Evaluación y mitigación de discriminación potencial
- Normativas : Cumplimiento de GDPR, CCPA y otras regulaciones de privacidad
## Verificación de calidad y cumplimiento de normas
### Técnicas: comparación con modelos de referencia y análisis de diferencias Inspección basada en modelos
- Golden sample : Comparación con una muestra perfecta de referencia
- CAD matching : Verificación contra modelos de diseño asistido por ordenador
- Análisis estadístico : Detección de anomalías basada en distribuciones normales
```
# Ejemplo de verificación de calidad mediante 
comparación de imágenes
import cv2
import numpy as np

def verificar_calidad(imagen_test, 
imagen_referencia, umbral=0.85):
    # Asegurar mismo tamaño
    imagen_test = cv2.resize(imagen_test, 
(imagen_referencia.shape[1], 
imagen_referencia.shape[0]))
    
    # Convertir a escala de grises
    gris_test = cv2.cvtColor(imagen_test, 
cv2.COLOR_BGR2GRAY)
    gris_ref = cv2.cvtColor(imagen_referencia, 
cv2.COLOR_BGR2GRAY)
    
    # Calcular diferencia absoluta
    diff = cv2.absdiff(gris_test, gris_ref)
    
    # Umbralizar para destacar diferencias 
significativas
    _, thresh = cv2.threshold(diff, 30, 255, 
cv2.THRESH_BINARY)
    
    # Aplicar operaciones morfológicas para 
reducir ruido
    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.morphologyEx(thresh, 
cv2.MORPH_OPEN, kernel)
    
    # Encontrar contornos de las diferencias
    contornos, _ = cv2.findContours(thresh, 
cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Dibujar contornos en la imagen original
    resultado = imagen_test.copy()
    cv2.drawContours(resultado, contornos, -1, (0, 
0, 255), 2)
    
    # Calcular porcentaje de similitud
    pixeles_diferentes = np.count_nonzero(thresh)
    total_pixeles = thresh.shape[0] * 
thresh.shape[1]
    similitud = 1.0 - (pixeles_diferentes / 
total_pixeles)
    
    # Determinar si pasa la verificación
    pasa_verificacion = similitud >= umbral
    
    # Añadir texto con resultado
    texto = f"PASA: {similitud:.2%}" if 
pasa_verificacion else f"FALLA: {similitud:.2%}"
    cv2.putText(resultado, texto, (10, 30), 
cv2.FONT_HERSHEY_SIMPLEX, 1, 
                (0, 255, 0) if pasa_verificacion 
else (0, 0, 255), 2)
    
    return resultado, pasa_verificacion, similitud
``` Técnicas avanzadas de inspección
- Segmentación semántica : Clasificación a nivel de píxel para identificar componentes
- Detección de anomalías : Modelos no supervisados para identificar patrones inusuales
- Análisis espectral : Inspección en rangos no visibles (infrarrojo, ultravioleta) Métricas de calidad
- Precisión y recall : Balance entre falsos positivos y falsos negativos
- Curvas ROC : Evaluación del rendimiento a diferentes umbrales
- Matrices de confusión : Análisis detallado de clasificaciones correctas e incorrectas
### Aplicaciones en control de producción y sistemas de seguridad Control de producción
- Inspección en línea : Verificación de productos durante la fabricación
- Control estadístico de procesos : Monitorización de tendencias y variaciones
- Trazabilidad : Seguimiento de productos a lo largo de la cadena de producción Sistemas de seguridad
- Verificación de documentos : Detección de falsificaciones en pasaportes, billetes
- Control de acceso : Autenticación mediante características biométricas
- Videovigilancia inteligente : Detección de comportamientos anómalos o sospechosos
Caso de estudio: Sistema de inspección de PCBs

Una empresa de electrónica implementó un sistema de visión artificial para la inspección de placas de circuito impreso:

- Cámaras de alta resolución (20MP) con iluminación especializada
- Inspección de soldaduras, componentes y posicionamiento
- Verificación contra diseños CAD
- Resultados:
  - Reducción del 95% en defectos no detectados
  - Aumento del 30% en velocidad de producción
  - ROI alcanzado en 8 meses
## Medición precisa
### Técnicas: fotogrametría, visión estéreo y sensores de profundidad Fotogrametría
- Principios : Reconstrucción de medidas a partir de fotografías
- Fotogrametría de corto alcance : Mediciones precisas en objetos cercanos
- Aerofotogrametría : Mediciones a partir de imágenes aéreas o satelitales Visión estéreo
- Principio de triangulación : Cálculo de profundidad mediante disparidad
- Calibración de sistemas estéreo : Determinación de parámetros intrínsecos y extrínsecos
- Mapas de disparidad : Representación visual de la profundidad de escena
```
# Ejemplo de cálculo de mapa de disparidad con 
OpenCV
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcular_mapa_disparidad(img_izquierda, 
img_derecha):
    # Convertir a escala de grises
    gris_izq = cv2.cvtColor(img_izquierda, 
cv2.COLOR_BGR2GRAY)
    gris_der = cv2.cvtColor(img_derecha, 
cv2.COLOR_BGR2GRAY)
    
    # Crear objeto StereoBM
    stereo = 
cv2.StereoBM_create(numDisparities=128, 
blockSize=15)
    
    # Calcular mapa de disparidad
    disparidad = stereo.compute(gris_izq, 
gris_der)
    
    # Normalizar para visualización
    disparidad_norm = cv2.normalize(disparidad, 
None, alpha=0, beta=255, 
                                  
norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    
    # Colorear mapa de disparidad
    disparidad_color = 
cv2.applyColorMap(disparidad_norm, 
cv2.COLORMAP_JET)
    
    return disparidad, disparidad_norm, 
disparidad_color

# Función para calcular distancia real a partir de 
disparidad
def disparidad_a_distancia(disparidad, f, B, 
escala=16.0):
    # f: distancia focal en píxeles
    # B: línea base (distancia entre cámaras) en 
metros
    # escala: factor de escala usado en el cálculo 
de disparidad
    
    # Evitar división por cero
    disparidad_ajustada = disparidad / escala
    mask = disparidad_ajustada > 0
    
    # Calcular distancia: Z = f*B/d
    distancia = np.zeros_like(disparidad, 
dtype=np.float32)
    distancia[mask] = f * B / 
disparidad_ajustada[mask]
    
    return distancia
 Sensores de profundidad
- Time-of-Flight (ToF) : Medición basada en tiempo de vuelo de señales
- Luz estructurada : Proyección de patrones conocidos para calcular profundidad
- LiDAR : Escaneo láser para mediciones de alta precisión
### Aplicaciones en control de calidad, medición de movimiento y velocidad en vídeo Control de calidad dimensional
- Verificación de tolerancias : Comprobación de dimensiones críticas
- Inspección de ensamblajes : Verificación de ajustes y alineaciones
- Metrología 3D : Reconstrucción completa de superficies para análisis Análisis de movimiento
- Seguimiento de objetos : Medición de trayectorias y velocidades
- Análisis biomecánico : Estudio de movimientos humanos
- Vibrometría : Detección y cuantificación de vibraciones Medición de velocidad en vídeo
- Flujo óptico : Estimación de movimiento entre frames consecutivos
- Tracking multi-objeto : Seguimiento simultáneo de múltiples elementos
- Calibración espacio-temporal : Conversión de píxeles a unidades reales

```python
# Ejemplo de cálculo de flujo óptico con OpenCV
import cv2
import numpy as np

def calcular_flujo_optico(frame1, frame2):
    # Convertir a escala de grises
    gris1 = cv2.cvtColor(frame1, 
cv2.COLOR_BGR2GRAY)
    gris2 = cv2.cvtColor(frame2, 
cv2.COLOR_BGR2GRAY)
    
    # Calcular flujo óptico denso Farneback
    flujo = cv2.calcOpticalFlowFarneback(gris1, 
gris2, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    
    # Convertir a coordenadas polares
    mag, ang = cv2.cartToPolar(flujo[..., 0], 
flujo[..., 1])
    
    # Crear imagen HSV para visualización
    hsv = np.zeros_like(frame1)
    hsv[..., 0] = ang * 180 / np.pi / 2  # Matiz 
según dirección
    hsv[..., 1] = 255                     # 
Saturación máxima
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, 
cv2.NORM_MINMAX)  # Valor según magnitud
    
    # Convertir a BGR para visualización
    flujo_color = cv2.cvtColor(hsv, 
cv2.COLOR_HSV2BGR)
    
    return flujo, flujo_color, mag, ang

# Función para estimar velocidad de objetos
def estimar_velocidad(flujo, mascara_objeto, 
escala_pixel_metro, fps):
    # Extraer flujo solo en la región del objeto
    flujo_objeto = flujo[mascara_objeto > 0]
    
    # Calcular velocidad media en píxeles/frame
    if len(flujo_objeto) > 0:
        vel_x = np.mean(flujo_objeto[:, 0])
        vel_y = np.mean(flujo_objeto[:, 1])
        vel_magnitud = np.sqrt(vel_x**2 + 
vel_y**2)
        
        # Convertir a metros/segundo
        vel_metros_segundo = vel_magnitud * 
escala_pixel_metro * fps
        return vel_metros_segundo, (vel_x, vel_y)
    else:
        return 0, (0, 0)
```

Caso de estudio: Sistema de medición en industria automotriz

Un fabricante de componentes automotrices implementó un sistema de visión para medición precisa:

- Cámaras estéreo calibradas con precisión submilimétrica
- Iluminación estructurada para mejorar la reconstrucción 3D
- Medición automática de más de 50 características críticas por pieza
- Resultados:
  - Precisión de ±0.05mm en mediciones críticas
  - Tiempo de inspección reducido de 15 minutos a 30 segundos por pieza
  - Trazabilidad completa con registro de todas las mediciones
## Detección de defectos en productos y personas
### Técnicas: análisis de patrones y texturas Análisis de texturas
- Descriptores estadísticos : Matrices de co-ocurrencia, LBP (Local Binary Patterns)
- Análisis frecuencial : Transformadas de Fourier, Wavelets
- Filtros de Gabor : Detección de orientaciones y frecuencias específicas


        



        ### Aplicaciones en dispositivos médicos y automatización de procesos Dispositivos médicos
- Endoscopios inteligentes : Detección automática de anomalías
- Microscopios automatizados : Análisis de muestras sin intervención humana
- Sistemas de cirugía asistida : Guía visual para procedimientos quirúrgicos Automatización de procesos
- Control de calidad en línea : Inspección 100% en tiempo real
- Guiado de robots : Posicionamiento preciso para manipulación
- Clasificación automática : Separación de productos por características visuales
```
# Ejemplo de sistema de clasificación automática 
con deep learning
import tensorflow as tf
from tensorflow.keras.applications import 
MobileNetV2
from tensorflow.keras.layers import 
GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model

def crear_modelo_clasificacion(num_clases):
    # Cargar modelo base preentrenado
    base_model = MobileNetV2(weights='imagenet', 
include_top=False, input_shape=(224, 224, 3))
    
    # Congelar capas del modelo base
    for layer in base_model.layers:
        layer.trainable = False
    
    # Añadir capas de clasificación
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(128, activation='relu')(x)
    predicciones = Dense(num_clases, 
activation='softmax')(x)
    
    # Crear modelo final
    modelo = Model(inputs=base_model.input, 
outputs=predicciones)
    
    # Compilar
    modelo.compile(
        
optimizer=tf.keras.optimizers.Adam(learning_rate=0
.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return modelo

# Función para procesar imagen y clasificar
def clasificar_producto(modelo, imagen, 
etiquetas):
    # Preprocesar imagen
    img = cv2.resize(imagen, (224, 224))
    img = img / 127.5 - 1.0  # Normalización para 
MobileNet
    img = np.expand_dims(img, axis=0)
    
    # Realizar predicción
    prediccion = modelo.predict(img)
    clase_id = np.argmax(prediccion[0])
    confianza = prediccion[0][clase_id]
    
    # Obtener etiqueta
    etiqueta = etiquetas[clase_id]
    
    return etiqueta, confianza, prediccion[0]
``` Integración de sistemas
- Comunicación industrial : Protocolos para interacción con PLCs, SCADA
- Edge computing : Procesamiento local para respuesta en tiempo real
- Sistemas MES/ERP : Integración con gestión de producción y recursos
Caso de estudio: Automatización en industria farmacéutica

Un fabricante farmacéutico implementó un sistema integral de visión artificial:

- Inspección de blísteres, viales y etiquetas
- Verificación de códigos, fechas y lotes
- Control de presencia y posición de medicamentos
- Resultados:
  - Cumplimiento 100% de normativas GMP
  - Trazabilidad completa de cada unidad producida
  - Cero recalls por problemas de calidad en 3 años
## Conclusiones y futuro de la visión artificial
### Tendencias emergentes
- Edge AI : Procesamiento en dispositivo para aplicaciones en tiempo real
- Visión + IA generativa : Creación y modificación de imágenes para entrenamiento
- Sistemas multimodales : Combinación de visión con lenguaje natural y otros sensores
- Aprendizaje continuo : Sistemas que mejoran constantemente con nuevos datos
### Desafíos actuales
- Interpretabilidad : Comprensión de decisiones tomadas por modelos complejos
- Datos sintéticos : Generación de datos de entrenamiento realistas
- Eficiencia energética : Reducción del consumo para aplicaciones móviles y embebidas
- Robustez : Funcionamiento fiable en condiciones variables y adversas
### Impacto futuro
- Democratización : Herramientas accesibles para empresas de todos los tamaños
- Personalización masiva : Producción flexible adaptada a necesidades individuales
- Sostenibilidad : Optimización de recursos y reducción de desperdicios
- Nuevos modelos de negocio : Servicios basados en análisis visual de datos
## Recursos adicionales
### Bibliotecas y frameworks
- OpenCV: https://opencv.org/
- TensorFlow: https://www.tensorflow.org/
- PyTorch: https://pytorch.org/
- scikit-image: https://scikit-image.org/
### Datasets públicos
- COCO: https://cocodataset.org/
- ImageNet: https://www.image-net.org/
- MVTec AD: https://www.mvtec.com/company/research/datasets/mvtec-ad
### Comunidades y recursos de aprendizaje
- PyImageSearch: https://pyimagesearch.com/
- Computer Vision News: https://www.rsipvision.com/computer-vision-news/
- Papers With Code: https://paperswithcode.com/task/computer-vision