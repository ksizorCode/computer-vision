import cv2
import numpy as np
import os

def main():
    print("Iniciando programa ArUco...")
    
    # Verificar OpenCV
    print(f"Versión OpenCV: {cv2.__version__}")
    
    # Obtener el directorio donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    img_folder = os.path.join(script_dir, "img_aruco")
    img_path = os.path.join(img_folder, "imagenAR.png")
    
    print(f"Directorio del script: {script_dir}")
    print(f"Buscando carpeta en: {img_folder}")
    print(f"Buscando imagen en: {img_path}")
    
    if not os.path.exists(img_folder):
        print("Error: La carpeta 'img_aruco' no existe")
        print(f"Crea la carpeta 'img_aruco' en: {script_dir}")
        print("Y coloca tu imagen 'imagenAR.png' dentro")
        return
        
    if not os.path.exists(img_path):
        print(f"Error: No se encontró la imagen en {img_path}")
        print("Asegúrate de que el archivo se llame exactamente 'imagenAR.png'")
        print(f"Archivos en img_aruco: {os.listdir(img_folder) if os.path.exists(img_folder) else 'Carpeta no existe'}")
        return
    
    # Cargar la imagen AR
    ar_image = cv2.imread(img_path)
    if ar_image is None:
        print(f"Error: No se pudo cargar la imagen {img_path}")
        print("Verifica que el archivo no esté dañado")
        return
    
    print(f"Imagen cargada correctamente: {ar_image.shape}")
    
    # Redimensionar la imagen AR si es muy grande
    height, width = ar_image.shape[:2]
    if width > 300 or height > 300:
        scale = 300 / max(width, height)
        new_width = int(width * scale)
        new_height = int(height * scale)
        ar_image = cv2.resize(ar_image, (new_width, new_height))
        print(f"Imagen redimensionada a: {ar_image.shape}")
    
    # Configuración de la cámara (valores genéricos)
    camera_matrix = np.array([[600, 0, 320],
                             [0, 600, 240],
                             [0, 0, 1]], dtype=np.float32)
    
    dist_coeffs = np.array([0, 0, 0, 0, 0], dtype=np.float32)
    
    # Configurar ArUco - Compatible con versiones antiguas y nuevas
    try:
        # Para OpenCV 4.7+
        aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
        parameters = cv2.aruco.DetectorParameters()
        detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
        use_new_api = True
        print("Usando API nueva de ArUco")
    except AttributeError:
        # Para versiones más antiguas de OpenCV
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
        parameters = cv2.aruco.DetectorParameters_create()
        use_new_api = False
        print("Usando API antigua de ArUco")
    
    # Tamaño del marcador ArUco en metros
    marker_size = 0.05  # 5 cm
    
    # Intentar abrir la cámara
    print("Intentando abrir la cámara...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara 0, intentando con cámara 1...")
        cap = cv2.VideoCapture(1)
        
    if not cap.isOpened():
        print("Error: No se pudo abrir ninguna cámara")
        print("Verifica que tu cámara esté conectada y no esté siendo usada por otra aplicación")
        return
    
    print("Cámara abierta correctamente")
    print("Controles:")
    print("- Presiona 'q' para salir")
    print("- Presiona 's' para modo simple (sin AR)")
    print("- Muestra un marcador ArUco a la cámara")
    
    frame_count = 0
    simple_mode = False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo leer el frame de la cámara")
            break
        
        frame_count += 1
        
        # Detectar marcadores ArUco
        try:
            if use_new_api:
                corners, ids, rejected = detector.detectMarkers(frame)
            else:
                corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
        except Exception as e:
            print(f"Error detectando marcadores: {e}")
            corners, ids, rejected = [], None, []
        
        # Mostrar información básica
        info_text = f"Frame: {frame_count} | ArUcos: {len(ids) if ids is not None else 0}"
        if simple_mode:
            info_text += " | MODO SIMPLE"
        cv2.putText(frame, info_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        if ids is not None and len(ids) > 0:
            print(f"¡ArUco detectado! IDs: {ids.flatten()}")
            
            # Dibujar los marcadores detectados
            try:
                cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            except Exception as e:
                print(f"Error dibujando marcadores: {e}")
            
            # Solo hacer AR si no está en modo simple
            if not simple_mode:
                # Estimar pose para cada marcador
                try:
                    # Verificar que estimatePoseSingleMarkers existe
                    if hasattr(cv2.aruco, 'estimatePoseSingleMarkers'):
                        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                            corners, marker_size, camera_matrix, dist_coeffs)
                    else:
                        # Método alternativo usando solvePnP
                        rvecs, tvecs = [], []
                        for corner in corners:
                            # Definir puntos 3D del marcador
                            object_points = np.array([
                                [-marker_size/2,  marker_size/2, 0],
                                [ marker_size/2,  marker_size/2, 0],
                                [ marker_size/2, -marker_size/2, 0],
                                [-marker_size/2, -marker_size/2, 0]
                            ], dtype=np.float32)
                            
                            success, rvec, tvec = cv2.solvePnP(
                                object_points, corner.reshape(-1, 2), 
                                camera_matrix, dist_coeffs)
                            
                            if success:
                                rvecs.append(rvec)
                                tvecs.append(tvec)
                    
                    # Procesar cada marcador detectado
                    for i in range(min(len(ids), len(rvecs), len(tvecs))):
                        try:
                            # Dibujar ejes del marcador
                            if hasattr(cv2, 'drawFrameAxes'):
                                cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, 
                                                rvecs[i], tvecs[i], marker_size)
                            elif hasattr(cv2.aruco, 'drawAxis'):
                                cv2.aruco.drawAxis(frame, camera_matrix, dist_coeffs, 
                                                 rvecs[i], tvecs[i], marker_size)
                            
                            # Verificar que tenemos valores válidos
                            if np.any(np.isnan(rvecs[i])) or np.any(np.isnan(tvecs[i])):
                                continue
                                
                            # Crear puntos 3D para la imagen perpendicular
                            img_height, img_width = ar_image.shape[:2]
                            
                            # Escalar la imagen al tamaño del marcador
                            scale_factor = marker_size / max(img_width, img_height) * 2
                            scaled_width = img_width * scale_factor
                            scaled_height = img_height * scale_factor
                            
                            # Puntos 3D perpendiculares al marcador (en el plano YZ)
                            object_points_3d = np.array([
                                [0, -scaled_width/2, scaled_height/2],    
                                [0, scaled_width/2, scaled_height/2],     
                                [0, scaled_width/2, -scaled_height/2],    
                                [0, -scaled_width/2, -scaled_height/2]    
                            ], dtype=np.float32)
                            
                            # Proyectar puntos 3D a 2D
                            img_points_2d, _ = cv2.projectPoints(
                                object_points_3d, rvecs[i], tvecs[i], 
                                camera_matrix, dist_coeffs)
                            
                            # Puntos fuente de la imagen
                            src_points = np.array([
                                [0, 0],
                                [img_width, 0],
                                [img_width, img_height],
                                [0, img_height]
                            ], dtype=np.float32)
                            
                            dst_points = img_points_2d.reshape(-1, 2).astype(np.float32)
                            
                            # Verificar que los puntos sean válidos
                            if (np.any(np.isnan(dst_points)) or np.any(np.isinf(dst_points)) or
                                np.any(dst_points < -1000) or np.any(dst_points > frame.shape[1] + 1000)):
                                continue
                            
                            # Verificar que los puntos forman un cuadrilátero válido
                            area = cv2.contourArea(dst_points.astype(np.int32))
                            if area < 100:  # Área mínima
                                continue
                            
                            # Calcular matriz de transformación
                            matrix = cv2.getPerspectiveTransform(src_points, dst_points)
                            
                            # Aplicar transformación
                            warped_img = cv2.warpPerspective(
                                ar_image, matrix, (frame.shape[1], frame.shape[0]))
                            
                            # Crear máscara
                            mask = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.uint8)
                            cv2.fillPoly(mask, [dst_points.astype(np.int32)], 255)
                            
                            # Combinar imágenes
                            mask_inv = cv2.bitwise_not(mask)
                            frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
                            warped_img_fg = cv2.bitwise_and(warped_img, warped_img, mask=mask)
                            frame = cv2.add(frame_bg, warped_img_fg)
                            
                        except Exception as e:
                            print(f"Error procesando marcador {i}: {e}")
                            continue
                            
                except Exception as e:
                    print(f"Error estimando pose: {e}")
                    simple_mode = True  # Cambiar a modo simple automáticamente
                    print("Cambiando automáticamente a modo simple")
        
        # Instrucciones en pantalla
        cv2.putText(frame, "Presiona 'q' para salir, 's' para modo simple", 
                   (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Mostrar frame
        cv2.imshow('ArUco 3D - Presiona q para salir', frame)
        
        # Control de teclado
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Saliendo...")
            break
        elif key == ord('s'):
            simple_mode = not simple_mode
            print(f"Modo simple: {'Activado' if simple_mode else 'Desactivado'}")
    
    # Limpiar recursos
    cap.release()
    cv2.destroyAllWindows()
    print("Programa terminado")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error general: {e}")
        print("Asegúrate de tener instalado: pip install opencv-python opencv-contrib-python")
    
    input("Presiona Enter para cerrar...")