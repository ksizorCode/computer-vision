# Marcadores ArUco

## ¿Qué son los Marcadores ArUco?

Los **marcadores ArUco** son patrones visuales cuadrados en blanco y negro que funcionan como códigos QR especializados para **Realidad Aumentada** y **visión por computadora**. Fueron desarrollados por la Universidad de Córdoba (España) y están integrados en OpenCV.

### Características principales:
- **Detección rápida** y robusta en tiempo real
- **Cálculo de pose** (posición y orientación) en 3D
- **Resistentes** a rotaciones, escalado y cambios de perspectiva
- **Código abierto** y gratuitos
- **Fácil implementación** con Python/OpenCV

## Anatomía de un Marcador ArUco

```
┌─────────────────┐
│ ■ ■ ■ ■ ■ ■ ■ ■ │ ← Borde negro (1 bit)
│ ■ □ □ ■ □ ■ □ ■ │ 
│ ■ ■ □ □ ■ ■ ■ ■ │ ← Datos del ID
│ ■ □ ■ ■ □ □ □ ■ │   (4x4, 5x5, 6x6, 7x7)
│ ■ ■ ■ □ □ ■ ■ ■ │
│ ■ □ □ ■ ■ □ ■ ■ │
│ ■ ■ ■ ■ ■ ■ ■ ■ │
└─────────────────┘
```

### Componentes:
1. **Borde exterior**: Marco negro de 1 bit de ancho
2. **Área de datos**: Patrón interno que codifica el ID único
3. **ID único**: Número identificador del marcador (0, 1, 2, ...)

## Diccionarios ArUco

Los marcadores se organizan en **diccionarios** que definen cuántos marcadores están disponibles y su robustez:

| Diccionario | Número de IDs | Tamaño | Descripción |
|-------------|---------------|---------|-------------|
| `DICT_4X4_50` | 50 IDs | 4×4 bits | Marcadores pequeños, detección rápida |
| `DICT_4X4_100` | 100 IDs | 4×4 bits | Más opciones, mismo tamaño |
| `DICT_4X4_250` | 250 IDs | 4×4 bits | Muchas opciones, 4×4 bits |
| `DICT_4X4_1000` | 1,000 IDs | 4×4 bits | Máximo para 4×4 |
| `DICT_5X5_50` | 50 IDs | 5×5 bits | Mayor robustez |
| `DICT_5X5_100` | 100 IDs | 5×5 bits | Equilibrio robustez/cantidad |
| `DICT_5X5_250` | 250 IDs | 5×5 bits | Más opciones |
| `DICT_5X5_1000` | 1,000 IDs | 5×5 bits | Máximo para 5×5 |
| `DICT_6X6_50` | 50 IDs | 6×6 bits | Muy robustos |
| `DICT_6X6_100` | 100 IDs | 6×6 bits | Buena opción general |
| `DICT_6X6_250` | 250 IDs | 6×6 bits | **Más popular** |
| `DICT_6X6_1000` | 1,000 IDs | 6×6 bits | Máximo para 6×6 |
| `DICT_7X7_50` | 50 IDs | 7×7 bits | Máxima robustez |
| `DICT_7X7_100` | 100 IDs | 7×7 bits | Muy robustos |
| `DICT_7X7_250` | 250 IDs | 7×7 bits | Robustos con muchas opciones |
| `DICT_7X7_1000` | 1,000 IDs | 7×7 bits | Máximo para 7×7 |

### Reglas importantes:
- **Más bits** (7×7 vs 4×4) = mayor robustez pero marcadores más grandes
- **Más IDs** = más opciones pero mayor posibilidad de confusión
- **Recomendado**: `DICT_6X6_250` para proyectos generales

## Implementación Práctica en Python

### 1. Instalación
```bash
pip install opencv-python
# o para funciones extras:
pip install opencv-contrib-python
```

### 2. Detección Básica de Marcadores

```python
import cv2
import numpy as np

# Configurar diccionario y parámetros
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()

# Inicializar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar marcadores
    corners, ids, rejected = cv2.aruco.detectMarkers(
        gray, aruco_dict, parameters=parameters
    )
    
    # Si se detectan marcadores
    if ids is not None:
        # Dibujar marcadores detectados
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
        # Mostrar información de cada marcador
        for i, marker_id in enumerate(ids):
            print(f"Marcador detectado: ID {marker_id[0]}")
    
    # Mostrar frame
    cv2.imshow('Detección ArUco', frame)
    
    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### 3. Generación de Marcadores

```python
import cv2
import numpy as np

# Configurar diccionario
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

# Generar marcador
marker_id = 42  # ID del marcador (0-249 para DICT_6X6_250)
marker_size = 200  # Tamaño en píxeles

marker_image = cv2.aruco.drawMarker(aruco_dict, marker_id, marker_size)

# Guardar imagen
cv2.imwrite(f'aruco_marker_{marker_id}.png', marker_image)

# Mostrar marcador
cv2.imshow(f'Marcador ArUco ID: {marker_id}', marker_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 4. Cálculo de Pose (Posición y Orientación)

```python
import cv2
import numpy as np

# Parámetros de calibración de cámara (ejemplo)
# En un proyecto real, estos se obtienen mediante calibración
camera_matrix = np.array([[800, 0, 320],
                         [0, 800, 240],
                         [0, 0, 1]], dtype=np.float32)

dist_coeffs = np.array([0.1, -0.2, 0, 0, 0], dtype=np.float32)

# Tamaño real del marcador en metros (ejemplo: 5cm)
marker_size = 0.05

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar marcadores
    corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    if ids is not None:
        # Dibujar marcadores
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        
        # Estimar pose de cada marcador
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
            corners, marker_size, camera_matrix, dist_coeffs
        )
        
        # Dibujar ejes 3D en cada marcador
        for i in range(len(ids)):
            cv2.aruco.drawAxis(frame, camera_matrix, dist_coeffs, 
                             rvecs[i], tvecs[i], marker_size)
            
            # Mostrar información de posición
            x, y, z = tvecs[i][0]
            print(f"Marcador {ids[i][0]}: X={x:.3f}, Y={y:.3f}, Z={z:.3f}")
    
    cv2.imshow('Pose ArUco', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Calibración de Cámara

Para obtener medidas precisas, es **fundamental** calibrar la cámara:

```python
import cv2
import numpy as np
import glob

def calibrate_camera():
    # Preparar puntos del tablero de ajedrez
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    
    # Preparar puntos 3D del tablero (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp = np.zeros((6*7, 3), np.float32)
    objp[:,:2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
    
    # Arrays para almacenar puntos 3D y 2D
    objpoints = []  # Puntos 3D en el mundo real
    imgpoints = []  # Puntos 2D en el plano de la imagen
    
    # Cargar imágenes del tablero de ajedrez
    images = glob.glob('calibration_images/*.jpg')
    
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Encontrar esquinas del tablero
        ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)
        
        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)
    
    # Calibrar cámara
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
        objpoints, imgpoints, gray.shape[::-1], None, None
    )
    
    return mtx, dist

# Usar la calibración
camera_matrix, dist_coeffs = calibrate_camera()
```

## Ventajas y Desventajas

### ✅ Ventajas
- **Detección robusta** en tiempo real
- **Cálculo de pose preciso** (6DOF: 3 posición + 3 rotación)
- **Resistente** a rotaciones y cambios de escala
- **Fácil implementación** con OpenCV
- **Código abierto** y gratuito
- **Múltiples marcadores** simultáneos
- **Buen rendimiento** computacional

### ❌ Desventajas
- **Requiere marcador visible** (no funciona sin él)
- **Sensible a iluminación** extrema
- **Puede ser estéticamente intrusivo**
- **Problemas con oclusión parcial**
- **Distancia limitada** de detección
- **Requiere calibración de cámara** para medidas precisas

## Aplicaciones Prácticas

### Educación
- Libros de texto con modelos 3D interactivos
- Visualización de conceptos abstractos
- Laboratorios virtuales

### Industria
- Asistencia en ensamblaje
- Control de calidad visual
- Mantenimiento guiado por AR

### Entretenimiento
- Juegos de realidad aumentada
- Filtros interactivos
- Experiencias inmersivas

### Investigación
- Robótica (localización y navegación)
- Seguimiento de objetos
- Análisis de movimiento

## Parámetros de Configuración Avanzados

```python
# Parámetros del detector ArUco
parameters = cv2.aruco.DetectorParameters_create()

# Ajustes principales
parameters.adaptiveThreshWinSizeMin = 3
parameters.adaptiveThreshWinSizeMax = 23
parameters.adaptiveThreshWinSizeStep = 10
parameters.adaptiveThreshConstant = 7

# Filtros de candidatos
parameters.minMarkerPerimeterRate = 0.03
parameters.maxMarkerPerimeterRate = 4.0
parameters.polygonalApproxAccuracyRate = 0.03

# Verificación de bits
parameters.minOtsuStdDev = 5.0
parameters.perspectiveRemovePixelPerCell = 4
parameters.perspectiveRemoveIgnoredMarginPerCell = 0.13

# Detección de esquinas
parameters.maxErroneousBitsInBorderRate = 0.35
parameters.minDistanceToBorder = 3
parameters.errorCorrectionRate = 0.6
```

## Consejos Prácticos

### Para Mejor Detección:
1. **Iluminación uniforme** sin sombras fuertes
2. **Marcadores planos** sin deformaciones
3. **Contraste alto** entre marcador y fondo
4. **Tamaño apropiado** según la distancia
5. **Evitar reflejos** en la superficie del marcador

### Para Proyectos:
1. **Calibra siempre** tu cámara para medidas precisas
2. **Usa DICT_6X6_250** para proyectos generales
3. **Imprime marcadores** en papel mate, no brillante
4. **Testa diferentes parámetros** según tu entorno
5. **Considera la distancia** máxima de trabajo

## Ejercicios Prácticos

### Ejercicio 1: Detector Básico
Crear un programa que detecte marcadores ArUco y muestre sus IDs en pantalla.

### Ejercicio 2: Contador de Marcadores
Programa que cuente cuántos marcadores diferentes ha visto y mantenga un registro.

### Ejercicio 3: AR Simple
Dibujar un cubo 3D virtual sobre cada marcador detectado.

### Ejercicio 4: Medidor de Distancias
Calcular y mostrar la distancia entre dos marcadores específicos.

## Recursos Adicionales

- **Documentación oficial**: [OpenCV ArUco Tutorial](https://docs.opencv.org/master/d5/dae/tutorial_aruco_detection.html)
- **Generador online**: [ArUco Marker Generator](https://chev.me/arucogen/)
- **Papers originales**: S. Garrido-Jurado et al. "Automatic generation and detection of highly reliable fiducial markers under occlusion"
- **GitHub**: [ArUco Library](https://github.com/opencv/opencv_contrib/tree/master/modules/aruco)

---

*Estos apuntes cubren los conceptos fundamentales de ArUco. Para proyectos específicos, siempre consulta la documentación oficial y realiza pruebas en tu entorno particular.*