# Librerías Python para Computer Vision

Aquí hablaremos de las librerías más importantes, útiles y fáciles de usar en el mundo del computer vision, organizadas por categorías y evaluadas según diferentes criterios. Incluye historia, casos de uso reales y curiosidades sobre cada una.



## Librerías Principales de Computer Vision

### Librerías de Propósito General

| Librería | Lenguaje Principal | Facilidad de Uso | Popularidad | Casos de Uso Principales |
|----------|-------------------|------------------|-------------|-------------------------|
| **OpenCV** | C++/Python | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Procesamiento de imágenes, detección de objetos, análisis de video |
| **PIL/Pillow** | Python | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Manipulación básica de imágenes, conversiones de formato |
| **scikit-image** | Python | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Algoritmos de procesamiento de imágenes científicas |
| **NumPy** | Python | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Base matemática, arrays de imágenes, operaciones vectorizadas |
| **ImageIO** | Python | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | Lectura y escritura de múltiples formatos de imagen |

### Librerías de Deep Learning para Vision

| Librería | Framework Base | Facilidad de Uso | Rendimiento | Modelos Pre-entrenados |
|----------|----------------|------------------|-------------|----------------------|
| **TorchVision** | PyTorch | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ResNet, YOLO, Mask R-CNN, ViT |
| **TensorFlow/Keras** | TensorFlow | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | EfficientNet, MobileNet, Inception |
| **Detectron2** | PyTorch | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Detección y segmentación de objetos |
| **MMDetection** | PyTorch | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | Suite completa de detección de objetos |
| **Ultralytics** | PyTorch | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | YOLO v8, detección en tiempo real |

---

## Historia y Curiosidades de las Librerías

### OpenCV - El Gigante Veterano

| Aspecto | Detalles |
|---------|----------|
| **Creación** | 1999 por Intel Research |
| **Nombre completo** | Open Source Computer Vision Library |
| **Curiosidad histórica** | Originalmente pensado para aplicaciones de tiempo real en Intel |
| **Récord** | Más de 2500 algoritmos optimizados |
| **Casos famosos** | Sistema de reconocimiento facial de Facebook (inicialmente) |
| **Datos interesantes** | Escrito inicialmente en C, luego portado a C++ |

**Casos de uso históricos:**
- **2004**: Primeros sistemas de videovigilancia inteligente
- **2010**: Aplicaciones de realidad aumentada
- **Actualidad**: Vehículos autónomos, control de calidad industrial

### NumPy - La Fundación Silenciosa

| Aspecto | Detalles |
|---------|----------|
| **Creación** | 2006 por Travis Oliphant |
| **Precedente** | Evolucionó de Numeric y Numarray |
| **Importancia** | Base de prácticamente todas las librerías de Python científico |
| **Rendimiento** | 10-100x más rápido que Python puro para operaciones matemáticas |
| **Curiosidad** | Una imagen es solo un array de NumPy con forma (altura, ancho, canales) |

**¿Por qué es crucial en computer vision?**
- **Representación de imágenes**: Cada píxel es un número
- **Operaciones vectorizadas**: Procesar millones de píxeles simultáneamente
- **Interoperabilidad**: Todas las librerías de CV hablan "NumPy"

### PIL/Pillow - El Superviviente

| Aspecto | Detalles |
|---------|----------|
| **PIL original** | 1995 por Fredrik Lundh |
| **Pillow (fork)** | 2010 como continuación de PIL |
| **Drama histórico** | PIL se volvió incompatible con Python 3, nació Pillow |
| **Simplicidad** | API diseñada para ser intuitiva desde el día 1 |
| **Adopción** | Incluida por defecto en muchas distribuciones |

**Casos de uso icónicos:**
- **Primeras startups web**: Redimensionado automático de avatares
- **Instagram**: Procesamiento inicial de filtros (antes de migrar a soluciones más complejas)
- **Blogs y CMS**: Generación automática de thumbnails

### TorchVision - El Revolucionario Moderno

| Aspecto | Detalles |
|---------|----------|
| **Lanzamiento** | 2016 junto con PyTorch |
| **Padre** | Facebook AI Research (FAIR) |
| **Revolución** | Democratizó el uso de modelos pre-entrenados |
| **Impacto** | Redujo el tiempo de desarrollo de meses a días |
| **Modelos icónicos** | ResNet cambió la historia del deep learning |

### Detectron2 - El Especialista de Élite

| Aspecto | Detalles |
|---------|----------|
| **Origen** | 2019, sucesor de Detectron |
| **Creador** | Facebook AI Research |
| **Especialidad** | Detección y segmentación de objetos de última generación |
| **Velocidad** | 2x más rápido que su predecesor |
| **Casos famosos** | Análisis de video en redes sociales, aplicaciones médicas |

### Ultralytics - El Joven Prodigio

| Aspecto | Detalles |
|---------|----------|
| **Fundación** | 2020 por Glenn Jocher |
| **Filosofía** | "Computer vision simple y accesible" |
| **YOLOv5 controversy** | Creó controversia al llamar YOLOv5 a su implementación |
| **Éxito** | Más fácil de usar que implementaciones oficiales YOLO |
| **Comunidad** | Crecimiento explosivo en GitHub |

---

## Casos de Uso Reales y Curiosidades

### Aplicaciones Históricas Famosas

| Aplicación | Librería Principal | Año | Impacto |
|------------|-------------------|-----|---------|
| **Google Photos** | TensorFlow/OpenCV | 2015 | Búsqueda por contenido visual |
| **Tesla Autopilot** | Múltiples (custom + OpenCV) | 2016 | Conducción autónoma |
| **Snapchat Filters** | OpenCV + Custom | 2015 | AR en tiempo real masivo |
| **Amazon Go** | Deep learning + OpenCV | 2018 | Tiendas sin cajeros |
| **COVID-19 Diagnosis** | scikit-image + deep learning | 2020 | Análisis de rayos X |

### Curiosidades Técnicas

| Librería | Curiosidad |
|----------|------------|
| **OpenCV** | Puede detectar sonrisas, pero también pestañeos y bostezos |
| **NumPy** | Una imagen 4K RGB ocupa exactamente 24.8 MB en NumPy |
| **Pillow** | Soporta más de 30 formatos de imagen diferentes |
| **TorchVision** | Sus modelos pre-entrenados han "visto" millones de imágenes de ImageNet |
| **scikit-image** | Incluye algoritmos que ganaron competencias académicas |

### Récords y Estadísticas Sorprendentes

| Métrica | Dato |
|---------|------|
| **OpenCV descargas** | >200 millones de instalaciones |
| **YOLO detección** | Puede procesar >150 FPS en GPUs modernas |
| **ImageNet dataset** | 14+ millones de imágenes etiquetadas |
| **Tiempo de entrenamiento** | ResNet-50 desde cero: ~25 horas en GPU moderna |
| **Precisión humana** | ImageNet error rate humano: ~5.1% |

### Principiantes

| Librería | Instalación | Documentación | Curva de Aprendizaje | Comunidad |
|----------|-------------|---------------|---------------------|-----------|
| **Pillow** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Ultralytics** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **OpenCV** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **scikit-image** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

### Usuarios Intermedios/Avanzados

| Librería | Flexibilidad | Personalización | Rendimiento | Ecosistema |
|----------|-------------|----------------|-------------|------------|
| **TorchVision** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Detectron2** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **OpenCV** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **MMDetection** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## Casos de Uso Específicos

### Procesamiento Básico de Imágenes

| Tarea | Librería Recomendada | Alternativas | Dificultad |
|-------|---------------------|--------------|------------|
| Redimensionar imágenes | Pillow | OpenCV, scikit-image | ⭐ |
| Aplicar filtros | scikit-image | OpenCV | ⭐⭐ |
| Conversión de formatos | Pillow | ImageIO | ⭐ |
| Ajustes de color | OpenCV | scikit-image, Pillow | ⭐⭐ |

### Detección y Reconocimiento

| Tarea | Librería Recomendada | Modelos Populares | Dificultad |
|-------|---------------------|-------------------|------------|
| Detección de objetos | Ultralytics | YOLOv8, YOLOv5 | ⭐⭐ |
| Reconocimiento facial | OpenCV | Haar Cascades, DLib | ⭐⭐⭐ |
| Segmentación semántica | Detectron2 | Mask R-CNN | ⭐⭐⭐⭐ |
| Clasificación de imágenes | TorchVision | ResNet, EfficientNet | ⭐⭐ |

### Análisis de Video

| Tarea | Librería Recomendada | Características | Dificultad |
|-------|---------------------|----------------|------------|
| Lectura de video | OpenCV | Múltiples codecs | ⭐ |
| Tracking de objetos | OpenCV | Algoritmos integrados | ⭐⭐⭐ |
| Análisis temporal | OpenCV + NumPy | Procesamiento frame a frame | ⭐⭐⭐ |
| Detección en tiempo real | Ultralytics | Optimizado para velocidad | ⭐⭐ |

---

## Instalación y Configuración

### Comandos de Instalación

| Librería | Comando pip | Dependencias Adicionales |
|----------|-------------|-------------------------|
| **Pillow** | `pip install Pillow` | Ninguna |
| **OpenCV** | `pip install opencv-python` | Ninguna para uso básico |
| **scikit-image** | `pip install scikit-image` | NumPy, SciPy |
| **NumPy** | `pip install numpy` | Ninguna (es la base) |
| **TorchVision** | `pip install torch torchvision` | PyTorch |
| **Ultralytics** | `pip install ultralytics` | PyTorch, OpenCV |
| **Detectron2** | Ver documentación oficial | PyTorch, CUDA (recomendado) |

### Requisitos del Sistema

| Librería | GPU Requerida | RAM Mínima | Compatibilidad |
|----------|---------------|------------|----------------|
| **Pillow** | No | 512 MB | Windows, macOS, Linux |
| **OpenCV** | Opcional | 1 GB | Windows, macOS, Linux |
| **TorchVision** | Recomendada | 4 GB | Windows, macOS, Linux |
| **Detectron2** | Sí (para entrenamiento) | 8 GB | Linux (principalmente) |
| **Ultralytics** | Recomendada | 4 GB | Windows, macOS, Linux |

---

## Ejemplos de Código Básico

### Carga y Manipulación de Imágenes

| Librería | Ejemplo de Código | Uso Típico |
|----------|-------------------|------------|
| **Pillow** | ```python<br>from PIL import Image<br>img = Image.open('foto.jpg')<br>img.resize((300, 300))``` | Manipulación básica |
| **OpenCV** | ```python<br>import cv2<br>img = cv2.imread('foto.jpg')<br>gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)``` | Procesamiento avanzado |
| **scikit-image** | ```python<br>from skimage import io, filters<br>img = io.imread('foto.jpg')<br>edges = filters.sobel(img)``` | Análisis científico |
| **NumPy** | ```python<br>import numpy as np<br>img = np.array(Image.open('foto.jpg'))<br>img_bright = img + 50``` | Manipulación matemática |

---

## Recomendaciones por Nivel

### Para Principiantes
- **Comenzar con**: Pillow para manipulación básica
- **Siguiente paso**: OpenCV para procesamiento más avanzado
- **Para deep learning**: Ultralytics para detección de objetos

### Para Desarrollo Profesional
- **Base sólida**: OpenCV + scikit-image
- **Deep learning**: TorchVision o TensorFlow/Keras
- **Proyectos específicos**: Detectron2 o MMDetection

### Para Investigación
- **Flexibilidad máxima**: PyTorch + TorchVision
- **Algoritmos SOTA**: MMDetection, Detectron2
- **Experimentación**: Combinación de múltiples librerías

---

## Conclusiones

### Librerías Más Versátiles
1. **OpenCV** - El estándar de la industria
2. **TorchVision** - Mejor para deep learning
3. **Pillow** - Perfecta para tareas simples

### Criterios de Selección
- **Facilidad de uso**: Pillow > Ultralytics > OpenCV
- **Potencia**: Detectron2 > TorchVision > OpenCV
- **Comunidad**: OpenCV > TorchVision > scikit-image
- **Documentación**: Ultralytics > TorchVision > Pillow

### Recomendación Final
Para la mayoría de proyectos, una combinación de **NumPy** (base matemática), **OpenCV** (procesamiento), **TorchVision** (deep learning) y **Pillow** (manipulación básica) cubre el 95% de las necesidades en computer vision.

### El Stack Perfecto por Escenario

**Para Prototipado Rápido:**
```python
import numpy as np
from PIL import Image
import cv2
```

**Para Producción Empresarial:**
```python
import numpy as np
import cv2
import torch
import torchvision
```

**Para Investigación Académica:**
```python
import numpy as np
from skimage import *
import torch
import torchvision
# + librerías especializadas según necesidad
```


# Otras Librerías para otros ámbitos:

# Librerías Python por Categoría

| Categoría | Librería | Descripción en Español | URL Oficial |
|-----------|----------|------------------------|-------------|
| **Computación Cuántica (Quantum Computing)** | QuTiP | Caja de herramientas cuánticas en Python para simular dinámicas de sistemas cuánticos abiertos y cerrados | https://qutip.org/ |
| | PyQuil | Librería Python para programación cuántica usando Quil, el lenguaje de instrucciones cuánticas de Rigetti | https://pyquil-docs.rigetti.com/ |
| | Qiskit | Marco de trabajo de código abierto para computación cuántica desarrollado por IBM | https://qiskit.org/ |
| | PennyLane | Librería multiplataforma para aprendizaje automático cuántico y programación cuántica diferenciable | https://pennylane.ai/ |
| **Estadística Computacional (Statistical Computing)** | Pandas | Librería para manipulación y análisis de datos estructurados | https://pandas.pydata.org/ |
| | statsmodels | Herramientas estadísticas para modelado estadístico y econometría | https://www.statsmodels.org/ |
| | Xarray | Manejo de matrices N-dimensionales etiquetadas y conjuntos de datos | https://xarray.dev/ |
| | Seaborn | Librería de visualización estadística basada en matplotlib | https://seaborn.pydata.org/ |
| **Procesamiento de Señales (Signal Processing)** | SciPy | Librería para computación científica con algoritmos de procesamiento de señales | https://scipy.org/ |
| | PyWavelets | Transformadas wavelet discretas y continuas | https://pywavelets.readthedocs.io/ |
| | python-control | Librería para análisis y diseño de sistemas de control | https://python-control.org/ |
| | HyperSpy | Análisis interactivo de datos multidimensionales | https://hyperspy.org/ |
| **Procesamiento de Imágenes (Image Processing)** | Scikit-image | Algoritmos de procesamiento de imágenes | https://scikit-image.org/ |
| | OpenCV | Librería de visión computacional y procesamiento de imágenes | https://opencv.org/ |
| | Mahotas | Visión computacional y procesamiento de imágenes rápido | https://mahotas.readthedocs.io/ |
| **Gráficos y redes (Graphs and Networks)** | NetworkX | Creación, manipulación y estudio de redes complejas | https://networkx.org/ |
| | graph-tool | Manipulación y análisis eficiente de grafos | https://graph-tool.skewed.de/ |
| | igraph | Análisis y visualización de redes | https://igraph.org/python/ |
| | PyGSP | Procesamiento de señales en grafos | https://pygsp.readthedocs.io/ |
| **Astronomía (Astronomy)** | AstroPy | Librería fundamental de astronomía comunitaria | https://www.astropy.org/ |
| | SunPy | Librería para física solar | https://sunpy.org/ |
| | SpacePy | Herramientas para física espacial | https://spacepy.github.io/ |
| **Psicología (Cognitive Psychology)** | PsychoPy | Creación de experimentos en psicología y neurociencia | https://www.psychopy.org/ |
| **Bioinformática (Bioinformatics)** | BioPython | Herramientas para computación biológica | https://biopython.org/ |
| | Scikit-Bio | Estructuras de datos y algoritmos para bioinformática | https://scikit-bio.org/ |
| | PyEnsembl | Interfaz Python para bases de datos genómicas Ensembl | https://github.com/openvax/pyensembl |
| | ETE | Análisis y visualización de árboles filogenéticos | http://etetoolkit.org/ |
| **Bayesian Inference** | PyStan | Interfaz Python para modelado bayesiano con Stan | https://pystan.readthedocs.io/ |
| | PyMC | Programación probabilística bayesiana | https://www.pymc.io/ |
| | ArviZ | Análisis exploratorio de modelos bayesianos | https://arviz-devs.github.io/ |
| | emcee | Muestreador MCMC ensemble | https://emcee.readthedocs.io/ |
| **Mathematical Analysis** | SciPy | Algoritmos fundamentales para computación científica | https://scipy.org/ |
| | SymPy | Librería para matemáticas simbólicas | https://www.sympy.org/ |
| | cvxpy | Modelado y resolución de problemas de optimización convexa | https://www.cvxpy.org/ |
| | FEniCS | Plataforma para resolver ecuaciones diferenciales parciales | https://fenicsproject.org/ |
| **Química (Chemistry)** | Cantera | Herramientas para cinética química, termodinámica y transporte | https://cantera.org/ |
| | MDAnalysis | Análisis de simulaciones de dinámica molecular | https://www.mdanalysis.org/ |
| | RDKit | Toolkit de quimioinformática | https://www.rdkit.org/ |
| | PyBaMM | Modelado matemático de baterías | https://www.pybamm.org/ |
| **Geociencias (Geoscience)** | Pangeo | Ecosistema para geociencias de big data | https://pangeo.io/ |
| | Simpeg | Simulación y estimación de parámetros en geofísica | https://simpeg.xyz/ |
| | ObsPy | Librería para procesamiento de datos sismológicos | https://obspy.org/ |
| | Fatiando a Terra | Herramientas de modelado geofísico | https://www.fatiando.org/ |
| **Procesamiento Geoespacial (Geographic Processing)** | Shapely | Manipulación y análisis de objetos geométricos planares | https://shapely.readthedocs.io/ |
| | GeoPandas | Extensión de pandas para datos geoespaciales | https://geopandas.org/ |
| | Folium | Visualización de datos geoespaciales interactivos | https://python-visualization.github.io/folium/ |
| **Arquitectura e Ingeniería (Architecture & Engineering)** | COMPAS | Marco computacional para arquitectura e ingeniería | https://compas.dev/ |
| | City Energy Analyst | Análisis de sistemas energéticos urbanos | https://cityenergyanalyst.com/ |
| | Sverchok | Herramienta paramétrica para arquitectura y diseño | https://github.com/nortikin/sverchok |