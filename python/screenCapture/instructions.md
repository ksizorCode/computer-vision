# Instrucciones para que este modelo funcine:

En este ejemplo se utiliza YOLO como sistema de detección de personas, un modelo ya preentenado que tendrás que descargargarte en tu plataforma y meterlo junto al script que se va a ajecutar. Es decir, metelo en este carpeta. El motivo por el que no se encuentra ya aquí es debido a su peso (más de 100MB), Github no permite almacenarlo.


=== DESCARGA DE MODELOS YOLO ===
Para mejor detección, descarga estos archivos:

YOLOv4 (recomendado):
1. yolov4.weights - https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
2. yolov4.cfg - https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4.cfg
3. coco.names - https://raw.githubusercontent.com/AlexeyAB/darknet/master/data/coco.names

O YOLOv3:
1. yolov3.weights - https://pjreddie.com/media/files/yolov3.weights
2. yolov3.cfg - https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg
3. coco.names - https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

Coloca estos archivos en la misma carpeta que el script.
Sin estos archivos, se usará detección básica (solo personas).


