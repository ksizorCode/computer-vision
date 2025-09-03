# Conceptos fundamentales de imágenes en visión por ordenador

En visión por ordenador, una imagen digital se describe como una matriz bidimensional de **píxeles**, donde cada píxel almacena información sobre color e intensidad. A continuación, se presentan los conceptos clave de forma estructurada y mejorada.

---

## 1. El píxel: unidad básica de la imagen digital

### 1.1 ¿Qué es un píxel?

- **Definición**: El término “píxel” (contracción de *picture element*) representa la unidad mínima de información en una imagen digital.
- **Función**: Cada píxel es un punto discreto en la retícula de la imagen que puede ser controlado o mostrado individualmente.
- **Contextualización**:  
  - En una pantalla, el píxel es el punto más pequeño que se ilumina.  
  - En un sensor de cámara, el píxel corresponde a un “fotodetector” que mide la intensidad de la luz en una posición concreta.

### 1.2 Estructura espacial de una imagen

- Una imagen se organiza como una **matriz** de tamaño `ancho × alto` (por ejemplo, 1920×1080).
- Cada posición `(x, y)` en esta matriz corresponde a un píxel con coordenadas específicas.  
  - El origen `(0, 0)` suele ubicarse en la esquina superior izquierda.
- **Resolución**:  
  - Se refiere al número total de píxeles:  
    \```
    Ancho × Alto = Número total de píxeles
    \```  
  - A mayor resolución → más detalle y mayor tamaño de fichero.

### 1.3 Representación numérica de intensidad

1. **Escala de grises**:  
   - Cada píxel almacena un valor único (0–255) que indica la intensidad lumínica.  
     - `0` → negro absoluto  
     - `255` → blanco absoluto  
     - Valores intermedios → tonos de gris  
   - Ejemplo: Una imagen de 8 bits en escala de grises permite 256 niveles de intensidad.

2. **Profundidad de bits (color depth)**:  
   | Bits por píxel | Número de niveles   | Ejemplo de uso         |
   |----------------|---------------------|------------------------|
   | 1 bit          | 2 (blanco/negro)    | Documentos escaneados  |
   | 8 bits         | 256                 | Grises simples         |
   | 16 bits        | 65.536              | Imágenes científicas   |
   | 24 bits        | 16.777.216          | Color True Color (RGB) |
   | 32 bits        | 4.294.967.296       | RGBA (incluye alfa)    |
   | 48 bits        | ~281 billones       | HDR profesional        |

- **Cálculo del tamaño en memoria**:  
  \```text
  Tamaño (bytes) = Ancho × Alto × Canales × BytesPorCanal
  \```  
  - Ejemplo: Imagen RGB 1920×1080 →  
    - Canales = 3 (R, G, B)  
    - BytesPorCanal = 1 (8 bits)  
    - Tamaño ≈ 1920 × 1080 × 3 × 1 = 6 220 800 bytes ≈ 6,2 MB

---

## 2. Canales de color: modelo RGB y otros espacios

### 2.1 Modelo RGB (Red, Green, Blue)

- **Principio aditivo**:  
  - Combina tres canales (rojo, verde y azul) con intensidades variables para generar cualquier color.  
  - Emula la forma en que los *conos* de la retina humana perciben la luz.

- **Representación de un píxel RGB**:  
  - Cada píxel se define como una tupla `(R, G, B)`, donde cada componente ∈ [0, 255].  
  - Ejemplos:  
    ```text
    (255, 0, 0)     → Rojo puro
    (0, 255, 0)     → Verde puro
    (0, 0, 255)     → Azul puro
    (255, 255, 255) → Blanco
    (0, 0, 0)       → Negro
    (128, 64, 192)  → Tono púrpura específico
    ```
- **Rango de colores**:  
  - Con 8 bits por canal → 256³ = 16 777 216 colores posibles.

### 2.2 Representación en frameworks de Deep Learning

- Una imagen RGB de tamaño `H×W` (por ejemplo, 224×224) se almacena como un **tensor** de forma `(H, W, 3)`.  
  - Canales:  
    1. Canal Rojo  
    2. Canal Verde  
    3. Canal Azul  
- **Normalización habitual**:  
  1. Dividir cada componente de `[0, 255]` a `[0.0, 1.0]` → facilitar la convergencia en redes neuronales.  
  2. O bien, restar la media y dividir por la desviación típica del dataset (p. ej., ImageNet):  
     \```python
     imagen_norm = (imagen / 255.0 - media) / desviación
     \```

### 2.3 Otros espacios de color relevantes

1. **HSV (Hue, Saturation, Value)**  
   - Separación de **Tono (H)**, **Saturación (S)** y **Valor/Luminosidad (V)**.  
   - Útil cuando interesa segmentar por color (p. ej., buscar todos los píxeles rojos sin importar intensidad).  

2. **Escala de grises (Grayscale)**  
   - Simplifica a un solo canal:  
     \```text
     Gris = 0.299·R + 0.587·G + 0.114·B
     \```  
   - Reducción de coste computacional para algoritmos que no necesitan color.

3. **RGBA**  
   - Igual que RGB, pero con un cuarto canal **Alfa** (transparencia).  
   - Fundamental en composición de imágenes y realidad aumentada.

4. **CMYK (Cyan, Magenta, Yellow, Black)**  
   - Modelo sustractivo para impresión.  
   - No suele usarse directamente en visión por ordenador, pero es relevante en pipelines de diseño gráfico multimedia.

---

## 3. Resolución, tamaño y calidad visual

### 3.1 Definición de resolución

- Se define por las dimensiones `(ancho × alto)` en píxeles.  
- Ejemplos comunes:  
  - **VGA**: 640 × 480  
  - **HD**: 1280 × 720  
  - **Full HD**: 1920 × 1080  
  - **4K**: 3840 × 2160  

### 3.2 Impacto de la resolución

| Característica       | Baja resolución            | Alta resolución               |
|----------------------|----------------------------|-------------------------------|
| Nivel de detalle     | Píxeles visibles           | Mayor nitidez                 |
| Tamaño de archivo    | Ligero                     | Pesado                        |
| Velocidad de procesado| Rápida                     | Requiere más poder de cálculo |
| Espacio en memoria   | Reducido                   | Mayor                         |

- **Elección en visión por ordenador**:  
  - Si el objetivo es detectar detalles finos (p. ej., grietas en una superficie), puede requerirse alta resolución.  
  - Para tareas rápidas en tiempo real (p. ej., tracking en vídeo), a veces se reduce la resolución para acelerar el procesamiento.

---

## 4. Preprocesamiento básico de píxeles

Antes de aplicar algoritmos de visión, se suelen realizar pasos de preprocesamiento que trabajan directamente sobre los valores de los píxeles:

### 4.1 Conversión de espacios de color

- **RGB → Grayscale**:  
  - Simplifica el problema a un solo canal.  
  - Fórmula ponderada:  
    \```text
    Gris = 0.299·R + 0.587·G + 0.114·B
    \```
- **RGB → HSV**:  
  - Permite segmentar por matiz (Hue), ignorando variaciones de brillo.  

### 4.2 Normalización y escalado

- **Dividir por 255**: Escalar valores a `[0.0, 1.0]`.  
- **Estandarización**: Restar la media y dividir por la desviación típica de cada canal.  
- **Clipping**: Limitar valores fuera de rango (0–255) por sobre/infraexposición.

### 4.3 Corrección de iluminación

- **Ecualización de histogramas** (p. ej., CLAHE) para mejorar contraste.  
- **Ajuste gamma** para corregir iluminaciones no lineales.

### 4.4 Filtrado y suavizado

- **Filtro de desenfoque (blur)**:  
  - `GaussianBlur`, `MedianBlur`, `BilateralFilter`.  
  - Reduce ruido antes de detectar bordes.
- **Detección de bordes**:  
  - Operadores como **Canny**, **Sobel**, **Laplace**.  
  - Convierte la imagen en mascaras de bordes para facilitar segmentación.

---

## 5. Implicaciones en visión por ordenador

### 5.1 Representación tensorial en Deep Learning

- Una imagen RGB cargada en un framework (TensorFlow, PyTorch) se convierte en un tensor de forma `(L, A, C)`:  
  - **L** = altura (height)  
  - **A** = anchura (width)  
  - **C** = canales (3 en RGB)  
- Ejemplo en PyTorch:  

```python
  from torchvision import transforms
  transform = transforms.Compose([
      transforms.Resize((224, 224)),
      transforms.ToTensor(),      
      transforms.Normalize(mean=[0.485, 0.456, 0.406],
                           std=[0.229, 0.224, 0.225])
  ])
  imagen_tensor = transform(imagen_pil)  # Forma: [3, 224, 224]
```
## 5.2 Procesamiento multicapa de canales
- **En redes neuronales convolucionales (CNN):**
  - Los filtros tienen tamaño `(k, k, 3)` para operar simultáneamente sobre los tres canales RGB.
  - Permiten extraer características que dependen de combinaciones específicas de colores.
  - Algunos algoritmos (p. ej., segmentación basada en color) pueden trabajar solo con el canal **Hue** de HSV en lugar de RGB completo.

## 5.3 Otros formatos y extensiones
- **Imágenes RGBA:**
  - Añaden un cuarto canal (**alfa**) para transparencia.
  - Muy usadas en realidad aumentada y composición multimedia.
- **Formatos de compresión:**
  - **JPEG:** compresión con pérdida → artefactos por cuantización.
  - **PNG:** compresión sin pérdida + canal alfa.
  - **TIFF:** formatos de alta profundidad (16–32 bits por canal), habituales en contextos científicos o profesionales.

---

## 6. Espacios de color alternativos: breve referencia

| Espacio    | Descripción                                            | Uso común                                      |
|------------|--------------------------------------------------------|------------------------------------------------|
| **RGB**    | Aditivo, 3 canales (Rojo, Verde, Azul)                 | Visualización en pantallas y cámaras digitales |
| **HSV**    | 3 canales (Matiz, Saturación, Valor)                    | Segmentación por color, selección intuitiva    |
| **Grayscale** | 1 canal (intensidad de brillo)                       | Tareas donde el color no aporta información    |
| **RGBA**   | RGB + Alfa (transparencia)                              | Composición de gráficos, realidad aumentada     |
| **CMYK**   | Sustractivo, 4 canales (Cian, Magenta, Amarillo, Negro) | Impresión y diseño gráfico                     |
| **LAB**    | Perceptualmente uniforme (Luminosidad + dos canales de color) | Procesamiento profesional de color, corrección de color |

---

## 7. Resumen y conclusiones
1. **El píxel** es la base de cualquier imagen digital. Conocer su representación numérica y profundidad en bits es crucial para entender la calidad y el tamaño de los datos.  
2. **Canales RGB:** Modelan cómo percibimos el color. Cada píxel contiene tres valores (R, G, B) que, combinados, generan más de 16 millones de colores.  
3. **Preprocesamiento:** Incluye normalización, conversión de espacios de color, corrección de iluminación y filtrado. Son pasos previos necesarios antes de aplicar algoritmos más avanzados.  
4. **Tensores en Deep Learning:** Las imágenes se manipulan como tensores tridimensionales `(alto, ancho, canales)`. Los frameworks esperan estos tensores normalizados para alimentar redes neuronales.  
5. **Espacios de color alternativos** (HSV, Grayscale, RGBA, CMYK, LAB) permiten simplificar tareas específicas o mejorar la precisión en segmentación y detección.

---

> **Tip Friky:** Imagina cada píxel como un bloque de Lego.  
> - En **RGB**, tienes tres tipos de bloques (rojo, verde y azul) que, al juntarlos en diferentes proporciones, construyen cualquier figura (color).  
> - Cuando trabajas con **HSV**, cambias la forma de “pintar” la figura (matiz y saturación), sin tocar la estructura.  
> - Y en **escala de grises**, solo usas bloques grises para ver la silueta de la figura.  

Conocer estas bases te permitirá entender y aplicar con éxito cualquier técnica de visión por ordenador, ya sea detección de objetos, clasificación, segmentación o reconstrucción 3D. ¡A programar y a explorar el universo de los píxeles!  