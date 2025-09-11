import cv2
import numpy as np
import os
import time

def load_obj_simple(filepath):
    """
    Carga un archivo OBJ de forma simple y eficiente
    """
    vertices = []
    faces = []
    
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('v '):  # Vértice
                    parts = line.split()
                    if len(parts) >= 4:
                        x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                        vertices.append([x, y, z])
                        
                elif line.startswith('f '):  # Cara
                    parts = line.split()
                    face_vertices = []
                    
                    for part in parts[1:]:
                        vertex_idx = int(part.split('/')[0]) - 1  # OBJ usa índices base 1
                        face_vertices.append(vertex_idx)
                    
                    if len(face_vertices) >= 3:
                        # Convertir quads en triángulos para mejor rendimiento
                        if len(face_vertices) == 4:
                            faces.append([face_vertices[0], face_vertices[1], face_vertices[2]])
                            faces.append([face_vertices[0], face_vertices[2], face_vertices[3]])
                        else:
                            faces.append(face_vertices[:3])  # Solo tomar triángulos
        
        print(f"Modelo cargado: {len(vertices)} vértices, {len(faces)} triángulos")
        return np.array(vertices, dtype=np.float32), faces
    
    except Exception as e:
        print(f"Error cargando archivo OBJ: {e}")
        return None, None

def find_texture_file(obj_filepath):
    """
    Busca archivos de textura en el mismo directorio que el OBJ
    """
    obj_dir = os.path.dirname(obj_filepath)
    obj_name = os.path.splitext(os.path.basename(obj_filepath))[0]
    
    # Extensiones de imagen comunes
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
    
    # Nombres comunes de archivos de textura
    texture_names = [obj_name, 'texture', 'diffuse', 'tex']
    
    for name in texture_names:
        for ext in image_extensions:
            texture_path = os.path.join(obj_dir, name + ext)
            if os.path.exists(texture_path):
                texture = cv2.imread(texture_path)
                if texture is not None:
                    # Redimensionar textura para mejor rendimiento
                    height, width = texture.shape[:2]
                    if width > 512 or height > 512:
                        scale = 512 / max(width, height)
                        new_width = int(width * scale)
                        new_height = int(height * scale)
                        texture = cv2.resize(texture, (new_width, new_height))
                    
                    print(f"Textura encontrada: {name + ext} ({texture.shape})")
                    return texture
    
    return None

def create_simple_cube():
    """
    Crea un cubo simple optimizado
    """
    vertices = np.array([
        # Cara frontal
        [-1, -1,  1], [ 1, -1,  1], [ 1,  1,  1], [-1,  1,  1],
        # Cara trasera  
        [-1, -1, -1], [-1,  1, -1], [ 1,  1, -1], [ 1, -1, -1]
    ], dtype=np.float32)
    
    # Caras como triángulos (mejor rendimiento)
    faces = [
        # Frontal
        [0, 1, 2], [0, 2, 3],
        # Trasera
        [4, 5, 6], [4, 6, 7],
        # Izquierda
        [4, 0, 3], [4, 3, 5],
        # Derecha
        [1, 7, 6], [1, 6, 2],
        # Superior
        [3, 2, 6], [3, 6, 5],
        # Inferior
        [4, 7, 1], [4, 1, 0]
    ]
    
    return vertices, faces

def create_gradient_texture():
    """
    Crea una textura simple de gradiente para mejor rendimiento
    """
    size = 256
    texture = np.zeros((size, size, 3), dtype=np.uint8)
    
    for i in range(size):
        for j in range(size):
            # Gradiente diagonal colorido
            r = int(255 * (i / size))
            g = int(255 * (j / size))
            b = int(255 * ((i + j) / (2 * size)))
            texture[i, j] = [b, g, r]  # BGR format
    
    return texture

def render_face_simple(frame, vertices_2d, face, texture, depth_values):
    """
    Renderiza una cara de forma simple y eficiente
    """
    if len(face) != 3:  # Solo triángulos
        return
    
    try:
        # Obtener puntos 2D del triángulo
        points_2d = []
        valid_face = True
        
        for vertex_idx in face:
            if vertex_idx >= len(vertices_2d):
                valid_face = False
                break
            points_2d.append(vertices_2d[vertex_idx])
        
        if not valid_face or len(points_2d) != 3:
            return
        
        # Convertir a array numpy
        triangle = np.array(points_2d, dtype=np.int32)
        
        # Verificar que el triángulo esté dentro de la pantalla
        frame_h, frame_w = frame.shape[:2]
        if (np.any(triangle[:, 0] < -100) or np.any(triangle[:, 0] > frame_w + 100) or
            np.any(triangle[:, 1] < -100) or np.any(triangle[:, 1] > frame_h + 100)):
            return
        
        # Calcular profundidad promedio del triángulo para z-buffering básico
        avg_depth = np.mean([depth_values[i] for i in face])
        
        # Color basado en profundidad (más lejano = más oscuro)
        depth_factor = max(0.3, min(1.0, 1.0 - (avg_depth - 0.05) * 10))
        
        if texture is not None:
            # Usar color de textura promedio para este triángulo
            tex_h, tex_w = texture.shape[:2]
            sample_y = int(tex_h * 0.5)
            sample_x = int(tex_w * 0.5)
            color = texture[sample_y, sample_x].astype(float) * depth_factor
            color = tuple(int(c) for c in color)
        else:
            # Color sólido con variación de profundidad
            base_color = (100, 150, 200)  # Azul grisáceo
            color = tuple(int(c * depth_factor) for c in base_color)
        
        # Dibujar triángulo relleno
        cv2.fillPoly(frame, [triangle], color)
        
        # Opcional: dibujar bordes para definir la forma
        cv2.polylines(frame, [triangle], True, (0, 0, 0), 1)
        
    except Exception as e:
        # En caso de error, dibujar como líneas
        if len(face) >= 3:
            for i in range(len(face)):
                start_idx = face[i]
                end_idx = face[(i + 1) % len(face)]
                
                if start_idx < len(vertices_2d) and end_idx < len(vertices_2d):
                    start_point = tuple(vertices_2d[start_idx])
                    end_point = tuple(vertices_2d[end_idx])
                    cv2.line(frame, start_point, end_point, (0, 255, 0), 1)

def main():
    print("Iniciando programa ArUco optimizado...")
    
    # Verificar OpenCV
    print(f"Versión OpenCV: {cv2.__version__}")
    
    # Obtener el directorio donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_folder = os.path.join(script_dir, "img_aruco")
    
    print(f"Buscando modelos 3D en: {model_folder}")
    
    # Buscar archivos OBJ
    model_files = []
    if os.path.exists(model_folder):
        for file in os.listdir(model_folder):
            if file.lower().endswith('.obj'):
                model_files.append(os.path.join(model_folder, file))
        
        print(f"Archivos OBJ encontrados: {[os.path.basename(f) for f in model_files]}")
    
    # Cargar modelo 3D
    vertices = None
    faces = None
    texture = None
    
    if model_files:
        model_path = model_files[0]
        print(f"Cargando modelo: {os.path.basename(model_path)}")
        
        vertices, faces = load_obj_simple(model_path)
        
        if vertices is not None:
            texture = find_texture_file(model_path)
            
            # Limitar número de caras para mejor rendimiento
            if len(faces) > 1000:
                print(f"Modelo muy complejo ({len(faces)} caras), usando solo las primeras 1000")
                faces = faces[:1000]
    else:
        print("No se encontraron archivos OBJ, usando cubo de ejemplo...")
        vertices, faces = create_simple_cube()
    
    # Si no hay textura, crear una simple
    if texture is None:
        print("Creando textura de gradiente...")
        texture = create_gradient_texture()
    
    if vertices is None or faces is None:
        print("Error: No se pudo cargar ningún modelo 3D")
        return
    
    # Configuración de la cámara
    camera_matrix = np.array([[600, 0, 320],
                             [0, 600, 240],
                             [0, 0, 1]], dtype=np.float32)
    
    dist_coeffs = np.array([0, 0, 0, 0, 0], dtype=np.float32)
    
    # Configurar ArUco
    try:
        aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
        parameters = cv2.aruco.DetectorParameters()
        detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
        use_new_api = True
        print("Usando API nueva de ArUco")
    except AttributeError:
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
        parameters = cv2.aruco.DetectorParameters_create()
        use_new_api = False
        print("Usando API antigua de ArUco")
    
    # Tamaño del marcador ArUco en metros
    marker_size = 0.05
    
    # Iniciar cámara
    print("Intentando abrir la cámara...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
        
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara")
        return
    
    # Configurar resolución más baja para mejor rendimiento
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    print("Cámara abierta correctamente")
    print("Controles:")
    print("- Presiona 'q' para salir")
    print("- Presiona '+' o '-' para cambiar tamaño")
    print("- Presiona 't' para alternar texturas/wireframe")
    print("- Muestra un marcador ArUco a la cámara")
    
    # Variables de control
    model_scale = 0.03
    show_textured = True
    
    # Variables para FPS
    fps_counter = 0
    fps_timer = time.time()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Calcular FPS
        fps_counter += 1
        current_time = time.time()
        if current_time - fps_timer >= 1.0:
            fps = fps_counter / (current_time - fps_timer)
            fps_counter = 0
            fps_timer = current_time
        else:
            fps = 0
        
        # Detectar marcadores ArUco
        if use_new_api:
            corners, ids, rejected = detector.detectMarkers(frame)
        else:
            corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
        
        # Mostrar información
        mode_text = "Texturizado" if show_textured else "Wireframe"
        info_text = f"3D ({mode_text}) | ArUcos: {len(ids) if ids is not None else 0} | Escala: {model_scale:.2f}"
        cv2.putText(frame, info_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        if fps > 0:
            cv2.putText(frame, f"FPS: {fps:.1f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
        
        if ids is not None and len(ids) > 0:
            # Dibujar marcadores
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)
            
            # Estimar pose
            try:
                rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                    corners, marker_size, camera_matrix, dist_coeffs)
                
                for i in range(len(ids)):
                    # Dibujar ejes
                    try:
                        cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, 
                                        rvecs[i], tvecs[i], marker_size)
                    except AttributeError:
                        cv2.aruco.drawAxis(frame, camera_matrix, dist_coeffs, 
                                         rvecs[i], tvecs[i], marker_size)
                    
                    # Proyectar vértices 3D a 2D
                    scaled_vertices = vertices * model_scale
                    projected_points, _ = cv2.projectPoints(
                        scaled_vertices, rvecs[i], tvecs[i], camera_matrix, dist_coeffs)
                    projected_points = projected_points.reshape(-1, 2).astype(np.int32)
                    
                    # Calcular profundidades para z-buffering básico
                    depth_values = []
                    for vertex in scaled_vertices:
                        # Transformar punto al sistema de coordenadas de la cámara
                        point_3d = np.array([vertex], dtype=np.float32).reshape(-1, 1, 3)
                        transformed, _ = cv2.projectPoints(point_3d, rvecs[i], tvecs[i], 
                                                         camera_matrix, dist_coeffs)
                        # Usar la coordenada Z transformada como profundidad aproximada
                        depth = np.linalg.norm(vertex) + tvecs[i][0][2]
                        depth_values.append(depth)
                    
                    # Renderizar modelo
                    if show_textured:
                        # Renderizar con caras rellenas
                        for face in faces:
                            render_face_simple(frame, projected_points, face, texture, depth_values)
                    else:
                        # Renderizar wireframe (más rápido)
                        for face in faces:
                            if len(face) >= 3:
                                for j in range(len(face)):
                                    start_idx = face[j]
                                    end_idx = face[(j + 1) % len(face)]
                                    
                                    if start_idx < len(projected_points) and end_idx < len(projected_points):
                                        start_point = tuple(projected_points[start_idx])
                                        end_point = tuple(projected_points[end_idx])
                                        cv2.line(frame, start_point, end_point, (0, 255, 0), 1)
                    
            except Exception as e:
                print(f"Error estimando pose: {e}")
        
        # Instrucciones
        cv2.putText(frame, "q:salir | t:modo | +/-:tamaño", 
                   (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Mostrar frame
        cv2.imshow('ArUco 3D Optimizado', frame)
        
        # Controles
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('t'):
            show_textured = not show_textured
            print(f"Modo cambiado a: {'Texturizado' if show_textured else 'Wireframe'}")
        elif key == ord('+') or key == ord('='):
            model_scale *= 1.1
            print(f"Escala aumentada a: {model_scale:.3f}")
        elif key == ord('-'):
            model_scale *= 0.9
            print(f"Escala reducida a: {model_scale:.3f}")
    
    # Limpiar
    cap.release()
    cv2.destroyAllWindows()
    print("Programa terminado")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error general: {e}")
    
    input("Presiona Enter para cerrar...")