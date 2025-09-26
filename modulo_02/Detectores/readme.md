# Detectores, Descriptores y Clasificadores en Visión por Computador

En visión por computador hay dos grandes familias de algoritmos que a veces se usan juntos:

- **Detectores y descriptores de características** → SIFT, ORB, AKAZE, etc.  
- **Algoritmos de clasificación/búsqueda** → KNN, SVM, CNN, etc.  

---

## 🔎 Detectores y descriptores de características

Sirven para **identificar puntos clave** en una imagen (esquinas, bordes, zonas con textura) y describirlos de forma que se puedan comparar entre imágenes.  
Con ellos se pueden reconocer objetos, emparejar imágenes o calcular homografías (por ejemplo, para pegar fotos en un panorama).

### 1. SIFT (Scale-Invariant Feature Transform)  
- Inventado en 1999 por David Lowe.  
- Detecta puntos clave en diferentes escalas.  
- **Invariante a escala, rotación y cambios de iluminación.**  
- Muy robusto, aunque pesado en cálculo (antes estaba patentado, hoy es libre).  
- **Aplicaciones:** reconocimiento de objetos, stitching de panoramas.

### 2. ORB (Oriented FAST and Rotated BRIEF)  
- Alternativa libre y rápida a SIFT y SURF.  
- Detecta esquinas con **FAST** y las describe con **BRIEF** añadiendo orientación.  
- Mucho más rápido que SIFT, ideal para **tiempo real**.  
- **Aplicaciones:** SLAM en robótica, visión en móviles y AR.

### 3. AKAZE (Accelerated KAZE)  
- Evolución de **KAZE** (2012), que trabaja con espacios no lineales (difusión no lineal).  
- Más preciso que ORB en algunos casos y más rápido que SIFT.  
- Usa descriptores binarios para un matching eficiente.  
- **Aplicaciones:** registro de imágenes, tracking robusto.

---

## 🔹 Otros Detectores Clásicos
- **Harris Corner Detector** → detecta esquinas (muy básico).  
- **FAST (Features from Accelerated Segment Test)** → esquinas muy rápido (usado en ORB).  
- **DoG (Difference of Gaussians)** → base del SIFT.  
- **MSER (Maximally Stable Extremal Regions)** → detecta regiones estables.  

## 🔹 Otros Descriptores Clásicos
- **BRIEF (Binary Robust Independent Elementary Features)** → muy rápido, pero no rotacionalmente invariante.  
- **SURF (Speeded Up Robust Features)** → más rápido que SIFT, pero con patente (menos usado hoy).  
- **FREAK (Fast Retina Keypoint)** → inspirado en el ojo humano, rápido y binario.  
- **LATCH** → basado en parches de imagen, eficiente y robusto.

## 🔹 Detectores + Descriptores Modernos (Deep Learning)
Hoy en día se usan redes neuronales:  
- **SuperPoint** → aprende a detectar y describir puntos.  
- **R2D2** (Reliable and Repeatable Detector and Descriptor).  
- **D2-Net**.  
- **LoFTR** (Local Feature Transformer, basado en transformers).  

👉 Más potentes, pero necesitan **entrenamiento y GPU**.

---

## 🤖 Clasificadores

### 4. KNN (K-Nearest Neighbors)  
*(lo que a veces se llama erróneamente “KKN” en realidad es KNN)*  
- Algoritmo de **clasificación supervisada**.  
- Busca los **k vecinos más cercanos** a un punto en un espacio de características y vota la clase.  
- Ejemplo: si entrenas con imágenes de perros y gatos, y llega una nueva que se parece más a los vectores de “gato”, se clasifica como gato.  
- **Aplicaciones:** reconocimiento de patrones, clasificación en datasets pequeños.

---

### 🔹 Otros Clasificadores Clásicos
- **SVM (Support Vector Machines)** → separa datos con hiperplanos, muy usado en visión clásica.  
- **Decision Trees** → clasificación por reglas en forma de árbol.  
- **Random Forest** → conjunto de árboles de decisión.  
- **Naive Bayes** → basado en probabilidades.  
- **Logistic Regression** → muy usado para clasificación binaria.

### 🔹 Clasificadores Modernos (Deep Learning)
- **CNN (Convolutional Neural Networks)** → el estándar para clasificación de imágenes.  
- **Transformers (Vision Transformers, ViT)** → basados en atención, muy potentes en datasets grandes.  
- **Ensembles** → combinación de modelos (ej: stacking, boosting como XGBoost o LightGBM).

---

## 📊 Tabla comparativa

| Tipo | Ejemplos | Ventajas | Inconvenientes |
|------|----------|----------|----------------|
| **Detectores clásicos** | Harris, FAST, DoG, MSER | Simples, rápidos | Poco robustos ante cambios grandes |
| **Descriptores clásicos** | SIFT, SURF, ORB, BRIEF, FREAK, LATCH | Robustos (SIFT/AKAZE), rápidos (ORB, BRIEF) | Algunos con patente, limitados ante escenas complejas |
| **Detectores/Descriptores deep** | SuperPoint, R2D2, LoFTR | Muy robustos, estado del arte | Necesitan entrenamiento, GPU |
| **Clasificadores clásicos** | KNN, SVM, Árboles, Random Forest, Bayes | Simples, interpretables | Escalan mal con datos masivos |
| **Clasificadores modernos** | CNN, Vision Transformers | Máxima precisión, generalizan bien | Necesitan muchos datos y recursos |

---

## 📌 Resumen

- **SIFT, ORB y AKAZE** → detectan y describen puntos clave en imágenes.  
- **KNN, SVM, CNN…** → clasifican vectores de características (pueden usarse junto a los anteriores).  
- En visión moderna, los **deep models (CNN, Transformers)** ya hacen ambos pasos: detección + clasificación, todo en uno.
