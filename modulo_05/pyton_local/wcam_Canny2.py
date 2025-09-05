import cv2
import numpy as np

# Inicializa la webcam
cap = cv2.VideoCapture(0)

# Variable para cambiar entre filtros
current_filter = 0
num_filters = 12

print("Controles:")
print("Presiona ESPACIO para cambiar filtro")
print("Presiona 'q' para salir")
print("Filtros disponibles: Original, Canny, Blur, Sepia, Negativo, Cartoon, Vintage, Neon, Thermal, Psychedelic, Oil Paint, Emboss")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Copia del frame original
    processed_frame = frame.copy()
    
    if current_filter == 0:  # Original
        filter_name = "Original"
        processed_frame = frame
        
    elif current_filter == 1:  # Canny
        filter_name = "Canny Edge Detection"
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        processed_frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
    elif current_filter == 2:  # Blur artístico
        filter_name = "Artistic Blur"
        processed_frame = cv2.bilateralFilter(frame, 15, 80, 80)
        processed_frame = cv2.medianBlur(processed_frame, 19)
        
    elif current_filter == 3:  # Sepia
        filter_name = "Sepia"
        sepia_kernel = np.array([[0.272, 0.534, 0.131],
                                [0.349, 0.686, 0.168],
                                [0.393, 0.769, 0.189]])
        processed_frame = cv2.transform(frame, sepia_kernel)
        processed_frame = np.clip(processed_frame, 0, 255).astype(np.uint8)
        
    elif current_filter == 4:  # Negativo
        filter_name = "Negative"
        processed_frame = 255 - frame
        
    elif current_filter == 5:  # Cartoon
        filter_name = "Cartoon"
        # Reducir ruido
        bilateral = cv2.bilateralFilter(frame, 15, 40, 40)
        # Detectar bordes
        gray = cv2.cvtColor(bilateral, cv2.COLOR_BGR2GRAY)
        gray_blur = cv2.medianBlur(gray, 7)
        edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        # Combinar
        processed_frame = cv2.bitwise_and(bilateral, edges)
        
    elif current_filter == 6:  # Vintage con colormap
        filter_name = "Vintage Thermal"
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Aplicar colormap AUTUMN para efecto vintage cálido
        processed_frame = cv2.applyColorMap(gray, cv2.COLORMAP_AUTUMN)
        # Añadir viñeta
        rows, cols = gray.shape
        kernel_x = cv2.getGaussianKernel(cols, 200)
        kernel_y = cv2.getGaussianKernel(rows, 200)
        kernel = kernel_y * kernel_x.T
        mask = 255 * kernel / np.linalg.norm(kernel)
        mask = mask.astype(np.uint8)
        mask = cv2.merge([mask, mask, mask])
        processed_frame = cv2.multiply(processed_frame, mask, scale=1/255)
        
    elif current_filter == 7:  # Neon
        filter_name = "Neon Glow"
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        # Aplicar colormap HOT para efecto neon
        processed_frame = cv2.applyColorMap(edges, cv2.COLORMAP_HOT)
        
    elif current_filter == 8:  # Thermal
        filter_name = "Thermal Vision"
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Colormap JET para efecto thermal
        processed_frame = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
        
    elif current_filter == 9:  # Psychedelic
        filter_name = "Psychedelic"
        # Separar canales y mezclarlos de forma creativa
        b, g, r = cv2.split(frame)
        # Crear efectos psicodélicos rotando los canales
        processed_frame = cv2.merge([r, b, g])
        # Aplicar colormap RAINBOW
        gray = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2GRAY)
        rainbow = cv2.applyColorMap(gray, cv2.COLORMAP_RAINBOW)
        processed_frame = cv2.addWeighted(processed_frame, 0.6, rainbow, 0.4, 0)
        
    elif current_filter == 10:  # Oil Paint Effect
        filter_name = "Oil Paint"
        # Efecto pintura al óleo usando bilateralFilter múltiple
        processed_frame = frame.copy()
        for _ in range(3):
            processed_frame = cv2.bilateralFilter(processed_frame, 9, 200, 200)
        # Añadir colormap SUMMER para tonos cálidos
        gray = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2GRAY)
        summer = cv2.applyColorMap(gray, cv2.COLORMAP_SUMMER)
        processed_frame = cv2.addWeighted(processed_frame, 0.8, summer, 0.2, 0)
        
    elif current_filter == 11:  # Emboss
        filter_name = "Emboss 3D"
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Kernel para efecto emboss
        kernel = np.array([[-2, -1, 0],
                          [-1, 1, 1],
                          [0, 1, 2]], dtype=np.float32)
        emboss = cv2.filter2D(gray, -1, kernel)
        emboss = emboss + 128  # Añadir offset para visualización
        emboss = np.clip(emboss, 0, 255).astype(np.uint8)
        # Aplicar colormap BONE para efecto 3D
        processed_frame = cv2.applyColorMap(emboss, cv2.COLORMAP_BONE)
    
    # Añadir texto con el nombre del filtro
    cv2.putText(processed_frame, f"Filtro: {filter_name}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(processed_frame, f"Filtro {current_filter + 1}/{num_filters}", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(processed_frame, "ESPACIO: Cambiar | Q: Salir", (10, frame.shape[0] - 20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
    
    # Mostrar el frame procesado
    cv2.imshow('Filtros Webcam', processed_frame)
    
    # Controles
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord(' '):  # Espacio para cambiar filtro
        current_filter = (current_filter + 1) % num_filters
        print(f"Cambiando a filtro: {filter_name}")

cap.release()
cv2.destroyAllWindows()