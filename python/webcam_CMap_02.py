import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import threading
import time

class ColormapCatalog:
    def __init__(self):
        # Lista de colormaps disponibles en matplotlib
        self.colormaps = [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis',
            'hot', 'cool', 'spring', 'summer', 'autumn', 'winter',
            'gray', 'bone', 'copper', 'pink',
            'jet', 'rainbow', 'hsv', 'flag', 'prism',
            'seismic', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral',
            'coolwarm', 'bwr', 'PiYG', 'PRGn', 'BrBG',
            'PuOr', 'RdGy', 'RdPu', 'BuPu', 'GnBu',
            'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'
        ]
        self.current_colormap_index = 0
        self.auto_cycle = True
        self.cycle_delay = 2.0  # segundos
        self.last_cycle_time = time.time()
        
    def apply_colormap(self, frame, colormap_name):
        """Aplica un colormap a la imagen"""
        # Convertir a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Normalizar valores entre 0 y 1
        normalized = gray / 255.0
        
        # Obtener el colormap de matplotlib
        cmap = cm.get_cmap(colormap_name)
        
        # Aplicar el colormap
        colored = cmap(normalized)
        
        # Convertir de vuelta a formato BGR para OpenCV (0-255)
        colored_bgr = (colored[:, :, :3] * 255).astype(np.uint8)
        colored_bgr = cv2.cvtColor(colored_bgr, cv2.COLOR_RGB2BGR)
        
        return colored_bgr
    
    def create_grid_view(self, frame, num_cols=6):
        """Crea una vista en cuadrícula con múltiples colormaps"""
        height, width = frame.shape[:2]
        
        # Calcular dimensiones de cada celda
        cell_height = height // ((len(self.colormaps) + num_cols - 1) // num_cols)
        cell_width = width // num_cols
        
        # Redimensionar frame para que quepa en las celdas
        small_frame = cv2.resize(frame, (cell_width - 4, cell_height - 20))
        
        # Crear imagen de salida
        grid_height = cell_height * ((len(self.colormaps) + num_cols - 1) // num_cols)
        grid_width = cell_width * num_cols
        grid = np.zeros((grid_height, grid_width, 3), dtype=np.uint8)
        
        # Llenar la cuadrícula
        for i, colormap_name in enumerate(self.colormaps):
            row = i // num_cols
            col = i % num_cols
            
            # Aplicar colormap
            colored_frame = self.apply_colormap(small_frame, colormap_name)
            
            # Posición en la cuadrícula
            y_start = row * cell_height + 2
            y_end = y_start + small_frame.shape[0]
            x_start = col * cell_width + 2
            x_end = x_start + small_frame.shape[1]
            
            # Colocar imagen en la cuadrícula
            grid[y_start:y_end, x_start:x_end] = colored_frame
            
            # Añadir texto con el nombre del colormap
            text_y = y_end + 15
            cv2.putText(grid, colormap_name, (x_start + 5, text_y), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
            
            # Resaltar el colormap actual
            if i == self.current_colormap_index:
                cv2.rectangle(grid, (x_start, y_start-2), (x_end, text_y+2), 
                            (0, 255, 0), 2)
        
        return grid
    
    def run(self):
        """Función principal que ejecuta el catálogo"""
        # Inicializar la webcam
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: No se pudo acceder a la webcam")
            return
        
        print("Controles:")
        print("- Presiona ESPACIO para cambiar entre vista individual y cuadrícula")
        print("- Presiona 'n' para siguiente colormap (en vista individual)")
        print("- Presiona 'p' para colormap anterior (en vista individual)")
        print("- Presiona 'a' para activar/desactivar cambio automático")
        print("- Presiona 'q' para salir")
        
        show_grid = True
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: No se pudo leer el frame")
                break
            
            # Voltear horizontalmente para efecto espejo
            frame = cv2.flip(frame, 1)
            
            current_time = time.time()
            
            # Cambio automático de colormap
            if self.auto_cycle and current_time - self.last_cycle_time > self.cycle_delay:
                self.current_colormap_index = (self.current_colormap_index + 1) % len(self.colormaps)
                self.last_cycle_time = current_time
            
            if show_grid:
                # Vista en cuadrícula
                display_frame = self.create_grid_view(frame)
                window_title = "Catálogo de Colormaps - Vista Cuadrícula"
            else:
                # Vista individual
                current_colormap = self.colormaps[self.current_colormap_index]
                display_frame = self.apply_colormap(frame, current_colormap)
                window_title = f"Colormap: {current_colormap}"
                
                # Añadir información en pantalla
                cv2.putText(display_frame, f"Colormap: {current_colormap}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(display_frame, f"Auto: {'ON' if self.auto_cycle else 'OFF'}", 
                           (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(display_frame, f"Colormap {self.current_colormap_index + 1}/{len(self.colormaps)}", 
                           (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            cv2.imshow(window_title, display_frame)
            
            # Manejar entrada de teclado
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q'):
                break
            elif key == ord(' '):  # Espacio
                show_grid = not show_grid
            elif key == ord('n') and not show_grid:
                self.current_colormap_index = (self.current_colormap_index + 1) % len(self.colormaps)
            elif key == ord('p') and not show_grid:
                self.current_colormap_index = (self.current_colormap_index - 1) % len(self.colormaps)
            elif key == ord('a'):
                self.auto_cycle = not self.auto_cycle
                self.last_cycle_time = current_time
        
        # Limpiar
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    catalog = ColormapCatalog()
    catalog.run()