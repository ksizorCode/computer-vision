# Módulo 02: El aprendizaje automático

## ¿Qué es el aprendizaje automático? ¿Cómo se relaciona con la visión por ordenador?

El aprendizaje automático es una rama de la inteligencia artificial que permite a los sistemas aprender y mejorar automáticamente a partir de la experiencia sin ser explícitamente programados. En visión por ordenador, el aprendizaje automático es fundamental para que los sistemas puedan interpretar y analizar imágenes y videos de manera eficiente.

### Evolución histórica

- **1950s-1960s**: Primeros conceptos de aprendizaje automático (perceptrón)
- **1980s**: Resurgimiento con redes neuronales y algoritmos de backpropagation
- **1990s-2000s**: Desarrollo de SVM, Random Forests y métodos estadísticos
- **2010s-presente**: Revolución del Deep Learning, especialmente en visión por ordenador

### Relación con la visión por ordenador

- **Reconocimiento de patrones**: El ML permite identificar patrones visuales complejos en imágenes
- **Automatización de tareas visuales**: Sustituye reglas manuales por aprendizaje a partir de datos
- **Escalabilidad**: Capacidad para manejar grandes volúmenes de datos visuales
- **Adaptabilidad**: Ajuste a nuevas condiciones visuales mediante reentrenamiento

### Aplicaciones específicas

- Detección y reconocimiento de objetos
- Segmentación de imágenes
- Reconocimiento facial
- Análisis de escenas
- Reconstrucción 3D
- Estimación de pose
- Seguimiento de objetos en video

## Principios básicos para entrenar y probar modelos

### Recolección y preparación de datos

- **Fuentes de datos**: Datasets públicos, datos propios, datos sintéticos
- **Anotación**: Etiquetado manual, semi-automático o automático
- **Preprocesamiento**:
  - Normalización (escalar valores a un rango específico)
  - Estandarización (media 0, desviación estándar 1)
  - Aumento de datos (data augmentation)

```python
# Ejemplo de preprocesamiento y aumento de datos con OpenCV y NumPy
import cv2
import numpy as np

# Cargar imagen
img = cv2.imread('imagen.jpg')

# Normalización
img_normalized = img / 255.0

# Estandarización
mean = np.mean(img, axis=(0, 1))
std = np.std(img, axis=(0, 1))
img_standardized = (img - mean) / std

# Aumento de datos básico
img_flipped = cv2.flip(img, 1)  # Volteo horizontal
img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  # Rotación
```

- División de datos en conjuntos de entrenamiento, validación y prueba.

### División de datos
- Conjunto de entrenamiento (60-80%): Para entrenar el modelo
- Conjunto de validación (10-20%): Para ajustar hiperparámetros
- Conjunto de prueba (10-20%): Para evaluación final

````
# División de datos con scikit-learn
from sklearn.model_selection import train_test_split

# X: características, y: etiquetas
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

print(f"Entrenamiento: {len(X_train)} muestras")
print(f"Validación: {len(X_val)} muestras")
print(f"Prueba: {len(X_test)} muestras")
````



### Selección del modelo adecuado
- Complejidad del problema : Lineal vs. no lineal
- Cantidad de datos disponibles : Modelos simples para pocos datos
- Interpretabilidad : Árboles vs. redes neuronales
- Velocidad de inferencia : Requisitos de tiempo real
- Recursos computacionales : Entrenamiento e inferencia
### Entrenamiento del modelo
- Optimización de parámetros : Ajuste de pesos mediante algoritmos como descenso de gradiente
- Épocas : Número de pasadas completas por el conjunto de entrenamiento
- Batch size : Número de muestras procesadas antes de actualizar parámetros
- Tasa de aprendizaje : Tamaño de los pasos en la optimización

````
# Ejemplo de entrenamiento de un modelo de clasificación simple
from sklearn.ensemble import RandomForestClassifier

# Crear y entrenar el modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predicciones en conjunto de validación
y_pred = model.predict(X_val)
```

### Evaluación del modelo
- Métricas para clasificación :
  
  - Precisión (accuracy)
  - Precisión y exhaustividad (precision & recall)
  - F1-score
  - Matriz de confusión
  - Curva ROC y AUC
- Métricas para regresión :
  
  - Error cuadrático medio (MSE)
  - Error absoluto medio (MAE)
  - R² (coeficiente de determinación)

```python
# Evaluación de un modelo de clasificación
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Calcular métricas
accuracy = accuracy_score(y_val, y_pred)
print(f"Precisión: {accuracy:.4f}")

print("\nInforme de clasificación:")
print(classification_report(y_val, y_pred))

print("\nMatriz de confusión:")
print(confusion_matrix(y_val, y_pred))
```

### Ajuste de hiperparámetros
- Búsqueda en cuadrícula (Grid Search) : Prueba sistemática de combinaciones
- Búsqueda aleatoria (Random Search) : Muestreo aleatorio del espacio de hiperparámetros
- Validación cruzada : Evaluación robusta de hiperparámetros

```python
# Ajuste de hiperparámetros con Grid Search
from sklearn.model_selection import GridSearchCV

# Definir parámetros a probar
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10]
}

# Crear el buscador de parámetros
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), 
                          param_grid, 
                          cv=5, 
                          scoring='accuracy')

# Entrenar con todos los parámetros
grid_search.fit(X_train, y_train)

# Mejores parámetros y resultado
print(f"Mejores parámetros: {grid_search.best_params_}")
print(f"Mejor precisión: {grid_search.best_score_:.4f}")

# Usar el mejor modelo
best_model = grid_search.best_estimator_
```




## Tipos de aprendizaje automático
- Aprendizaje supervisado
- Aprendizaje no supervisado
- Aprendizaje por refuerzo

## Tipos de aprendizaje automático
### Aprendizaje supervisado
En el aprendizaje supervisado, el modelo aprende a partir de datos etiquetados, donde cada ejemplo tiene una entrada y una salida deseada.
 Diferencias entre regresión y clasificación
- Regresión :
  
  - Predice valores continuos (números reales)
  - Ejemplos: predicción de precios, temperatura, edad
  - Métricas: MSE, MAE, R²
- Clasificación :
  
  - Asigna etiquetas a categorías discretas
  - Ejemplos: detección de objetos, reconocimiento facial, diagnóstico médico
  - Métricas: precisión, recall, F1-score, AUC Modelos de regresión Regresión lineal
- Concepto : Modelado de relación lineal entre variables
- Ecuación : y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
- Ventajas : Simple, interpretable, rápido
- Desventajas : Asume relación lineal, sensible a outliers
```python# Regresión lineal con scikit-learn
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Crear y entrenar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Coeficientes e intercepto
print(f"Intercepto: {model.intercept_}")
print(f"Coeficientes: {model.coef_}")

# Predicciones
y_pred = model.predict(X_test)

# Visualización
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicción')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
```



## Aprendizaje supervisado
Diferencias entre regresión y clasificación:
- Regresión: predice valores continuos.
- Clasificación: asigna etiquetas a categorías.

Estudio de modelos:
- Regresión lineal y logística
- Máquinas de vectores de soporte (SVM)
- Árboles de decisión
- Random Forest
- K-Nearest Neighbors (KNN)

## Aprendizaje no supervisado
Características:
- No requiere etiquetas en los datos.
- Busca patrones o estructuras ocultas.

Modelos:
- K-means
- DBSCAN
- Clustering jerárquico

## Deep Learning
### Estructura básica de las redes neuronales artificiales
- Neuronas artificiales
- Capas (entrada, ocultas, salida)
- Funciones de activación
- Propagación hacia adelante y retropropagación

### Redes neuronales convolucionales (CNNs)
- Arquitectura especializada para datos con estructura en forma de cuadrícula, como imágenes.
- Capas convolucionales, de pooling y totalmente conectadas.
- Impacto en la visión por ordenador: mejora significativa en tareas como reconocimiento de objetos, segmentación y clasificación.
- Aplicaciones en el mundo real: vehículos autónomos, diagnóstico médico, vigilancia, entre otros.