# Imágenes: conceptos clave como píxeles y canales de color (RGB).
## Conceptos fundamentales de imágenes en visión por ordenador

Una imagen digital es una enorme retícula de pixeles con valores numéricos para los canales Rojo, Verde y Azul.
Dependiendo de su tamaño hablaremos de resolución.

## Píxeles: la unidad básica
Un píxel (contracción de "picture element") es la unidad mínima de información en una imagen digital. Es el elemento más pequeño que puede ser controlado o representado en una pantalla o imagen digital.

## Estructura básica:
Una imagen digital es esencialmente una matriz bidimensional de píxeles, donde cada posición contiene información sobre el color y la intensidad de ese punto específico. Por ejemplo, una imagen de 1920x1080 píxeles contiene más de 2 millones de píxeles individuales organizados en 1920 columnas y 1080 filas.

## Representación numérica:
Cada píxel se representa mediante valores numéricos que indican su intensidad lumínica. En imágenes en escala de grises, un solo valor (típicamente entre 0 y 255) representa la intensidad, donde 0 es negro completo y 255 es blanco completo.

## Resolución e impacto:
La cantidad de píxeles determina la resolución de la imagen. Mayor número de píxeles generalmente significa mayor detalle y calidad visual, pero también mayor tamaño de archivo y requerimientos de procesamiento.

# Canales de color RGB
El modelo RGB (Red, Green, Blue) es el sistema de color más utilizado en visión por ordenador y dispositivos digitales, basado en la síntesis aditiva de color.

*Principio fundamental:* El modelo RGB replica cómo el ojo humano percibe los colores, combinando diferentes intensidades de rojo, verde y azul para crear todo el espectro visible. Este enfoque imita el funcionamiento de los conos en la retina humana, que son sensibles a estas tres longitudes de onda primarias.

*Estructura de canales:* Cada píxel en una imagen RGB contiene tres valores numéricos separados, uno para cada canal de color. Típicamente, cada canal se representa con valores entre 0 y 255 (8 bits por canal), permitiendo 256 niveles de intensidad por color.

*Representación práctica:* Un píxel RGB se expresa como una tupla (R, G, B). Por ejemplo, (255, 0, 0) representa rojo puro, (0, 255, 0) verde puro, (255, 255, 255) blanco, y (0, 0, 0) negro. La combinación (128, 64, 192) produciría un color púrpura específico.

*Espacio de color:* El modelo RGB puede representar aproximadamente 16.7 millones de colores diferentes (256³), cubriendo un rango sustancial del espectro visible humano.

# Implicaciones en visión por ordenador

*Procesamiento multicapa:* Los algoritmos de visión por ordenador deben procesar simultáneamente los tres canales de color. Las redes neuronales convolucionales, por ejemplo, utilizan filtros que operan sobre todos los canales para detectar características que pueden depender de combinaciones específicas de colores.
Representación tensorial: En frameworks de deep learning, una imagen RGB se representa como un tensor tridimensional con dimensiones altura × anchura × canales. Una imagen de 224×224 píxeles se convierte en un tensor de forma (224, 224, 3).

*Normalización y preprocesamiento:* Los valores de píxeles suelen normalizarse dividiendo por 255 para obtener valores entre 0 y 1, o mediante normalización estadística usando media y desviación estándar de datasets específicos.

*Otros modelos de color relevantes*
HSV (Hue, Saturation, Value): Útil para tareas que requieren separar información de color de la luminosidad, como segmentación basada en color o detección de objetos de colores específicos.
Escala de grises: Simplifica el procesamiento al usar un solo canal, calculado típicamente como una media ponderada de los canales RGB: Gris = 0.299×R + 0.587×G + 0.114×B.

*Canales alfa:* Algunos formatos incluyen un cuarto canal (RGBA) para transparencia, especialmente importante en aplicaciones de realidad aumentada y composición de imágenes.

Estos conceptos fundamentales forman la base sobre la cual se construyen todas las técnicas avanzadas de visión por ordenador, desde la detección de objetos hasta la síntesis de imágenes mediante inteligencia artificial.