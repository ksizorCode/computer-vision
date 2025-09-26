# Lectura de Códigos con Computer Vision

En Computer Vision, la lectura de códigos y etiquetas es una de las aplicaciones más prácticas y utilizadas, ya que permite extraer información directamente de objetos físicos usando cámaras y algoritmos de visión.

---

## Tipos de códigos generalmente utilizados

| Tema                                            | Descripción                                               | Aplicación práctica                                                |
|------------------------------------------------|----------------------------------------------------------|-------------------------------------------------------------------|
| Códigos de barras lineales (1D)               | Informacióncodificada en lineas o barras.                  | Escaneo de productos, inventario                                   |
| Códigos QR (2D)                               | Información codificada en 2 dimensiones                 | Tickets, enlaces, tarjetas de visita digitales                     |
| Códigos Data Matrix                             | Códigos 2D muy compactos, usados en industria          | Etiquetado de componentes electrónicos, piezas de fábrica          |
| Códigos Aztec                                  | Códigos 2D optimizados para transporte                 | Billetes de avión, transporte público                              |
| Códigos PDF417                                 | Códigos 2D con gran capacidad de datos                 | Documentos oficiales, carnets, pasaportes                          |
| Marcadores AR (fiduciales)                     | Patrón visual especial para realidad aumentada         | Posicionamiento de objetos en AR, robots, juegos                   |
| Etiquetas RFID visuales o híbridas             | QR + información de RFID, o códigos visuales específicos | Control de inventario avanzado, trazabilidad                       |
| Códigos de colores / codificación por color   | Detectar combinaciones de colores como “códigos”       | Sistemas simples de codificación industrial, etiquetado de cajas   |
| Marcas de agua visuales o patrones de seguridad | Patrones ocultos en documentos o imágenes            | Detección de falsificaciones, seguridad de tickets                 |
| Reconocimiento de logotipos o símbolos        | Identificación de marcas como “código visual”          | Publicidad, control de calidad, verificación de productos          |

---

## Librerías y herramientas en Python

Para leer y procesar estos códigos, podemos usar librerías como:

- **OpenCV**: detección de formas, manipulación de imágenes, detección de marcadores AR (ARUCO).
- **pyzbar**: lectura de códigos de barras y códigos QR.
- **python-barcode**: generación de códigos de barras.
- **qrcode**: generación de códigos QR.
- **zxing**: lectura de múltiples formatos de códigos 1D y 2D.
- **pytesseract / EasyOCR**: lectura de texto impreso o escrito dentro de etiquetas.
- **Mediapipe / Dlib**: seguimiento de patrones o símbolos específicos.

---

## Flujo general para la lectura de códigos

1. **Captura de imagen**  
   - Webcam, cámara industrial, smartphone.  
   - Ajustes de iluminación y resolución para mejorar la detección.

2. **Preprocesamiento**  
   - Conversión a escala de grises o binarización.  
   - Filtros: desenfoque, umbral adaptativo, detección de contornos.  

3. **Detección del código**  
   - Usando librerías específicas (pyzbar, OpenCV ARUCO).  
   - Identificación de la posición y orientación del código.

4. **Decodificación / Lectura de datos**  
   - Extracción del contenido: números, URL, texto, información codificada.  

5. **Uso de la información**  
   - Mostrar en pantalla, registrar en base de datos, activar procesos automáticos.

---

## Ejemplos de proyectos prácticos

- Escaneo de códigos QR de tickets para validar entradas en eventos.  
- Inventario automatizado leyendo códigos de barras de productos con webcam.  
- Robots que leen marcadores AR para moverse en un entorno controlado.  
- Detectar códigos de colores en cajas de productos para clasificación automática.  
- Sistemas de seguridad que detectan marcas de agua en documentos.  

---

## Buenas prácticas

- Asegurarse de buena iluminación y contraste.  
- Evitar ángulos muy oblicuos; rotar o corregir perspectiva si es necesario.  
- Probar distintos tamaños de códigos y distancias de la cámara.  
- Manejar errores: códigos parcialmente dañados o mal impresos.  
- Para códigos industriales, combinar visión con sensores RFID si es posible.  

---

Con estos apuntes, los alumnos pueden ver **el espectro completo de códigos visuales**, entender cómo se detectan y decodifican, y tener ideas para mini-proyectos prácticos con Python.



# Tipos de Códigos de Barras Lineales (1D)

Los códigos de barras lineales se usan para codificar información de forma visual y legible por escáneres. Los más comunes son EAN, UPC, Code39 y Code128.

| Código | Descripción | Características principales | Uso común |
|--------|------------|----------------------------|-----------|
| **EAN (European Article Number)** | Código de barras estándar europeo | - 13 dígitos (EAN-13) o 8 dígitos (EAN-8) <br> - Incluye prefijo de país y número de producto | Productos de supermercado, libros (ISBN) |
| **UPC (Universal Product Code)** | Código de barras estándar estadounidense | - 12 dígitos (UPC-A) <br> - Similar a EAN pero con prefijo diferente | Supermercados y retail en EE. UU. |
| **Code 39** | Código alfanumérico | - Puede incluir letras y números <br> - Menos denso que Code 128 <br> - Fácil de imprimir y escanear | Inventarios, identificadores internos, tarjetas de acceso |
| **Code 128** | Código alfanumérico de alta densidad | - Muy compacto, puede codificar todo ASCII <br> - Alta densidad de datos por longitud <br> - Permite codificación de caracteres especiales | Logística, envíos, etiquetas industriales |

---

## Tip práctico

- **EAN / UPC** → ideales para productos y supermercados, fáciles de reconocer visualmente.  
- **Code39 / Code128** → más usados en entornos industriales o corporativos, para inventarios, control de acceso y logística.
