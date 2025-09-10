import cv2
import numpy as np
from PIL import ImageGrab
import time
import os
from datetime import datetime

class DetectorTiempoReal:
    def __init__(self):
        # Configurar YOLO
        self.net = None
        self.output_layers = None
        self.classes = []
        self.colors = None
        
        # Clases que queremos detectar (personas y vehículos)
        self.clases_objetivo = [
            'person',           # personas
            'car', 'truck', 'bus', 'motorbike', 'bicycle',  # vehículos
            'train', 'boat'     # otros vehículos
        ]
        
        self.cargar_yolo()
        
    def cargar_yolo(self):
        """
        Carga el modelo YOLO. Primero intenta con YOLOv4, luego YOLOv3
        """
        modelos_posibles = [
            {
                'weights': 'yolov4.weights',
                'config': 'yolov4.cfg',
                'names': 'coco.names'
            },
            {
                'weights': 'yolov3.weights', 
                'config': 'yolov3.cfg',
                'names': 'coco.names'
            }
        ]
        
        for modelo in modelos_posibles:
            if self.intentar_cargar_modelo(modelo):
                print(f"Modelo cargado: {modelo['weights']}")
                return
                
        # Si no encuentra modelos, usar detección básica
        print("No se encontraron modelos YOLO. Usando detección básica con Haar Cascades.")
        self.usar_deteccion_basica = True
        self.cargar_haar_cascades()
    
    def intentar_cargar_modelo(self, modelo):
        """
        Intenta cargar un modelo YOLO específico
        """
        try:
            if all(os.path.exists(archivo) for archivo in modelo.values()):
                self.net = cv2.dnn.readNet(modelo['weights'], modelo['config'])
                
                # Cargar nombres de clases
                with open(modelo['names'], 'r') as f:
                    self.classes = [line.strip() for line in f.readlines()]
                
                # Obtener capas de salida
                layer_names = self.net.getLayerNames()
                self.output_layers = [layer_names[i - 1] for i in self.net.getUnconnectedOutLayers().flatten()]
                
                # Colores aleatorios para cada clase
                self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))
                
                self.usar_deteccion_basica = False
                return True
        except Exception as e:
            print(f"Error cargando {modelo['weights']}: {e}")
        return False
    
    def cargar_haar_cascades(self):
        """
        Carga detectores Haar como alternativa básica
        """
        try:
            self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            self.body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
            print("Detectores Haar cargados (detección básica de personas)")
        except:
            print("Error cargando detectores Haar")
            self.usar_deteccion_basica = False
    
    def detectar_con_yolo(self, frame):
        """
        Detecta objetos usando YOLO
        """
        height, width, channels = frame.shape
        
        # Preparar imagen para YOLO
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)
        
        # Información de detecciones
        class_ids = []
        confidences = []
        boxes = []
        
        # Procesar detecciones
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                # Solo considerar detecciones con alta confianza de nuestras clases objetivo
                if confidence > 0.3 and self.classes[class_id] in self.clases_objetivo:
                    # Coordenadas del objeto
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    
                    # Coordenadas del rectángulo
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        
        # Aplicar supresión de máximos no locales
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.4)
        
        # Dibujar detecciones
        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                confidence = confidences[i]
                color = self.colors[class_ids[i]]
                
                # Dibujar rectángulo y etiqueta
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        return frame
    
    def detectar_con_haar(self, frame):
        """
        Detección básica usando Haar Cascades (solo personas)
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detectar caras
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, "Persona (cara)", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # Detectar cuerpos completos
        bodies = self.body_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Persona (cuerpo)", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        return frame
    
    def crear_carpeta_capturas(self):
        """
        Crear carpeta capturas si no existe
        """
        try:
            if not os.path.exists('capturas'):
                os.makedirs('capturas')
                print("Carpeta 'capturas' creada")
            return True
        except Exception as e:
            print(f"Error al crear carpeta capturas: {e}")
            return False
    
    def capturar_y_detectar(self):
        """
        Función principal de captura y detección en tiempo real
        """
        self.crear_carpeta_capturas()
        
        print("\n=== DETECTOR DE PERSONAS Y VEHÍCULOS ===")
        print("Controles:")
        print("- 'q' o ESC: Salir")
        print("- 's': Guardar captura con detecciones")
        print("- 'c': Cambiar entre detección completa y solo conteo")
        
        mostrar_detecciones = True
        
        while True:
            # Capturar pantalla
            screenshot = ImageGrab.grab()
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            # Aplicar detección
            if hasattr(self, 'usar_deteccion_basica') and self.usar_deteccion_basica:
                frame_detectado = self.detectar_con_haar(frame.copy())
            else:
                frame_detectado = self.detectar_con_yolo(frame.copy())
            
            # Redimensionar si es muy grande
            height, width = frame_detectado.shape[:2]
            if width > 1200:
                scale = 1200 / width
                new_width = int(width * scale)
                new_height = int(height * scale)
                frame_detectado = cv2.resize(frame_detectado, (new_width, new_height))
            
            # Mostrar resultado
            window_title = "Detección de Personas y Vehículos"
            cv2.imshow(window_title, frame_detectado)
            
            # Manejar teclas
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # Salir
                break
            elif key == ord('s'):  # Guardar
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                archivo = f'capturas{os.sep}deteccion_{timestamp}.png'
                cv2.imwrite(archivo, frame_detectado)
                print(f"Captura guardada: {archivo}")
            
            # Pequeña pausa
            time.sleep(0.01)
        
        cv2.destroyAllWindows()

def descargar_modelos_yolo():
    """
    Función auxiliar para descargar modelos YOLO si no existen
    """
    print("\n=== DESCARGA DE MODELOS YOLO ===")
    print("Para mejor detección, descarga estos archivos:")
    print("\nYOLOv4 (recomendado):")
    print("1. yolov4.weights - https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights")
    print("2. yolov4.cfg - https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg")
    print("3. coco.names - https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/coco.names")
    print("\nO YOLOv3:")
    print("1. yolov3.weights - https://pjreddie.com/media/files/yolov3.weights")
    print("2. yolov3.cfg - https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg")
    print("3. coco.names - https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names")
    print("\nColoca estos archivos en la misma carpeta que el script.")
    print("Sin estos archivos, se usará detección básica (solo personas).")

if __name__ == "__main__":
    print("=== DETECTOR DE PERSONAS Y VEHÍCULOS ===")
    
    # Verificar si existen modelos YOLO
    archivos_yolo = ['yolov4.weights', 'yolov4.cfg', 'yolov3.weights', 'yolov3.cfg', 'coco.names']
    if not any(os.path.exists(archivo) for archivo in archivos_yolo):
        respuesta = input("¿Quieres ver las instrucciones para descargar modelos YOLO? (y/n): ")
        if respuesta.lower() == 'y':
            descargar_modelos_yolo()
        
        input("\nPresiona Enter para continuar con detección básica...")
    
    # Iniciar detector
    detector = DetectorTiempoReal()
    
    print("\nIniciando en 3 segundos...")
    time.sleep(3)
    
    detector.capturar_y_detectar()