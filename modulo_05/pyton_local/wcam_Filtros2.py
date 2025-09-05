import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
import threading

class RobustColormapGridViewer:
    def __init__(self):
        # Variables de control de webcam
        self.cap = None
        self.frame_available = False
        self.current_frame = None
        self.frame_lock = threading.Lock()
        self.running = True
        
        # Intentar inicializar webcam con diferentes backends
        self.initialize_webcam()
        
        # Colormaps de OpenCV
        self.opencv_colormaps = [
            (cv2.COLORMAP_AUTUMN, "CV_AUTUMN"),
            (cv2.COLORMAP_BONE, "CV_BONE"),
            (cv2.COLORMAP_JET, "CV_JET"),
            (cv2.COLORMAP_WINTER, "CV_WINTER"),
            (cv2.COLORMAP_RAINBOW, "CV_RAINBOW"),
            (cv2.COLORMAP_OCEAN, "CV_OCEAN"),
            (cv2.COLORMAP_SUMMER, "CV_SUMMER"),
            (cv2.COLORMAP_SPRING, "CV_SPRING"),
            (cv2.COLORMAP_COOL, "CV_COOL"),
            (cv2.COLORMAP_HSV, "CV_HSV"),
            (cv2.COLORMAP_PINK, "CV_PINK"),
            (cv2.COLORMAP_HOT, "CV_HOT"),
            (cv2.COLORMAP_PARULA, "CV_PARULA"),
            (cv2.COLORMAP_MAGMA, "CV_MAGMA"),
            (cv2.COLORMAP_INFERNO, "CV_INFERNO"),
            (cv2.COLORMAP_PLASMA, "CV_PLASMA"),
            (cv2.COLORMAP_VIRIDIS, "CV_VIRIDIS"),
            (cv2.COLORMAP_CIVIDIS, "CV_CIVIDIS"),
            (cv2.COLORMAP_TWILIGHT, "CV_TWILIGHT"),
            (cv2.COLORMAP_TURBO, "CV_TURBO")
        ]
        
        # Colormaps de matplotlib
        self.matplotlib_colormaps = [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain',
            'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
            'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
            'turbo', 'nipy_spectral', 'gist_ncar', 'tab10', 'tab20',
            'Set1', 'Set2', 'Set3', 'Pastel1', 'Pastel2', 'Paired',
            'Accent', 'Dark2', 'seismic', 'coolwarm', 'bwr',
            'copper', 'gray', 'bone', 'pink', 'spring', 'summer',
            'autumn', 'winter', 'cool', 'hot', 'afmhot', 'gist_heat'
        ]
        
        # Combinar colormaps
        self.all_colormaps = []
        
        # Añadir OpenCV
        for cv_map, name in self.opencv_colormaps:
            self.all_colormaps.append(('opencv', cv_map, name))
        
        # Añadir matplotlib (verificar disponibilidad)
        for mpl_name in self.matplotlib_colormaps:
            try:
                plt.get_cmap(mpl_name)
                self.all_colormaps.append(('matplotlib', mpl_name, f"MPL_{mpl_name.upper()}"))
            except:
                continue
        
        # Configuración de interfaz
        self.grid_cols = 8
        self.grid_rows = math.ceil(len(self.all_colormaps) / self.grid_cols)
        self.cell_width = 150
        self.cell_height = 120
        self.padding = 8
        self.window_width = self.grid_cols * self.cell_width + (self.grid_cols + 1) * self.padding
        self.window_height = self.grid_rows * self.cell_height + (self.grid_rows + 1) * self.padding + 100
        
        # Variables de control
        self.brightness = 0
        self.contrast = 100
        self.selected_colormap = -1
        self.current_category = 'all'
        self.use_demo_image = False
        
        # Crear imagen de demostración
        self.demo_image = self.create_demo_image()
        
        print(f"✅ Cargados {len(self.all_colormaps)} colormaps:")
        print(f"   - OpenCV: {len(self.opencv_colormaps)}")
        print(f"   - Matplotlib: {len([x for x in self.all_colormaps if x[0] == 'matplotlib'])}")
        
        # Iniciar hilo de captura de frames
        if self.cap and self.cap.isOpened():
            self.capture_thread = threading.Thread(target=self.capture_frames)
            self.capture_thread.daemon = True
            self.capture_thread.start()
            print("📹 Webcam inicializada correctamente")
        else:
            print("⚠️  Usando imagen de demostración (webcam no disponible)")
            self.use_demo_image = True
        
        self.print_controls()
    
    def initialize_webcam(self):
        """Inicializa la webcam probando diferentes backends"""
        backends = [
            (cv2.CAP_DSHOW, "DirectShow"),
            (cv2.CAP_MSMF, "Media Foundation"),
            (cv2.CAP_V4L2, "Video4Linux"),
            (cv2.CAP_ANY, "Default")
        ]
        
        for backend, name in backends:
            try:
                print(f"🔍 Probando backend {name}...")
                cap = cv2.VideoCapture(0, backend)
                
                if cap.isOpened():
                    # Configurar propiedades para estabilidad
                    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                    cap.set(cv2.CAP_PROP_FPS, 15)  # FPS más bajo para estabilidad
                    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
                    
                    # Probar captura
                    ret, frame = cap.read()
                    if ret and frame is not None:
                        print(f"✅ Backend {name} funcionando")
                        self.cap = cap
                        return
                    else:
                        cap.release()
                        
            except Exception as e:
                print(f"❌ Backend {name} falló: {e}")
                continue
        
        print("⚠️  No se pudo inicializar ninguna webcam")
        self.cap = None
    
    def create_demo_image(self):
        """Crea una imagen de demostración con gradientes y patrones"""
        img = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # Gradiente horizontal
        for x in range(640):
            img[:, x] = [x * 255 // 640, 128, 255 - (x * 255 // 640)]
        
        # Añadir círculos concéntricos
        center = (320, 240)
        for radius in range(50, 200, 30):
            cv2.circle(img, center, radius, (255, 255, 255), 2)
        
        # Añadir texto
        cv2.putText(img, "DEMO IMAGE", (250, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(img, "Webcam not available", (200, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 1)
        
        return img
    
    def capture_frames(self):
        """Captura frames en un hilo separado para evitar bloqueos"""
        consecutive_failures = 0
        max_failures = 10
        
        while self.running and self.cap and self.cap.isOpened():
            try:
                ret, frame = self.cap.read()
                
                if ret and frame is not None:
                    with self.frame_lock:
                        self.current_frame = frame.copy()
                        self.frame_available = True
                    consecutive_failures = 0
                else:
                    consecutive_failures += 1
                    if consecutive_failures > max_failures:
                        print("⚠️  Demasiados fallos de captura, cambiando a modo demo")
                        self.use_demo_image = True
                        break
                
                time.sleep(0.033)  # ~30 FPS
                
            except Exception as e:
                consecutive_failures += 1
                print(f"Error en captura: {e}")
                if consecutive_failures > max_failures:
                    self.use_demo_image = True
                    break
                time.sleep(0.1)
    
    def get_current_frame(self):
        """Obtiene el frame actual de forma segura"""
        if self.use_demo_image:
            return self.demo_image.copy()
        
        with self.frame_lock:
            if self.frame_available and self.current_frame is not None:
                return self.current_frame.copy()
            else:
                return self.demo_image.copy()
    
    def matplotlib_colormap_to_opencv(self, gray_image, colormap_name):
        """Convierte colormap de matplotlib a formato OpenCV"""
        try:
            cmap = plt.get_cmap(colormap_name)
            normalized = gray_image.astype(np.float32) / 255.0
            colored = cmap(normalized)
            colored_bgr = colored[:, :, [2, 1, 0]]
            return (colored_bgr * 255).astype(np.uint8)
        except Exception as e:
            return cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
    
    def adjust_image(self, frame):
        """Ajusta brillo y contraste"""
        alpha = self.contrast / 100.0
        beta = self.brightness
        return cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    
    def apply_colormap_to_frame(self, frame, colormap_info):
        """Aplica colormap al frame"""
        colormap_type, colormap_data, _ = colormap_info
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        if colormap_type == 'opencv':
            return cv2.applyColorMap(gray, colormap_data)
        elif colormap_type == 'matplotlib':
            return self.matplotlib_colormap_to_opencv(gray, colormap_data)
        else:
            return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    def get_filtered_colormaps(self):
        """Filtra colormaps según categoría"""
        if self.current_category == 'opencv':
            return [(f'opencv', cv_map, name) for cv_map, name in self.opencv_colormaps]
        elif self.current_category == 'matplotlib':
            return [x for x in self.all_colormaps if x[0] == 'matplotlib']
        else:
            return self.all_colormaps
    
    def create_grid_display(self, original_frame):
        """Crea la retícula de colormaps"""
        current_colormaps = self.get_filtered_colormaps()
        current_rows = math.ceil(len(current_colormaps) / self.grid_cols)
        current_height = max(current_rows * self.cell_height + (current_rows + 1) * self.padding + 100, 500)
        
        grid_image = np.zeros((current_height, self.window_width, 3), dtype=np.uint8)
        grid_image.fill(25)
        
        # Título y información
        category_text = {
            'all': 'TODOS LOS COLORMAPS',
            'opencv': 'OPENCV COLORMAPS', 
            'matplotlib': 'MATPLOTLIB COLORMAPS'
        }
        
        cv2.putText(grid_image, f"COLORMAP VIEWER - {category_text[self.current_category]}", 
                   (20, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Estado de la webcam
        status_color = (0, 255, 0) if not self.use_demo_image else (255, 165, 0)
        status_text = "WEBCAM ACTIVA" if not self.use_demo_image else "MODO DEMO"
        cv2.putText(grid_image, status_text, (self.window_width - 200, 25), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, status_color, 1)
        
        info_text = f"Total: {len(current_colormaps)} | Brillo: {self.brightness:+d} | Contraste: {self.contrast}%"
        cv2.putText(grid_image, info_text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        
        controls_text = "1:OpenCV | 2:Matplotlib | 3:Todos | D:Demo | +/-:Brillo | C/V:Contraste | ESC:Salir"
        cv2.putText(grid_image, controls_text, (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (150, 150, 150), 1)
        
        # Redimensionar frame
        try:
            resized_frame = cv2.resize(original_frame, (self.cell_width - 15, self.cell_height - 25))
        except:
            resized_frame = cv2.resize(self.demo_image, (self.cell_width - 15, self.cell_height - 25))
        
        # Crear celdas
        for i, colormap_info in enumerate(current_colormaps):
            row = i // self.grid_cols
            col = i % self.grid_cols
            
            x = col * self.cell_width + (col + 1) * self.padding
            y = row * self.cell_height + (row + 1) * self.padding + 85
            
            if y + self.cell_height > grid_image.shape[0]:
                break
            
            try:
                colormap_frame = self.apply_colormap_to_frame(resized_frame, colormap_info)
                
                is_selected = (i == self.selected_colormap)
                border_color = (0, 255, 255) if is_selected else (80, 80, 80)
                border_thickness = 2 if is_selected else 1
                
                cv2.rectangle(grid_image, (x-1, y-1), 
                             (x + self.cell_width + 1, y + self.cell_height + 1), 
                             border_color, border_thickness)
                
                # Insertar imagen de forma segura
                h, w = colormap_frame.shape[:2]
                end_y = min(y + 5 + h, grid_image.shape[0])
                end_x = min(x + 8 + w, grid_image.shape[1])
                
                grid_image[y+5:end_y, x+8:end_x] = colormap_frame[:end_y-y-5, :end_x-x-8]
                
                # Nombre del colormap
                _, _, name = colormap_info
                display_name = name[:12] + "..." if len(name) > 15 else name
                text_color = (100, 255, 100) if colormap_info[0] == 'opencv' else (255, 150, 100)
                
                cv2.putText(grid_image, display_name, (x + 8, y + self.cell_height - 6), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.3, text_color, 1)
                
            except Exception as e:
                # Celda de error
                cv2.rectangle(grid_image, (x, y), (x + self.cell_width, y + self.cell_height), 
                             (50, 50, 50), -1)
                cv2.putText(grid_image, "ERROR", (x + 40, y + 60), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        
        return grid_image
    
    def handle_mouse_click(self, event, x, y, flags, param):
        """Maneja clicks del mouse"""
        if event == cv2.EVENT_LBUTTONDOWN:
            adjusted_y = y - 85
            if adjusted_y > 0:
                col = (x - self.padding) // (self.cell_width + self.padding)
                row = (adjusted_y - self.padding) // (self.cell_height + self.padding)
                
                current_colormaps = self.get_filtered_colormaps()
                
                if 0 <= col < self.grid_cols and 0 <= row < math.ceil(len(current_colormaps) / self.grid_cols):
                    cell_index = row * self.grid_cols + col
                    if cell_index < len(current_colormaps):
                        self.selected_colormap = cell_index if cell_index != self.selected_colormap else -1
                        if self.selected_colormap != -1:
                            _, _, name = current_colormaps[cell_index]
                            print(f"✅ Seleccionado: {name}")
    
    def print_controls(self):
        """Imprime controles disponibles"""
        print("\n🎮 CONTROLES DISPONIBLES:")
        print("=" * 40)
        print("1, 2, 3    - Cambiar categoría de colormaps")
        print("D          - Activar/desactivar modo demo")
        print("+/-        - Ajustar brillo")
        print("C/V        - Ajustar contraste") 
        print("R          - Reset valores")
        print("ESPACIO    - Captura de pantalla")
        print("Click      - Seleccionar colormap")
        print("ESC        - Salir")
        print("=" * 40)
    
    def run(self):
        """Ejecuta la aplicación principal"""
        cv2.namedWindow('Robust Colormap Viewer', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('Robust Colormap Viewer', self.handle_mouse_click)
        
        cv2.namedWindow('Selected View', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Selected View', 500, 400)
        
        print("🎨 Robust Colormap Viewer iniciado")
        
        frame_count = 0
        
        try:
            while True:
                frame_count += 1
                
                # Obtener frame actual
                current_frame = self.get_current_frame()
                adjusted_frame = self.adjust_image(current_frame)
                
                # Crear visualización
                grid_display = self.create_grid_display(adjusted_frame)
                cv2.imshow('Robust Colormap Viewer', grid_display)
                
                # Vista seleccionada
                current_colormaps = self.get_filtered_colormaps()
                
                if self.selected_colormap != -1 and self.selected_colormap < len(current_colormaps):
                    colormap_info = current_colormaps[self.selected_colormap]
                    large_frame = cv2.resize(adjusted_frame, (480, 360))
                    selected_display = self.apply_colormap_to_frame(large_frame, colormap_info)
                    
                    _, _, name = colormap_info
                    cv2.putText(selected_display, f"COLORMAP: {name}", 
                               (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                    cv2.putText(selected_display, f"Tipo: {colormap_info[0].upper()}", 
                               (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
                    
                    cv2.imshow('Selected View', selected_display)
                else:
                    original_large = cv2.resize(adjusted_frame, (480, 360))
                    cv2.putText(original_large, "ORIGINAL - Click para seleccionar", 
                               (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                    cv2.imshow('Selected View', original_large)
                
                # Manejar teclas
                key = cv2.waitKey(30) & 0xFF  # Tiempo de espera más largo
                
                if key == 27:  # ESC
                    break
                elif key == ord('1'):
                    self.current_category = 'opencv'
                    self.selected_colormap = -1
                    print("📊 Mostrando colormaps de OpenCV")
                elif key == ord('2'):
                    self.current_category = 'matplotlib'
                    self.selected_colormap = -1
                    print("📊 Mostrando colormaps de Matplotlib")
                elif key == ord('3'):
                    self.current_category = 'all'
                    self.selected_colormap = -1
                    print("📊 Mostrando todos los colormaps")
                elif key == ord('d') or key == ord('D'):
                    self.use_demo_image = not self.use_demo_image
                    status = "ACTIVADO" if self.use_demo_image else "DESACTIVADO"
                    print(f"🖼️  Modo demo {status}")
                elif key == ord('+') or key == ord('='):
                    self.brightness = min(50, self.brightness + 5)
                    print(f"☀️ Brillo: {self.brightness}")
                elif key == ord('-'):
                    self.brightness = max(-50, self.brightness - 5)
                    print(f"🌙 Brillo: {self.brightness}")
                elif key == ord('c'):
                    self.contrast = min(200, self.contrast + 10)
                    print(f"🔆 Contraste: {self.contrast}%")
                elif key == ord('v'):
                    self.contrast = max(50, self.contrast - 10)
                    print(f"🔅 Contraste: {self.contrast}%")
                elif key == ord('r'):
                    self.brightness = 0
                    self.contrast = 100
                    self.selected_colormap = -1
                    print("🔄 Valores reseteados")
                elif key == ord(' '):
                    filename = f"colormap_capture_{int(time.time())}.jpg"
                    cv2.imwrite(filename, grid_display)
                    print(f"📸 Captura guardada: {filename}")
        
        except KeyboardInterrupt:
            print("\n⚠️  Interrupción por teclado")
        except Exception as e:
            print(f"❌ Error durante ejecución: {e}")
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Limpia recursos"""
        self.running = False
        
        if self.cap:
            self.cap.release()
        
        cv2.destroyAllWindows()
        print("🧹 Recursos liberados")
        print("👋 Robust Colormap Viewer cerrado")

# Ejecutar aplicación
if __name__ == "__main__":
    try:
        app = RobustColormapGridViewer()
        app.run()
    except Exception as e:
        print(f"❌ Error fatal: {e}")
        print("\n💡 Soluciones sugeridas:")
        print("1. Instalar dependencias: pip install opencv-python matplotlib numpy")
        print("2. Verificar que la webcam no esté en uso por otra aplicación")
        print("3. Ejecutar como administrador si es necesario")
        print("4. Usar modo demo presionando 'D' si la webcam falla")