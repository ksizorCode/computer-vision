import cv2
import time
import numpy as np


def _noop(_=None):
    # Callback vacío requerido por createTrackbar
    pass


def apply_colormap(edges, colormap_id):
    """Aplica mapa de colores a la imagen de bordes"""
    colormaps = [
        cv2.COLORMAP_VIRIDIS, cv2.COLORMAP_PLASMA, cv2.COLORMAP_INFERNO, cv2.COLORMAP_MAGMA,
        cv2.COLORMAP_JET, cv2.COLORMAP_HSV, cv2.COLORMAP_RAINBOW, cv2.COLORMAP_OCEAN,
        cv2.COLORMAP_SUMMER, cv2.COLORMAP_SPRING, cv2.COLORMAP_COOL, cv2.COLORMAP_WINTER,
        cv2.COLORMAP_AUTUMN, cv2.COLORMAP_HOT, cv2.COLORMAP_PINK, cv2.COLORMAP_BONE,
        cv2.COLORMAP_TWILIGHT, cv2.COLORMAP_TWILIGHT_SHIFTED, cv2.COLORMAP_TURBO, cv2.COLORMAP_DEEPGREEN
    ]
    
    if colormap_id == 0:  # Sin colormap
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    else:
        return cv2.applyColorMap(edges, colormaps[(colormap_id - 1) % len(colormaps)])


def apply_visual_effects(img, effect_id, intensity):
    """Aplica efectos visuales a la imagen"""
    if effect_id == 0:  # Sin efecto
        return img
    
    height, width = img.shape[:2]
    result = img.copy()
    
    if effect_id == 1:  # Glow effect
        # Crear un blur fuerte y combinarlo
        blur = cv2.GaussianBlur(img, (21, 21), 0)
        result = cv2.addWeighted(img, 0.7, blur, 0.3 * intensity/10, 0)
    
    elif effect_id == 2:  # Neon effect
        # Combinar original con versión muy borrosa
        blur = cv2.GaussianBlur(img, (15, 15), 0)
        result = cv2.addWeighted(img, 1.0, blur, intensity/10, 10)
    
    elif effect_id == 3:  # Vintage/Sepia
        # Crear efecto sepia
        kernel = np.array([[0.272, 0.534, 0.131],
                          [0.349, 0.686, 0.168],
                          [0.393, 0.769, 0.189]])
        result = cv2.transform(img, kernel)
        result = np.clip(result, 0, 255).astype(np.uint8)
    
    elif effect_id == 4:  # Posterize
        # Reducir colores para efecto poster
        factor = max(1, 10 - intensity)
        result = (img // (factor * 25)) * (factor * 25)
    
    elif effect_id == 5:  # Emboss
        # Efecto relieve/emboss
        kernel = np.array([[-2, -1, 0],
                          [-1,  1, 1],
                          [ 0,  1, 2]])
        result = cv2.filter2D(img, -1, kernel)
        result = cv2.convertScaleAbs(result, alpha=intensity/5, beta=128)
    
    elif effect_id == 6:  # Motion blur
        # Desenfoque de movimiento
        size = min(15, max(3, intensity))
        kernel = np.zeros((size, size))
        kernel[int((size-1)/2), :] = np.ones(size)
        kernel = kernel / size
        result = cv2.filter2D(img, -1, kernel)
    
    elif effect_id == 7:  # Cristal/Glass
        # Efecto vidrio roto
        noise = np.random.randint(0, intensity*3, (height, width, 2), dtype=np.int16)
        x, y = np.meshgrid(np.arange(width), np.arange(height))
        x_new = np.clip(x + noise[:, :, 0], 0, width-1).astype(np.int32)
        y_new = np.clip(y + noise[:, :, 1], 0, height-1).astype(np.int32)
        result = img[y_new, x_new]
    
    elif effect_id == 8:  # Psychedelic
        # Efecto psicodélico con ondas
        x, y = np.meshgrid(np.arange(width), np.arange(height))
        wave_x = (np.sin(y / 20) * intensity).astype(np.int16)
        wave_y = (np.cos(x / 20) * intensity).astype(np.int16)
        x_new = np.clip(x + wave_x, 0, width-1).astype(np.int32)
        y_new = np.clip(y + wave_y, 0, height-1).astype(np.int32)
        result = img[y_new, x_new]
    
    return result


def create_overlay_pattern(height, width, pattern_id, intensity):
    """Crea patrones de overlay para efectos adicionales"""
    overlay = np.zeros((height, width, 3), dtype=np.uint8)
    
    if pattern_id == 0:  # Sin patrón
        return overlay
    
    elif pattern_id == 1:  # Vignette (viñeta)
        center_x, center_y = width // 2, height // 2
        max_dist = np.sqrt(center_x**2 + center_y**2)
        y, x = np.ogrid[:height, :width]
        distances = np.sqrt((x - center_x)**2 + (y - center_y)**2)
        vignette = 1 - np.clip(distances / max_dist, 0, 1)
        vignette = np.power(vignette, 2.0 - intensity/10)
        overlay = np.stack([vignette * 255] * 3, axis=-1).astype(np.uint8)
    
    elif pattern_id == 2:  # Líneas escaneadas
        for i in range(0, height, max(2, 10 - intensity)):
            overlay[i:i+1, :] = [50, 50, 50]
    
    elif pattern_id == 3:  # Cuadrícula
        grid_size = max(10, 50 - intensity * 4)
        for i in range(0, height, grid_size):
            overlay[i:i+1, :] = [30, 30, 30]
        for i in range(0, width, grid_size):
            overlay[:, i:i+1] = [30, 30, 30]
    
    elif pattern_id == 4:  # Círculos concéntricos
        center_x, center_y = width // 2, height // 2
        y, x = np.ogrid[:height, :width]
        distances = np.sqrt((x - center_x)**2 + (y - center_y)**2)
        circles = np.sin(distances / (20 - intensity)) * 127 + 127
        overlay = np.stack([circles] * 3, axis=-1).astype(np.uint8)
    
    return overlay


def main_with_canny():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return

    # Ventanas
    cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Canny Effects', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Combined View', cv2.WINDOW_NORMAL)

    # Trackbars originales para Canny
    max_threshold = 255
    cv2.createTrackbar('Min', 'Canny Effects', 50, max_threshold, _noop)
    cv2.createTrackbar('Max', 'Canny Effects', 150, max_threshold, _noop)
    cv2.createTrackbar('Blur', 'Canny Effects', 3, 31, _noop)
    cv2.createTrackbar('Dilate', 'Canny Effects', 0, 5, _noop)
    cv2.createTrackbar('Invert', 'Canny Effects', 0, 1, _noop)
    cv2.createTrackbar('L2', 'Canny Effects', 1, 1, _noop)
    
    # Nuevos trackbars para efectos visuales
    cv2.createTrackbar('Colormap', 'Canny Effects', 0, 20, _noop)  # 20 colormaps disponibles
    cv2.createTrackbar('Effect', 'Canny Effects', 0, 8, _noop)     # 8 efectos visuales
    cv2.createTrackbar('Intensity', 'Canny Effects', 5, 10, _noop) # Intensidad del efecto
    cv2.createTrackbar('Overlay', 'Canny Effects', 0, 4, _noop)    # Patrones de overlay
    cv2.createTrackbar('Blend', 'Canny Effects', 50, 100, _noop)   # Mezcla con original
    cv2.createTrackbar('Gamma', 'Canny Effects', 10, 30, _noop)    # Corrección gamma
    
    # Trackbars de control
    cv2.createTrackbar('FPS', 'Canny Effects', 0, 60, _noop)
    cv2.createTrackbar('ShowFPS', 'Canny Effects', 1, 1, _noop)
    cv2.createTrackbar('ShowInfo', 'Canny Effects', 1, 1, _noop)   # Mostrar info de efectos

    # Medición de FPS
    last_ts = time.perf_counter()
    fps_ema = 0.0
    
    # Nombres de efectos para mostrar
    colormap_names = ['None', 'Viridis', 'Plasma', 'Inferno', 'Magma', 'Jet', 'HSV', 'Rainbow', 
                      'Ocean', 'Summer', 'Spring', 'Cool', 'Winter', 'Autumn', 'Hot', 'Pink', 
                      'Bone', 'Twilight', 'TwilightShift', 'Turbo', 'DeepGreen']
    effect_names = ['None', 'Glow', 'Neon', 'Vintage', 'Posterize', 'Emboss', 'MotionBlur', 'Glass', 'Psychedelic']
    overlay_names = ['None', 'Vignette', 'Scanlines', 'Grid', 'Circles']

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame.")
            break

        loop_start = time.perf_counter()

        # Lee valores de trackbars originales
        min_val = cv2.getTrackbarPos('Min', 'Canny Effects')
        max_val = cv2.getTrackbarPos('Max', 'Canny Effects')
        blur_k = cv2.getTrackbarPos('Blur', 'Canny Effects')
        dilate_iters = cv2.getTrackbarPos('Dilate', 'Canny Effects')
        invert = cv2.getTrackbarPos('Invert', 'Canny Effects')
        use_l2 = bool(cv2.getTrackbarPos('L2', 'Canny Effects'))
        
        # Lee valores de efectos visuales
        colormap_id = cv2.getTrackbarPos('Colormap', 'Canny Effects')
        effect_id = cv2.getTrackbarPos('Effect', 'Canny Effects')
        intensity = cv2.getTrackbarPos('Intensity', 'Canny Effects')
        overlay_id = cv2.getTrackbarPos('Overlay', 'Canny Effects')
        blend_factor = cv2.getTrackbarPos('Blend', 'Canny Effects') / 100.0
        gamma_val = cv2.getTrackbarPos('Gamma', 'Canny Effects') / 10.0
        
        # Control
        fps_cap = cv2.getTrackbarPos('FPS', 'Canny Effects')
        show_fps = bool(cv2.getTrackbarPos('ShowFPS', 'Canny Effects'))
        show_info = bool(cv2.getTrackbarPos('ShowInfo', 'Canny Effects'))

        # Asegurar que max > min
        if max_val <= min_val:
            max_val = min_val + 1

        # Procesamiento Canny básico
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        if blur_k and blur_k > 1:
            k = blur_k if (blur_k % 2 == 1) else blur_k + 1
            gray_proc = cv2.GaussianBlur(gray, (k, k), 0)
        else:
            gray_proc = gray

        edges = cv2.Canny(gray_proc, min_val, max_val, apertureSize=3, L2gradient=use_l2)

        if dilate_iters > 0:
            edges = cv2.dilate(edges, None, iterations=dilate_iters)

        if invert:
            edges = cv2.bitwise_not(edges)

        # Aplicar corrección gamma a los bordes
        if gamma_val != 1.0:
            edges_gamma = np.power(edges / 255.0, gamma_val) * 255.0
            edges = np.clip(edges_gamma, 0, 255).astype(np.uint8)

        # Aplicar colormap
        colored_edges = apply_colormap(edges, colormap_id)
        
        # Aplicar efectos visuales
        if effect_id > 0:
            colored_edges = apply_visual_effects(colored_edges, effect_id, intensity)
        
        # Crear y aplicar overlay
        if overlay_id > 0:
            height, width = colored_edges.shape[:2]
            overlay = create_overlay_pattern(height, width, overlay_id, intensity)
            colored_edges = cv2.addWeighted(colored_edges, 0.8, overlay, 0.2, 0)
        
        # Mezclar con imagen original si se desea
        if blend_factor > 0 and blend_factor < 1:
            frame_resized = cv2.resize(frame, (colored_edges.shape[1], colored_edges.shape[0]))
            final_result = cv2.addWeighted(colored_edges, 1 - blend_factor, frame_resized, blend_factor, 0)
        else:
            final_result = colored_edges

        # Calcular FPS
        now = time.perf_counter()
        dt = max(now - last_ts, 1e-6)
        last_ts = now
        inst_fps = 1.0 / dt
        fps_ema = inst_fps if fps_ema == 0 else (0.9 * fps_ema + 0.1 * inst_fps)

        # Preparar imagen para mostrar información
        webcam_disp = frame.copy()
        info_img = final_result.copy()

        # Mostrar FPS
        if show_fps:
            fps_text = f"FPS: {fps_ema:5.1f}" if fps_cap == 0 else f"FPS: {fps_ema:5.1f} (cap {fps_cap})"
            cv2.putText(webcam_disp, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(info_img, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Mostrar información de efectos
        if show_info:
            y_offset = 60
            texts = [
                f"Colormap: {colormap_names[min(colormap_id, len(colormap_names)-1)]}",
                f"Effect: {effect_names[min(effect_id, len(effect_names)-1)]}",
                f"Intensity: {intensity}",
                f"Overlay: {overlay_names[min(overlay_id, len(overlay_names)-1)]}",
                f"Blend: {blend_factor:.1f}",
                f"Gamma: {gamma_val:.1f}"
            ]
            
            for i, text in enumerate(texts):
                cv2.putText(info_img, text, (10, y_offset + i*25), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Mostrar imágenes
        cv2.imshow('Webcam', webcam_disp)
        cv2.imshow('Canny Effects', info_img)
        
        # Crear vista combinada (side by side)
        combined = np.hstack([cv2.resize(frame, (320, 240)), 
                             cv2.resize(final_result, (320, 240))])
        cv2.imshow('Combined View', combined)

        # Control de FPS
        proc_ms = (time.perf_counter() - loop_start) * 1000.0
        if fps_cap > 0:
            target_ms = max(1.0, 1000.0 / float(fps_cap))
            delay = int(max(1.0, target_ms - proc_ms))
        else:
            delay = 1

        key = cv2.waitKey(delay) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):  # Guardar screenshot
            timestamp = int(time.time())
            cv2.imwrite(f'canny_effect_{timestamp}.jpg', final_result)
            print(f"Screenshot guardado: canny_effect_{timestamp}.jpg")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("=== DETECTOR CANNY CON EFECTOS VISUALES ===")
    print("Controles disponibles:")
    print("- Trackbars para ajustar todos los parámetros")
    print("- 20+ mapas de colores diferentes")
    print("- 8 efectos visuales (Glow, Neon, Vintage, etc.)")
    print("- 4 patrones de overlay")
    print("- Mezcla con imagen original")
    print("- Corrección gamma")
    print("- Presiona 'q' para salir")
    print("- Presiona 's' para guardar screenshot")
    print()
    
    main_with_canny()