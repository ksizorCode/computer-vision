# Clasificación de Imágenes

El proceso de asignar a una imagen una o múltiples etiquetas que describan su contenido.
La asignación de etiquetas atiend a un criterio un subjetivo, en función de quien etiquete una imagen puede tener diferentes clasificaciones. Ejemplo:

![imagen](https://live.staticflickr.com/1/91967_89bddcd616_z.jpg)

|Objetos    |Genéricas   |Semántico | Acciones |
|-----------|------------|----------|----------|
|persona    |ciudad      |cielo     |salto     |
|bicicleta  |rio         |agua      |peligro   |
|puente     |            |nubes     |          |
|persona    |            |          |          |

El objetivo del etiquetado es la creación de sistemas de clasificación de imágenes capaces de aprender; qué etiquetas tenemos que asignar a una determinada imagen a partir de un conjunto de imagenes de aprendizaje que ya han sido previamente etiquetadas.
El criterio de etiquetado utilizado se generará en base a la estructura que dedidamos que tenga nuestro dataset o conjunto de aprendizaje.

## ¿Que NO consideramos clasificación de imagen?

- Detección de objetos - detecta el objeto en la imagen e indica donde de forma autónoma. En nuestro caso clasificaremos las imágenes i
- Segmentación
- Busqueda por similitud / Retribal.

# Dificultadoes
Enorme variabilidad. Puede venir dada por:
- Iluminación
- Tamaño, posición, punto de vista
- Variavilidad en el fono de l aimagen
- Oclusiones parciales
- Variables intra-clase



# Esquema general de clasificación de imagen

```mermaid
flowchart TB
  A[Imagen] --> B[Estración de caractrísticas] --> C[Representación de imagen] --> D[Clasificación] --> E[Biblioteca]

  class Zebra{
   +bool is_wild
   +run()
   }
```

***Estracción de características***
Obtendremos características visuales a partir de la imagen. Cada característica visual se almacenará como vector numérico que describirá de forma visual las características de la región de la imagen.
- Detección de Puntos de interés - zonas que nos pueden dar informaicón relevante sobre el contenido de la imagen (cambios de contraste, contornos de los objetos, etc.. )
- Descripción local de los puntos de interés.


Representación de imagen - creación de vector numérico combinando todos los puntos de interés.

Clasificación - Se distribuirán las imágenes en un espacio multimensional que agrupará las imágenes por clases.

Biblioteca - 



