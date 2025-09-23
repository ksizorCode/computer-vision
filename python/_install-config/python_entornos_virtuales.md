# Instalación de Python

- instala python de la web oficial - python.org
- instala anaconda




# Entornos Virtuales de Python

https://www.youtube.com/watch?v=N9PdRkXOQ4w



## Trabajar con el Terminal / CMD - Panel de Comandos / PowerShell

Comandos básicos para trabajar con el cmd:

|Comando | Qué hace                                                 |
|--------|----------------------------------------------------------|
|cd..    |Change Directorio.. - Sube de nivel                       |
|cd      |C/:Loquesea/otracosa - lleva a esa ruta                   |
|cls     |limpia el cmd                                             |

---

## Instalación
- Instalar python
- en caso de desisntalar y tener que volver a instalar, es altamente recomendable borrar las variables del sistema y posibles restos. Para ello existen programas como Revo Unnistaller. Con el que seleccionaremos todos los elementos Phython, luego analizar que dependencias pueden haber quedado.


## Instalar un entorno virtual de Phyton
Saber qué versión de Python tengo instalada:

```terminal
python --version
```

## Instalación de modulos / paquetes

Vamos a instalar un modulo de entornos virtuales
```terminal
pip install virtualenv
```


Para ver los módulos que ya tengo instalados
```terminal
pip freeze
```


C:\Users\tuNombre\Desktop\Proyecto01>  virtualenv p1
C:\Users\tuNombre\Desktop\Proyecto01>  .\p1\Scripts\activate
