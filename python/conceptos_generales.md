# Introducción a Phyton

## 1. Introducción a Phyton

**¿Qué es Python y para qué sirve?**  
Python es un lenguaje de programación de alto nivel, interpretado y multiparadigma, muy popular por su sintaxis sencilla y legible. Se utiliza en desarrollo web, ciencia de datos, automatización, inteligencia artificial, visión por computador, scripting, entre otros.

**Filosofía “batteries included”**  
Python incluye una gran cantidad de módulos estándar que facilitan tareas comunes (manejo de fechas, operaciones matemáticas, acceso a archivos, redes, etc.) sin instalar bibliotecas adicionales.

> **Analogía cinéfila**: Imagina que Python es como el guion maestro de una película: ya trae las escenas básicas (“baterías incluidas”) para que no tengas que escribir cada detalle desde cero. Tú te encargas de agregar los efectos especiales (librerías externas) cuando lo necesites.

---

# 2. Instalación y primeros pasos

Durante el curso podremos ejecutar Python de dos maneras.
- En la nube, a través de Google Colab.
Se ejecuta a través del navegador y no requiere de instalación alguna y se ejecuta a través de celdas de código. Pudiendo compartimentar el código y añadirle anotaciones en markdown.
Es lo más sencillo pero hay ciertas funciones que no se pueden ejecutar.
Limitaciones de recurso en el uso de CPU o GPU
Dependencia de conexiones en caso de que sea inestable
Privacidad y seguridad
Limitaciones de personalización
Interrupcciones por tiempo de inactividad.

- A través de un entorno local.
Se ejecuta en tu ordenador. 
Mayor control de recursos.
Trabajo ofline
Personalización y flexibilidad bibliotecas
Privacidad y Seguridad. Los datos y archivos se mentienen en tu propia máquina.



## 2.1 Entorno en la Nube
### Google Colab
Trabajar con google colab solo requeriría de una cuenta de google y acceder a la web https://colab.research.google.com/
Los archivos pueden guardarse y crearse también desde google drive.

## 2.2 Entorno Local

Para instalar y congigurar un entorno de ejecución de Phyton en local deberemos:
Principal:
1.  Instalar Phyton

2.  Instalar uno o varios editores de código. Algunsos ejemplos pueden ser:
    - VSCode
    - PyChirm
    - Sublime Text
    - Atom
    - Windsurf
    - Cursor
    - Eclipse
    - Trae
    - etc…

3. Instalar herramientas de gestión de dependencias
    - pip
    - virtualenv

4.  Instalar librerías y gestionar versiones

Otros:
5.  Configurar un entorno de desarrollo ID
6.  Control de Versiones (Git)


Así pues empecemos con ello:

1. **Descarga e instalación**  
   - **Windows**: Descarga el instalador desde [python.org](https://www.python.org/downloads/) y asegúrate de marcar “Add Python to PATH”.  
   - **macOS**: Python viene preinstalado, pero se recomienda usar Homebrew:
     ```bash
     brew install python
     ```
   - **Linux**: Usualmente ya está instalado. Si no, en distribuciones basadas en Debian/Ubuntu:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

2. **Configuración de un editor/IDE**  
   - **Visual Studio Code**: extensiones “Python” (de Microsoft) y “Pylance”.  
   - **PyCharm**: versión Community es gratuita y muy completa.  
   - **Thonny**: ideal para principiantes, con interfaz simple.

4. **“Hello, world!” al estilo videojuego**  
   ```python
   # hello_game.py
   jugador = "Link"
   print(f"¡Bienvenido, héroe {jugador}! ¡Que comience la aventura!")

----


## Empezando con la programación

Una de las cosas más importantes en python es la indentación. A la hora de escribir código es muy importante que los elementos que pertenencen a un grupo o subgrupo (lo quehabitualmente en otros lenguajes se hace con llaves), esten aquí bien intendtados.

Ejemplo:

```javascript
// Ejemplo de estructura en JavaScript
if(edad>18){
    print("Puedes pasar");
}
```

```python
#Ejemplo de estructura en Python
if(edad>18)
    print("Puedes pasar")
```

# 1. Comentarios y documentación

Un comentarios es un escrito no tiene valor a nivel de código pero sí para el desarrollador. Se suele utilizar par hacer anogaciones, grupos, especificaciones o aclaraciones.
Los comentarios son de un gran valor a la hora de estructurar la programación, dejar explicaciones a otros programadores o a un mismo programador cuando tenga que volver a revisar el código. En muchos casos también se utiliza para desactivar fragmentos de código (dejar un bloque de código que no se ejecute) o las referencias de donde obtuvo una codumentación.

Comentarios de línea: Utiliza el símbolo # para añadir comentarios en una sola línea.

```python
# Este es un comentario que explica el propósito de la línea siguiente
vida_jugador = 100  # Variable que almacena las vidas del jugador
```

Bloques de comentarios (docstrings)
Las cadenas de documentación (docstrings) usan triple comilla ''' ''' o """ """ y se colocan al inicio de módulos, funciones o clases.
```python
def calcular_dano(ataque, defensa):
    """
    Calcula el daño infligido según ataque y defensa.
    - ataque: valor de ataque del personaje atacante.
    - defensa: valor de defensa del personaje defensor.
    Retorna un entero con el daño calculado.
    """
    dano = ataque - defensa
    return max(dano, 0)
```

Ejemplo de ambos tipos de comentarios:

```python
# ¡Que la fuerza te acompañe!
def usar_fuerza(intensidad):
    """
    Si eres Jedi, lanza un empujón con la Fuerza.
    Si eres Sith, lanza un rayo de Fuerza.
    """
    if intensidad > 50:
        print("¡Poder oscuro liberado!")
    else:
        print("Un empujón ligero con la Fuerza.")
````


---

# 2. Variables y tipos de datos básicos
Las variables son elementos que almacenan un valor.
En el siguiente ejemplo la variable nombre almacena pedro

```python
    nombre = "Pedro"
    nacimiento=1983
    cotiza=true
````

## Tipos de datos:

Enteros (int): Números sin parte decimal
```python
vidas = 7
nivel = 1
```
Reales/decimales (float): números con parte decimal
```python
velocidad=4.5
puntuación=1234.56
```

Texto/string (str): cadena de caracteres
```python
nombre='Matías'
saludo="Hellow There!"
````

Booleanos (bool): valores true o false / 0 o 1
```python
juego_terminado=false
pausa=true
````

Constantes
Una constante es una especie de variable que mantiene su valor durante el tiempo de ejecución del código. Es decir, su valor no cambia.
En otros lenguajes es muy habitual, pero en Python no existen. Es decir, puedes cambiarle el valor a una variable en cualquier momento.

Pero por herencia en la forma de trabajar con otros lenguajes se acostumbra a escribir en mayúsculas las variales que actuan como constantes.

PI = 3.1416
GRAVEDAD = 9.81


>Ejemplos de Variables
```python
    # Vida y energía de un personaje de RPG
    vida = 120                  # puntos de vida
    energia = 75.5              # puntos de energía (puede ser decimal)
    nombre = "Cloud"            # protagonista de Final Fantasy VII
    en_combate = True           # donde se encuentra ahora
    TITULO="Final Fantasy"      # titulo del videojuego
```

> *PEP 8 – Style Guide for Python Code* 
Recomendaciones a la hora de escribir código Python.
Puedes saber más de PEP 8 en este enlace: https://peps.python.org/pep-0008/

---

#4 Operadores
A la hora de realizar concatenaciones o cálculos matemáticos utilizamos operadores. 

Operadores aritméticos:
```python
a = 10         # Asignacion
b = 3
print(a + b)   # 13  (suma )
print(a - b)   # 7   (resta)
print(a * b)   # 30
print(a / b)   # 3.3333333333333335  (división real)
print(a // b)  # 3                   (división entera)
print(a % b)   # 1                   (módulo o resto)
print(a ** b)  # 1000                (potencia: 10^3)

```

Operadores de comparación:
```python
x = 5
y = 8
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False
```

Operadores lógicos
```python

vida_jugador = 0
tiene_pocion = True
# “and” / “or” / “not”
if vida_jugador <= 0 and tiene_pocion:
    print("¡Usa poción para revivir!")
if not tiene_pocion or vida_jugador > 0:
    print("No necesitas poción ahora.")

```


> Ejemplo de El señor de los anillos
```python
    # Calcular puntos de vida tras combate
    ataque_aragorn = 25
    defensa_orco = 10
    dano = ataque_aragorn - defensa_orco  # 15 puntos de daño
    vida_gimli = 40
    vida_gimli -= dano  # vida_gimli = 25
    print(f"¡Gimli queda con {vida_gimli} puntos de vida!")
```


# Entrada y salida de datos

print()

- imprime texto o variables en consola
- foramto con f-string (a partir de Phyton 3.6+)

```python
    nombre = "Lara Croft"
    nivel = 5
    print(f"¡Bienvenida, {nombre}! Estás en el nivel {nivel}.")
```

Formateo de cadenas
- Concatenación
```python
    mensaje = "Jugador: " + nombre + " | Nivel: " + str(nivel)
    print(mensaje)
```

- F-strings
```python
    print(f"Jugador: {nombre} | Nivel: {nivel}")
```

-format():
```pyton
    print("Jugador: {} | Nivel: {}".format(nombre, nivel))
```


- input()
Lee los datos que el usuario inserta a través del teclado
```python
    nombre = input("¿Cuál es tu nombre de héroe? ")
    print(f"¡Saludos, {nombre}! Prepárate para la misión.")
````

> Ejemplo
```python
    # Pedir nombre de héroe
    palabraSecreta = input("¡Di amigo y entra")
    print(f"Para abrir las puertas, hay que pronunciar la palabra "{palabraSecreta}" en Sindarin, que significa amigo")
```



# Estructura de los datos
