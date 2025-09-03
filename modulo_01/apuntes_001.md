# Apuntes Introductorios de Visión por Ordenador
---

## 1. Introducción a la Inteligencia Artificial  

> **Ejemplo cinematográfico**: En *2001: Una odisea del espacio*, HAL 9000 representa una IA “general” capaz de razonar y tomar decisiones complejas. Sin embargo, hoy en día, la mayoría de sistemas de IA son “narrow” (estrechos), especializados en tareas concretas.

### 1.1 ¿Qué es la Inteligencia Artificial?  
- **Definición básica**: Rama de la informática dedicada a crear sistemas que imitan funciones cognitivas humanas como aprender, razonar, planificar y resolver problemas.  
- **Objetivo práctico**: Automatizar tareas que requieren “inteligencia” (diagnóstico médico, reconocimiento de voz, recomendación de contenidos, etc.).  

### 1.2 Tipos de Inteligencia Artificial  
1. **IA Débil (Narrow AI)**  
   - Diseñada para UNA tarea específica (por ejemplo, Siri o Alexa).  
   - No “entiende” ni razona fuera de su dominio. 
   - Ejemplo: 

2. **IA Fuerte (General AI / AGI)**  
   - Persigue replicar la inteligencia humana en toda su amplitud.  
   - Capaz de aprender, comprender y aplicar conocimientos en múltiples dominios.  
   - **¡Aún no existe en la práctica!**  

3. **IA Súper (Superintelligence)**  
   - Hipotética. Inteligencia que supera a la humana en todas las tareas cognitivas.  
   - Tema recurrente en la cultura friky (por ejemplo, Skynet en *Terminator*).  

---

## 2. Aprendizaje Automático (Machine Learning)  

> **Ejemplo videojuego**: En *FIFA*, el comportamiento de los jugadores “aprende” a base de datos gigantes de partidos. No es magia: son algoritmos que identifican patrones en las jugadas.

### 2.1 ¿Qué es el Machine Learning (ML)?  
- Subcampo de la IA que construye sistemas capaces de **aprender** de datos sin ser explícitamente programados para cada situación.  
- **Idea clave**: Alimentar al modelo con ejemplos (datos de entrenamiento) y dejar que extraiga patrones.

### 2.2 Componentes Básicos de un Problema de ML  
1. **Datos de entrada (features)**: Variables que describen cada caso (e.g., píxeles de una imagen, características de audio).  
2. **Etiqueta o target**: Lo que queremos predecir (e.g., “gato” vs “perro”, precio de una casa).  
3. **Modelo**: Conjunto de parámetros que relacionan entradas y salidas (por ejemplo, los coeficientes de una regresión).  
4. **Función de pérdida (loss)**: Mide cuán lejos está la predicción del valor real.  
5. **Algoritmo de optimización**: Ajusta los parámetros minimizando la función de pérdida (e.g., gradiente descendente).

### 2.3 Tipos de Aprendizaje Automático  
1. **Aprendizaje Supervisado**  
   - Datos etiquetados: cada ejemplo incluye la respuesta correcta.  
   - **Tareas**:  
     - **Regresión**: Predecir valores continuos (p. ej., precio de la vivienda, temperatura).  
     - **Clasificación**: Asignar etiquetas discretas (p. ej., gato vs perro).  
   - **Modelos comunes**:  
     - Regresión Lineal / Logística  
     - Support Vector Machines (SVM)  
     - Árboles de Decisión y Random Forest  
     - K-Nearest Neighbors (KNN)  

2. **Aprendizaje No Supervisado**  
   - Datos sin etiquetas. El objetivo es **descubrir estructuras** ocultas.  
   - **Tareas**:  
     - **Clustering (agrupamiento)**: k-means, DBSCAN (ejemplo: agrupar píxeles similares en una imagen).  
     - **Reducción de dimensionalidad**: PCA, t-SNE (útil para visualización de datos complejos).  
   - **Ejemplo friki**: En *Matrix*, los “agentes” podrían representar clusters de píxeles que definen a Neo; cada vez que Neo aparece, los píxeles se agrupan en torno a él.  

3. **Aprendizaje por Refuerzo**  
   - Agente aprende a tomar decisiones interactuando con un entorno y recibiendo **recompensas** o **penalizaciones**.  
   - En visión por ordenador, se usa menos frecuentemente, pero puede aplicarse para tareas como **robot vision** donde un robot ajusta su cámara para mejorar la percepción.

---

## 3. Deep Learning  

> **Ejemplo cine**: En *Ex Machina*, la IA Ava utiliza redes neuronales (hipotéticas) para interpretar lenguaje y reconocer rostros en tiempo real. Nuestras CNN actuales son un “primo lejano” de esa idea.

### 3.1 ¿Qué es Deep Learning (DL)?  
- Subcampo del ML basado en **Redes Neuronales Artificiales** (ANN) profundas (múltiples capas ocultas).  
- **Inspirado en la estructura del cerebro**, aunque con simplificaciones enormes.  
- Especialmente poderoso en tareas de visión, audio y lenguaje natural.

### 3.2 Redes Neuronales Convolucionales (CNN)  
#### 3.2.1 Concepto y Estructura  
- Diseñadas para procesar datos con **estructura de cuadrícula** (por ejemplo, imágenes).  
- Componentes básicos:  
  1. **Capas Convolucionales**: Filtros (kernels) que “deslizan” sobre la imagen para detectar **patrones locales** (bordes, texturas).  
  2. **Operación de Pooling**: Reduce la resolución espacial (downsampling), capturando información relevante con menos datos (max-pooling, average-pooling).  
  3. **Capas Completamente Conectadas (fully connected)**: Al final de la red, para combinar características extraídas y producir una predicción global.  

#### 3.2.2 Características de las CNN  
- **Invariancia a Traslaciones**: Un filtro que detecta un borde horizontal lo hará en cualquier parte de la imagen.  
- **Parámetros Compartidos**: Un mismo kernel se aplica en toda la imagen, lo que reduce drásticamente la cantidad de parámetros.  
- **Jerarquía de Características**:  
  - Capas bajas → detectan bordes y texturas simples (e.g., detectores de bordes como Sobel).  
  - Capas intermedias → detectan formas (ojos, ruedas, ventanas).  
  - Capas altas → detectan objetos completos (caras, coches, señales de tráfico).

#### 3.2.3 ¿Cómo Trabaja una CNN en Visión por Ordenador?  
1. **Entrada**: Una imagen (por ejemplo, un fotograma de *Blade Runner*).  
2. **Convolución + ReLU**: Filtrar la imagen con múltiples kernels, aplicando una función de activación (ReLU) para introducir no linealidad.  
3. **Pooling**: Reducir la dimensión espacial (e.g., pasar de 256×256 a 128×128).  
4. **Repetir**: Varias capas de convolución + pooling van extrayendo características cada vez más complejas.  
5. **Capas Fully Connected**: Finalmente, todas las características se “aplanan” y se procesan para clasificar (o para alguna otra tarea, como regresión de bounding boxes).  

> **Analogía cinematográfica**: Imagina que cada fotograma de *The Matrix* es pasado por “filtros mágicos” que, capa a capa, descubren si ese fotograma corresponde a un agente, a Neo o a un obstáculo.  

---

## 4. Tipos de Inteligencia Artificial Según su Capacitación (otra clasificación)  

1. **Sistemas Basados en Reglas (Expert Systems)**  
   - IA clásica: “Si-entonces” → e.g., sistemas de diagnóstico médicos antiguos.  
   - Limitados al conocimiento incluido manualmente.  

2. **IA Estadística (Data-Driven)**  
   - Incluye ML y DL.  
   - Aprende de datos masivos, no de reglas explícitas.  

3. **IA Híbrida**  
   - Combinación de enfoques simbólicos (reglas) y subsimbólicos (redes neuronales).  
   - En visión por ordenador, a veces se integran módulos de inferencia lógica con CNN para razonamiento.

---

## 5. Visión por Ordenador (Computer Vision)  

> **Ejemplo friki**: En *Minority Report*, la policía analiza imágenes en tiempo real para predecir crímenes. Si bien la “precrimen” es ficción, las técnicas de tracking y detección existen desde hace años.

### 5.1 ¿Qué es la Visión por Ordenador?  
- Disciplina que **permite a las máquinas ‘ver’** y extraer información de imágenes o secuencias de video.  
- Objetivos principales:  
  1. **Reconocer** qué hay en la imagen (clasificación).  
  2. **Localizar** objetos (detección).  
  3. **Segmentar** regiones (pixel a pixel).  
  4. **Seguir** movimientos en video (tracking).  
  5. **Reconstruir** escenas en 3D.

### 5.2 Algoritmos Clásicos vs. Deep Learning  
- **Enfoques Clásicos (antes de las CNN)**:  
  - Detección de bordes (Canny), esquinas (Harris), descriptores (SIFT, SURF).  
  - Segmentación basada en umbrales (Otsu), clustering (k-means).  
  - Tracking con KLT (Lucas-Kanade).  
- **Enfoques Modernos (Deep Learning)**:  
  - Modelos CNN para clasificación, detección (R-CNN, SSD, YOLO), segmentación (U-Net, Mask R-CNN).  
  - Tracking basado en DeepSORT, Track R-CNN.  

---

## 6. Algoritmos Clave en Visión por Ordenador  

### 6.1 Convolutional Neural Networks (CNN)  
- Ya descritas en el apartado 3.2, son la base de la mayoría de sistemas de visión actuales.  
- **Aplicaciones prácticas**:  
  - Clasificación de imágenes (e.g., reconocer dígitos en *Pac-Man*).  
  - Extracción de características para tareas más avanzadas.  

### 6.2 YOLO (You Only Look Once)  
#### 6.2.1 Concepto General  
- **Family of One-Stage Detectors**: A diferencia de modelos en dos fases (R-CNN, Faster R-CNN), YOLO realiza detección en **un único paso**:  
  1. Divide la imagen en una cuadrícula S×S.  
  2. Cada celda predice un número fijo de cajas (bounding boxes) + su grado de confianza + distribución de probabilidades de clases.  
  3. Filtra y refina esas cajas con Non-Maximum Suppression (NMS).  

#### 6.2.2 Características Principales  
- **Velocidad**: Capaz de procesar video en tiempo real (e.g., 45 FPS en YOLOv3).  
- **Precisión**: Buen compromiso entre velocidad y exactitud.  
- **Escalabilidad**: Nuevas versiones (YOLOv4, v5, v6, YOLOv7…) mejoran detección en pequeñas instancias y en condiciones difíciles de luz o ángulo.  

#### 6.2.3 ¿Cómo Trabaja YOLO?  
1. **División en cuadrícula**: Supongamos una imagen de 416×416 px dividida en 13×13 celdas.  
2. **Predicción de Bounding Boxes**: Cada celda genera 3–5 cajas con coordenadas normalizadas (x, y, w, h) y una **confidence score** (probabilidad de que la caja contenga un objeto + qué tan precisa es la caja).  
3. **Clasificación por celda**: Cada celda también emite probabilidades para cada clase (e.g., persona, coche, bicicleta).  
4. **Filtrado**: Se eliminan cajas con baja confianza y se aplican NMS para descartar cajas superpuestas que representen el mismo objeto.  

> **Analogía videojuego**: Imagina que cada celda es un “NPC” en *Halo*, que intenta adivinar si un enemigo está cerca y en qué dirección, y todos coordinan para apuntar con precisión sin duplicarse.  

---

## 7. Tareas Fundamentales en Visión por Ordenador  

> **Escena cinematográfica**: En *Blade Runner 2049*, los holocubos podrían analizar cada gota de lluvia para detectar rostros, seguir a personajes y reconstruir la trayectoria de un objeto. Estas tareas reales (aunque más modestas) se apoyan en algoritmos de detección, segmentación y tracking.

### 7.1 Detección de Objetos (Object Detection)  
- **Objetivo**: Identificar y localizar (mediante bounding boxes) todas las instancias de ciertas clases de objetos en una imagen.  
- **Salida típica**: Lista de (clase, caja delimitadora, confianza).  
- **Modelos clásicos**:  
  - **R-CNN (Region-based CNN)**:  
    1. Propuesta de regiones (Selective Search).  
    2. CNN que extrae características de cada región.  
    3. Clasificación + refinamiento de bounding boxes.  
  - **Fast/Faster R-CNN**: Integran la generación de propuestas con la red, mucho más rápido.  
  - **SSD (Single Shot Detector)**: Similar a YOLO, un solo paso.  
  - **YOLO**: Descrito anteriormente.  

### 7.2 Segmentación de Imágenes (Image Segmentation)  
- **Objetivo**: Clasificar cada píxel de la imagen en una clase (segmentación semántica) o marcar instancias individuales (segmentación de instancia).  
- **Tipos**:  
  1. **Segmentación Semántica**: Cada píxel recibe una etiqueta (e.g., “parte de una silla”, “parte del suelo”). No distingue entre multiples instancias de la misma clase.  
     - Modelos: FCN (Fully Convolutional Networks), U-Net, DeepLab.  
  2. **Segmentación de Instancia**: Además de clasificar píxeles, separa instancias individuales (p. ej., silla_1, silla_2).  
     - Modelos: Mask R-CNN, PANet.  

> **Ejemplo práctico**: En agricultura de precisión (imágenes de drones sobre campos de cultivo), la segmentación semántica permite distinguir distintos cultivos del suelo; la de instancia ayuda a contar plantas individuales para control de inventario.

### 7.3 Seguimiento de Objetos (Object Tracking)  
- **Objetivo**: Dado un objeto detectado en el primer frame de un video, seguir su trayectoria a lo largo de la secuencia.  
- **Tareas comunes**:  
  1. **Single Object Tracking (SOT)**: Seguimiento de un único objeto en movimiento (p. ej., el balón en un partido de *FIFA*).  
  2. **Multiple Object Tracking (MOT)**: Seguimiento simultáneo de múltiples objetos (p. ej., peatones en un cruce de tráfico).  
- **Enfoques clásicos**:  
  - **KCF (Kernelized Correlation Filters)**, MOSSE.  
  - **CamShift (Continuously Adaptive Mean Shift)**.  
- **Enfoques modernos (Deep Learning)**:  
  - **DeepSORT**: Combina detección (ej. YOLO) con un módulo de “re-identificación” basado en CNN para asociar el mismo objeto en distintos frames.  
  - **Track R-CNN**: Extiende Mask R-CNN para realizar detecciones y tracking simultáneamente.  

> **Analogía cinematográfica**: En *El Origen*, Cobb necesita seguir mentalmente a varios personajes en diferentes niveles de sueño (niveles de “frames” sucesivos) para coordinar el “kick” final. El tracking en visión hace un trabajo similar, manteniendo la identidad de cada objeto a lo largo del tiempo.

---

## 8. Resumen de Diferencias Entre Tareas  

| Tarea                    | Objetivo principal                                                   | Salida típica                               | Algoritmos comunes                                |
|--------------------------|----------------------------------------------------------------------|---------------------------------------------|---------------------------------------------------|
| **Clasificación de Imagen** | Determinar la clase predominante de toda la imagen                 | Etiqueta única (p. ej., “gato”)             | ResNet, VGG, Inception, EfficientNet              |
| **Detección de Objetos** | Localizar y clasificar múltiples objetos en una misma imagen         | Bounding boxes + etiquetas                  | R-CNN, Faster R-CNN, SSD, YOLO, RetinaNet         |
| **Segmentación Semántica** | Etiquetar cada píxel con una clase (sin distinguir instancias)      | Mapa de clases (imagen de tamaño original)  | FCN, U-Net, DeepLab, SegNet                       |
| **Segmentación de Instancia** | Etiquetar cada píxel y separar instancias individuales            | Mapas de máscaras para cada instancia       | Mask R-CNN, PANet, YOLACT                           |
| **Tracking de Objetos**  | Seguir la trayectoria de uno o varios objetos a lo largo de un video | Secuencia de bounding boxes con ID constante | KCF, MOSSE, CamShift, DeepSORT, Track R-CNN       |

---

## 9. Ejemplos de Aplicación en el Curso  

1. **Reconocimiento de Rostros para Seguridad**  
   - **Detección**: YOLO localiza rostros en la imagen.  
   - **Segmentación**: Mask R-CNN recorta con precisión las regiones faciales.  
   - **Tracking**: DeepSORT sigue personas en ambientes de vigilancia.  
   - **Caso friki**: En *Skyfall* (James Bond), los sistemas Skyfall Analytics combinan detección y tracking para seguir a Bond y villanos en tiempo real (¡un poco exagerado, pero cercano a lo que haremos con las técnicas básicas!).

2. **Control de Calidad en Manufactura**  
   - **Detección de defectos**: Una CNN entrenada reconoce arañazos o imperfecciones en piezas metálicas.  
   - **Segmentación de instancias**: U-Net identifica las áreas defectuosas pixel a pixel.  
   - **Tracking**: En una línea de producción, se sigue cada pieza para registrar estadísticas.  

3. **Juegos y Realidad Aumentada (AR)**  
   - **Detección de superficies**: Modelos CNN detectan superficies planas en tiempo real para proyectar elementos virtuales (como en *Pokémon Go* al capturar Pikachu).  
   - **Tracking de manos**: Deep Learning permite que, en *Half-Life: Alyx*, el casco VR reconozca la posición de la mano para interactuar con objetos.  

---

## 10. Qué Veremos en el Curso  

1. **Fundamentos de Visión por Ordenador**  
   - Historia, aplicaciones cotidianas, responsabilidades éticas (p. ej., privacidad, sesgos en datos).  
   - Procesamiento de imágenes clásicas (filtros, morfología).  

2. **Aprendizaje Automático & Deep Learning para Visión**  
   - Entrenamiento de modelos: conjuntos de datos (ImageNet, COCO).  
   - Arquitecturas CNN básicas: LeNet, AlexNet, VGG, ResNet.  
   - Transfer Learning: reutilizar pesos entrenados en grandes bases de datos.  

3. **Detección y Segmentación**  
   - R-CNN, Fast/Faster R-CNN, SSD, YOLO (versiones y mejoras).  
   - U-Net, Mask R-CNN, DeepLab.  

4. **Tracking de Objetos en Secuencias de Video**  
   - Métricas de evaluación (MOTA, MOTP).  
   - Algoritmos clásicos vs. DeepSORT.  

5. **Visión 3D y Realidad Aumentada**  
   - Reconstrucción 3D: estereo, SLAM, Point Clouds.  
   - Aplicaciones a videojuegos y entornos virtuales.  

6. **Proyectos Prácticos con TensorFlow y OpenCV**  
   - Detección en tiempo real con YOLOv5 + cámara web.  
   - Segmentación de semáforos en video de drones.  
   - Seguimiento de vehículos usando DeepSORT + YOLO.  

---

## 11. Conclusión  

Este curso de **Visión por Ordenador** te adentrará en cómo pasar **de píxeles a datos** útiles, combinando teoría y práctica. Aprenderás desde la teoría de **tipos de IA** y **aprendizaje automático** hasta la implementación de sistemas reales en **Deep Learning** (CNNs, YOLO, Mask R-CNN, etc.).  

¡Prepárate para “ver” el mundo con ojos de máquina! En cada tema, vincularemos conceptos con ejemplos frikis del cine y los videojuegos para que el aprendizaje sea ameno y relevante.  

---

> **Nota final**: No importa si al inicio las redes neuronales te parecen complejas; como en los videojuegos, la práctica constante (y las “vidas extra” en forma de ejercicios y ejemplos) te harán dominar estas técnicas. 🚀  