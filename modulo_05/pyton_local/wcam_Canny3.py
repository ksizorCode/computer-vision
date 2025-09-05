import cv2
import numpy as np

class WebcamFilterApp:
    def __init__(self):
        # Inicializar webcam
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise Exception("No se pudo abrir la webcam")
        
        # Variables de control
        self.current_filter = 0
        self.filter_names = [
            "Original", "Canny", "Blur", "Sepia", "Negativo", 
            "Cartoon", "Vintage", "Neon", "Thermal", "HSV", 
            "Emboss", "Sharpen"
        ]
        
        # Parámetros ajustables
        self.brightness = 0
        self.contrast = 100
        self.saturation = 100
        self.blur_intensity = 1
        self.edge_threshold1 = 100
        self.edge_threshold2 = 200
        self.colormap_type = 2  # JET por defecto
        
        # Lista de colormaps disponibles
        self.colormaps = [
            cv2.COLORMAP_AUTUMN, cv2.COLORMAP_BONE, cv2.COLORMAP_JET,
            cv2.COLORMAP_WINTER, cv2.COLORMAP_RAINBOW, cv2.COLORMAP_OCEAN,
            cv2.COLORMAP_SUMMER, cv2.COLORMAP_SPRING, cv2.COLORMAP_COOL,
            cv2.COLORMAP_HOT, cv2.COLORMAP_PINK, cv2.COLORMAP_HSV
        ]
        
        self.colormap_names = [
            "Autumn", "Bone", "Jet", "Winter", "Rainbow", "Ocean",
            "Summer", "Spring", "Cool", "Hot", "Pink", "HSV"
        ]
        
        # Estado de grabación
        self.recording = False
        self.video_writer = None
        
        self.setup_ui()
    
    def setup_ui(self):
        """Configura la interfaz de usuario con trackbars"""
        # Crear ventana principal
        cv2.namedWindow('Webcam Filters Pro', cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow('Controls', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Controls', 400, 600)
        
        # Trackbars para filtros generales
        cv2.createTrackbar('Filtro', 'Controls', 0, len(self.filter_names)-1, self.on_filter_change)
        cv2.createTrackbar('Brillo', 'Controls', 50, 100, self.on_brightness_change)
        cv2.createTrackbar('Contraste', 'Controls', 100, 200, self.on_contrast_change)
        cv2.createTrackbar('Saturacion', 'Controls', 100, 200, self.on_saturation_change)
        
        # Trackbars para efectos específicos
        cv2.createTrackbar('Blur', 'Controls', 1, 31, self.on_blur_change)
        cv2.createTrackbar('Canny Min', 'Controls', 100, 300, self.on_edge1_change)
        cv2.createTrackbar('Canny Max', 'Controls', 200, 400, self.on_edge2_change)
        cv2.createTrackbar('ColorMap', 'Controls', 2, len(self.colormaps)-1, self.on_colormap_change)
        
        # Crear imagen de controles con botones simulados
        self.create_control_panel()
    
    def create_control_panel(self):
        """Crea un panel de control visual"""
        control_img = np.zeros((200, 400, 3), dtype=np.uint8)
        
        # Título
        cv2.putText(control_img, 'WEBCAM FILTERS PRO', (80, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        
        # Información de controles
        instructions = [
            "CONTROLES:",
            "R - Iniciar/Parar grabacion",
            "S - Captura de pantalla", 
            "ESPACIO - Siguiente filtro",
            "ESC - Salir",
            "",
            f"Filtro actual: {self.filter_names[self.current_filter]}",
            f"ColorMap: {self.colormap_names[self.colormap_type]}"
        ]
        
        y_offset = 60
        for i, text in enumerate(instructions):
            color = (0, 255, 0) if i < 5 else (255, 255, 255)
            if i == 6:  # Filtro actual
                color = (0, 255, 255)
            cv2.putText(control_img, text, (10, y_offset + i*15), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
        
        cv2.imshow('Controls', control_img)
    
    # Callbacks para trackbars
    def on_filter_change(self, val):
        self.current_filter = val
        self.create_control_panel()
    
    def on_brightness_change(self, val):
        self.brightness = val - 50  # Rango -50 a +50
    
    def on_contrast_change(self, val):
        self.contrast = val
    
    def on_saturation_change(self, val):
        self.saturation = val
    
    def on_blur_change(self, val):
        self.blur_intensity = max(1, val)
        if self.blur_intensity % 2 == 0:
            self.blur_intensity += 1
    
    def on_edge1_change(self, val):
        self.edge_threshold1 = val
    
    def on_edge2_change(self, val):
        self.edge_threshold2 = val
    
    def on_colormap_change(self, val):
        self.colormap_type = val
        self.create_control_panel()
    
    def adjust_brightness_contrast(self, frame):
        """Ajusta brillo y contraste"""
        alpha = self.contrast / 100.0  # Factor de contraste
        beta = self.brightness  # Brillo
        return cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    
    def adjust_saturation(self, frame):
        """Ajusta saturación"""
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv[:, :, 1] = hsv[:, :, 1] * (self.saturation / 100.0)
        hsv[:, :, 1] = np.clip(hsv[:, :, 1], 0, 255)
        return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    def apply_filter(self, frame):
        """Aplica el filtro seleccionado"""
        filter_idx = self.current_filter
        
        if filter_idx == 0:  # Original
            return frame
        
        elif filter_idx == 1:  # Canny
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, self.edge_threshold1, self.edge_threshold2)
            return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
        elif filter_idx == 2:  # Blur
            return cv2.GaussianBlur(frame, (self.blur_intensity, self.blur_intensity), 0)
        
        elif filter_idx == 3:  # Sepia
            sepia_kernel = np.array([[0.272, 0.534, 0.131],
                                    [0.349, 0.686, 0.168],
                                    [0.393, 0.769, 0.189]])
            sepia = cv2.transform(frame, sepia_kernel)
            return np.clip(sepia, 0, 255).astype(np.uint8)
        
        elif filter_idx == 4:  # Negativo
            return 255 - frame
        
        elif filter_idx == 5:  # Cartoon
            bilateral = cv2.bilateralFilter(frame, 15, 40, 40)
            gray = cv2.cvtColor(bilateral, cv2.COLOR_BGR2GRAY)
            gray_blur = cv2.medianBlur(gray, 7)
            edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                        cv2.THRESH_BINARY, 7, 7)
            edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            return cv2.bitwise_and(bilateral, edges)
        
        elif filter_idx == 6:  # Vintage
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return cv2.applyColorMap(gray, self.colormaps[self.colormap_type])
        
        elif filter_idx == 7:  # Neon
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 50, 150)
            return cv2.applyColorMap(edges, cv2.COLORMAP_HOT)
        
        elif filter_idx == 8:  # Thermal
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return cv2.applyColorMap(gray, self.colormaps[self.colormap_type])
        
        elif filter_idx == 9:  # HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            return cv2.applyColorMap(hsv[:,:,0], self.colormaps[self.colormap_type])
        
        elif filter_idx == 10:  # Emboss
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]], dtype=np.float32)
            emboss = cv2.filter2D(gray, -1, kernel) + 128
            emboss = np.clip(emboss, 0, 255).astype(np.uint8)
            return cv2.applyColorMap(emboss, cv2.COLORMAP_BONE)
        
        elif filter_idx == 11:  # Sharpen
            kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            return cv2.filter2D(frame, -1, kernel)
        
        return frame
    
    def add_ui_overlay(self, frame):
        """Añade información de overlay"""
        h, w = frame.shape[:2]
        
        # Fondo semi-transparente para el texto
        overlay = frame.copy()
        cv2.rectangle(overlay, (10, 10), (400, 120), (0, 0, 0), -1)
        frame = cv2.addWeighted(frame, 0.8, overlay, 0.2, 0)
        
        # Información del filtro
        cv2.putText(frame, f"Filtro: {self.filter_names[self.current_filter]}", 
                   (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(frame, f"ColorMap: {self.colormap_names[self.colormap_type]}", 
                   (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Parámetros actuales
        cv2.putText(frame, f"Brillo: {self.brightness} | Contraste: {self.contrast}%", 
                   (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        cv2.putText(frame, f"Saturacion: {self.saturation}% | Blur: {self.blur_intensity}", 
                   (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        
        # Estado de grabación
        if self.recording:
            cv2.circle(frame, (w-30, 30), 10, (0, 0, 255), -1)
            cv2.putText(frame, "REC", (w-60, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        
        return frame
    
    def start_recording(self, frame_width, frame_height):
        """Inicia la grabación de video"""
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.video_writer = cv2.VideoWriter('webcam_output.avi', fourcc, 20.0, 
                                          (frame_width, frame_height))
        self.recording = True
        print("📹 Grabación iniciada - webcam_output.avi")
    
    def stop_recording(self):
        """Detiene la grabación"""
        if self.video_writer:
            self.video_writer.release()
            self.video_writer = None
        self.recording = False
        print("⏹️ Grabación detenida")
    
    def save_screenshot(self, frame):
        """Guarda una captura de pantalla"""
        filename = f"screenshot_{cv2.getTickCount()}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Captura guardada: {filename}")
    
    def run(self):
        """Ejecuta la aplicación principal"""
        print("🎥 WEBCAM FILTERS PRO - Iniciado")
        print("=" * 40)
        
        frame_count = 0
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            frame_count += 1
            
            # Aplicar ajustes básicos
            frame = self.adjust_brightness_contrast(frame)
            frame = self.adjust_saturation(frame)
            
            # Aplicar filtro seleccionado
            processed_frame = self.apply_filter(frame)
            
            # Añadir overlay de información
            final_frame = self.add_ui_overlay(processed_frame)
            
            # Grabar si está activo
            if self.recording and self.video_writer:
                self.video_writer.write(final_frame)
            
            # Mostrar frame
            cv2.imshow('Webcam Filters Pro', final_frame)
            
            # Manejar teclas
            key = cv2.waitKey(1) & 0xFF
            
            if key == 27:  # ESC
                break
            elif key == ord(' '):  # Espacio - siguiente filtro
                self.current_filter = (self.current_filter + 1) % len(self.filter_names)
                cv2.setTrackbarPos('Filtro', 'Controls', self.current_filter)
            elif key == ord('r') or key == ord('R'):  # Grabación
                if not self.recording:
                    h, w = final_frame.shape[:2]
                    self.start_recording(w, h)
                else:
                    self.stop_recording()
            elif key == ord('s') or key == ord('S'):  # Screenshot
                self.save_screenshot(final_frame)
        
        # Limpiar
        if self.recording:
            self.stop_recording()
        
        self.cap.release()
        cv2.destroyAllWindows()
        print("👋 Aplicación cerrada")

# Ejecutar la aplicación
if __name__ == "__main__":
    try:
        app = WebcamFilterApp()
        app.run()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Asegúrate de que tu webcam esté conectada y disponible")