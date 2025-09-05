import cv2
import numpy as np
import math

class ColormapGridViewer:
    def __init__(self):
        # Inicializar webcam
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise Exception("No se pudo abrir la webcam")
        
        # Todos los colormaps disponibles en OpenCV
        self.colormaps = [
            (cv2.COLORMAP_AUTUMN, "AUTUMN"),
            (cv2.COLORMAP_BONE, "BONE"),
            (cv2.COLORMAP_JET, "JET"),
            (cv2.COLORMAP_WINTER, "WINTER"),
            (cv2.COLORMAP_RAINBOW, "RAINBOW"),
            (cv2.COLORMAP_OCEAN, "OCEAN"),
            (cv2.COLORMAP_SUMMER, "SUMMER"),
            (cv2.COLORMAP_SPRING, "SPRING"),
            (cv2.COLORMAP_COOL, "COOL"),
            (cv2.COLORMAP_HSV, "HSV"),
            (cv2.COLORMAP_PINK, "PINK"),
            (cv2.COLORMAP_HOT, "HOT"),
            (cv2.COLORMAP_PARULA, "PARULA"),
            (cv2.COLORMAP_MAGMA, "MAGMA"),
            (cv2.COLORMAP_INFERNO, "INFERNO"),
            (cv2.COLORMAP_PLASMA, "PLASMA"),
            (cv2.COLORMAP_VIRIDIS, "VIRIDIS"),
            (cv2.COLORMAP_CIVIDIS, "CIVIDIS"),
            (cv2.COLORMAP_TWILIGHT, "TWILIGHT"),
            (cv2.COLORMAP_TWILIGHT_SHIFTED, "TWILIGHT_SHIFTED"),
            (cv2.COLORMAP_TURBO, "TURBO"),
            (cv2.COLORMAP_DEEPGREEN, "DEEPGREEN")
        ]
        
        # Configuración de la retícula
        self.grid_cols = 6  # Columnas en la retícula
        self.grid_rows = math.ceil(len(self.colormaps) / self.grid_cols)
        
        # Tamaño de cada celda en la retícula
        self.cell_width = 200
        self.cell_height = 150
        
        # Espacio entre celdas
        self.padding = 10
        
        # Calcular dimensiones de la ventana completa
        self.window_width = self.grid_cols * self.cell_width + (self.grid_cols + 1) * self.padding
        self.window_height = self.grid_rows * self.cell_height + (self.grid_rows + 1) * self.padding + 60  # +60 para header
        
        # Variables de control
        self.show_original = True
        self.brightness = 0
        self.contrast = 100
        self.selected_colormap = -1  # -1 significa ninguno seleccionado
        
        print(f"Mostrando {len(self.colormaps)} colormaps en retícula {self.grid_rows}x{self.grid_cols}")
        print("Controles:")
        print("- ESPACIO: Mostrar/ocultar original")
        print("- +/-: Ajustar brillo")
        print("- Ctrl +/-: Ajustar contraste")
        print("- Click en celda: Seleccionar colormap")
        print("- ESC: Salir")
    
    def adjust_image(self, frame):
        """Ajusta brillo y contraste de la imagen"""
        alpha = self.contrast / 100.0  # Factor de contraste
        beta = self.brightness  # Brillo
        return cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    
    def apply_colormap_to_frame(self, frame, colormap):
        """Aplica un colormap específico al frame"""
        # Convertir a escala de grises primero
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Aplicar el colormap
        colored = cv2.applyColorMap(gray, colormap)
        return colored
    
    def create_grid_display(self, original_frame):
        """Crea la visualización en retícula con todos los colormaps"""
        # Crear imagen base para la retícula
        grid_image = np.zeros((self.window_height, self.window_width, 3), dtype=np.uint8)
        
        # Fondo gris oscuro
        grid_image.fill(30)
        
        # Título principal
        cv2.putText(grid_image, "COLORMAP VIEWER - TIEMPO REAL", 
                   (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        # Información de controles
        info_text = f"Brillo: {self.brightness:+d} | Contraste: {self.contrast}% | Original: {'ON' if self.show_original else 'OFF'}"
        cv2.putText(grid_image, info_text, 
                   (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
        
        # Redimensionar frame original para las celdas
        resized_frame = cv2.resize(original_frame, (self.cell_width - 20, self.cell_height - 30))
        
        # Crear cada celda de la retícula
        for i, (colormap, name) in enumerate(self.colormaps):
            # Calcular posición en la retícula
            row = i // self.grid_cols
            col = i % self.grid_cols
            
            # Calcular coordenadas de la celda
            x = col * self.cell_width + (col + 1) * self.padding
            y = row * self.cell_height + (row + 1) * self.padding + 60  # +60 para el header
            
            # Aplicar colormap al frame
            colormap_frame = self.apply_colormap_to_frame(resized_frame, colormap)
            
            # Crear borde de la celda
            border_color = (0, 255, 255) if i == self.selected_colormap else (100, 100, 100)
            border_thickness = 3 if i == self.selected_colormap else 1
            
            cv2.rectangle(grid_image, (x-2, y-2), 
                         (x + self.cell_width + 2, y + self.cell_height + 2), 
                         border_color, border_thickness)
            
            # Insertar imagen con colormap
            grid_image[y+5:y+5+colormap_frame.shape[0], 
                      x+10:x+10+colormap_frame.shape[1]] = colormap_frame
            
            # Añadir nombre del colormap
            cv2.putText(grid_image, name, (x + 10, y + self.cell_height - 8), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            
            # Mostrar original en la primera celda si está activado
            if i == 0 and self.show_original:
                # Superponer frame original en esquina superior izquierda
                original_small = cv2.resize(resized_frame, (80, 60))
                grid_image[y+5:y+65, x+10:x+90] = original_small
                cv2.putText(grid_image, "ORIG", (x + 95, y + 40), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)
        
        return grid_image
    
    def handle_mouse_click(self, event, x, y, flags, param):
        """Maneja clicks del mouse para seleccionar colormaps"""
        if event == cv2.EVENT_LBUTTONDOWN:
            # Calcular qué celda fue clickeada
            adjusted_y = y - 60  # Restar el header
            if adjusted_y > 0:
                col = (x - self.padding) // (self.cell_width + self.padding)
                row = (adjusted_y - self.padding) // (self.cell_height + self.padding)
                
                # Verificar que está dentro de los límites
                if 0 <= col < self.grid_cols and 0 <= row < self.grid_rows:
                    cell_index = row * self.grid_cols + col
                    if cell_index < len(self.colormaps):
                        self.selected_colormap = cell_index if cell_index != self.selected_colormap else -1
                        print(f"Seleccionado: {self.colormaps[cell_index][1] if self.selected_colormap != -1 else 'Ninguno'}")
    
    def run(self):
        """Ejecuta la aplicación principal"""
        # Crear ventana y configurar callback del mouse
        cv2.namedWindow('Colormap Grid Viewer', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('Colormap Grid Viewer', self.handle_mouse_click)
        
        # Opcional: Crear ventana adicional para colormap seleccionado
        cv2.namedWindow('Selected Colormap', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Selected Colormap', 400, 300)
        
        print("🎨 Colormap Grid Viewer iniciado")
        print("=" * 50)
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            # Ajustar imagen
            adjusted_frame = self.adjust_image(frame)
            
            # Crear visualización en retícula
            grid_display = self.create_grid_display(adjusted_frame)
            
            # Mostrar retícula principal
            cv2.imshow('Colormap Grid Viewer', grid_display)
            
            # Mostrar colormap seleccionado en ventana separada
            if self.selected_colormap != -1:
                selected_colormap, selected_name = self.colormaps[self.selected_colormap]
                large_frame = cv2.resize(adjusted_frame, (400, 300))
                selected_display = self.apply_colormap_to_frame(large_frame, selected_colormap)
                
                # Añadir información
                cv2.putText(selected_display, f"COLORMAP: {selected_name}", 
                           (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(selected_display, "Click en retícula para cambiar", 
                           (10, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)
                
                cv2.imshow('Selected Colormap', selected_display)
            else:
                # Mostrar frame original en ventana seleccionada
                original_large = cv2.resize(adjusted_frame, (400, 300))
                cv2.putText(original_large, "ORIGINAL - Click para seleccionar", 
                           (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.imshow('Selected Colormap', original_large)
            
            # Manejar teclas
            key = cv2.waitKey(1) & 0xFF
            
            if key == 27:  # ESC
                break
            elif key == ord(' '):  # Espacio - toggle original
                self.show_original = not self.show_original
                print(f"Original: {'ON' if self.show_original else 'OFF'}")
            elif key == ord('+') or key == ord('='):  # Aumentar brillo
                self.brightness = min(50, self.brightness + 5)
                print(f"Brillo: {self.brightness}")
            elif key == ord('-'):  # Disminuir brillo
                self.brightness = max(-50, self.brightness - 5)
                print(f"Brillo: {self.brightness}")
            elif key == ord('c'):  # Aumentar contraste (con 'c')
                self.contrast = min(200, self.contrast + 10)
                print(f"Contraste: {self.contrast}%")
            elif key == ord('v'):  # Disminuir contraste (con 'v')
                self.contrast = max(50, self.contrast - 10)
                print(f"Contraste: {self.contrast}%")
            elif key == ord('r'):  # Reset valores
                self.brightness = 0
                self.contrast = 100
                self.selected_colormap = -1
                print("Valores reseteados")
        
        # Limpiar
        self.cap.release()
        cv2.destroyAllWindows()
        print("👋 Colormap Grid Viewer cerrado")

# Ejecutar la aplicación
if __name__ == "__main__":
    try:
        app = ColormapGridViewer()
        app.run()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Asegúrate de que tu webcam esté conectada y disponible")