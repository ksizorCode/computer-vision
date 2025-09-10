import cv2
import time
import numpy as np


def _noop(_=None):
    # Callback vacío requerido por createTrackbar
    pass


def main_with_canny():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se pudo abrir la cámara.")
        return

    # Ventanas
    cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Canny', cv2.WINDOW_NORMAL)

    # Trackbars para controlar Canny en tiempo real
    max_threshold = 255  # rango típico para umbral en Canny
    cv2.createTrackbar('Min', 'Canny', 50, max_threshold, _noop)
    cv2.createTrackbar('Max', 'Canny', 150, max_threshold, _noop)
    # Efectos y opciones
    cv2.createTrackbar('Blur', 'Canny', 3, 31, _noop)       # 0 -> sin blur, >0 kernel impar
    cv2.createTrackbar('Dilate', 'Canny', 0, 5, _noop)      # 0..5 iteraciones
    cv2.createTrackbar('Invert', 'Canny', 0, 1, _noop)      # 0/1 invertir
    cv2.createTrackbar('L2', 'Canny', 1, 1, _noop)          # 0/1 L2gradient
    cv2.createTrackbar('FPS', 'Canny', 0, 60, _noop)        # 0 = sin límite, 1..60
    cv2.createTrackbar('ShowFPS', 'Canny', 1, 1, _noop)     # 0/1 mostrar FPS

    # Medición de FPS
    last_ts = time.perf_counter()
    fps_ema = 0.0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo leer el frame.")
            break

        loop_start = time.perf_counter()

        # Lee valores actuales de los trackbars
        min_val = cv2.getTrackbarPos('Min', 'Canny')
        max_val = cv2.getTrackbarPos('Max', 'Canny')
        blur_k = cv2.getTrackbarPos('Blur', 'Canny')
        dilate_iters = cv2.getTrackbarPos('Dilate', 'Canny')
        invert = cv2.getTrackbarPos('Invert', 'Canny')
        use_l2 = bool(cv2.getTrackbarPos('L2', 'Canny'))
        fps_cap = cv2.getTrackbarPos('FPS', 'Canny')
        show_fps = bool(cv2.getTrackbarPos('ShowFPS', 'Canny'))

        # Asegura que max > min para evitar error en Canny
        if max_val <= min_val:
            max_val = min_val + 1

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Blur opcional (kernel impar)
        if blur_k and blur_k > 1:
            k = blur_k if (blur_k % 2 == 1) else blur_k + 1
            gray_proc = cv2.GaussianBlur(gray, (k, k), 0)
        else:
            gray_proc = gray

        # Canny (con opción L2)
        edges = cv2.Canny(gray_proc, min_val, max_val, apertureSize=3, L2gradient=use_l2)

        # Dilatación opcional para engrosar bordes
        if dilate_iters > 0:
            edges = cv2.dilate(edges, None, iterations=dilate_iters)

        # Invertir opcional
        if invert:
            edges_disp = cv2.bitwise_not(edges)
        else:
            edges_disp = edges

        # FPS medidos (EMA para suavizar)
        now = time.perf_counter()
        dt = max(now - last_ts, 1e-6)
        last_ts = now
        inst_fps = 1.0 / dt
        fps_ema = inst_fps if fps_ema == 0 else (0.9 * fps_ema + 0.1 * inst_fps)

        webcam_disp = frame.copy()
        if show_fps:
            txt = f"FPS: {fps_ema:5.1f}" if fps_cap == 0 else f"FPS: {fps_ema:5.1f} (cap {fps_cap})"
            cv2.putText(webcam_disp, txt, (10, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

        # Mostrar
        cv2.imshow('Webcam', webcam_disp)
        cv2.imshow('Canny', edges_disp)

        # Calcular delay para limitar FPS si corresponde
        proc_ms = (time.perf_counter() - loop_start) * 1000.0
        if fps_cap > 0:
            target_ms = max(1.0, 1000.0 / float(fps_cap))
            delay = int(max(1.0, target_ms - proc_ms))
        else:
            delay = 1

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main_with_canny()
