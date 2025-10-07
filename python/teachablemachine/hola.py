from tensorflow.keras.models import load_model
import cv2
import numpy as np

# --- Configuración ---
MODEL_PATH = "keras_Model.h5"
LABELS_PATH = "labels.txt"
CAMERA_ID = 0  # 0 o 1 según la cámara

# Desactivar notación científica en NumPy
np.set_printoptions(suppress=True)

# --- Cargar modelo y etiquetas ---
model = load_model(MODEL_PATH, compile=False)
with open(LABELS_PATH, "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# --- Inicializar cámara ---
camera = cv2.VideoCapture(CAMERA_ID)
if not camera.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

# --- Bucle principal ---
while True:
    ret, frame = camera.read()
    if not ret:
        print("Error al capturar imagen de la cámara.")
        break

    # Redimensionar imagen a 224x224
    img_resized = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

    # Preparar imagen para el modelo
    img_array = np.asarray(img_resized, dtype=np.float32).reshape(1, 224, 224, 3)
    img_array = (img_array / 127.5) - 1  # Normalizar a [-1, 1]

    # Hacer predicción
    prediction = model.predict(img_array)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # --- Mostrar predicción sobre la imagen ---
    text = f"{class_name}: {confidence_score*100:.1f}%"
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow("Webcam Image", frame)

    # --- Imprimir en consola ---
    print(f"Class: {class_name} | Confidence: {confidence_score*100:.1f}%")

    # Salir al presionar ESC
    if cv2.waitKey(1) == 27:
        break

# --- Liberar recursos ---
camera.release()
cv2.destroyAllWindows()
