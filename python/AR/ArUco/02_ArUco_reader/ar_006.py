# Carga modelo 3D desde archivo OBJ o PLY y lo proyecta sobre marcadores ArUco
# Permite cambiar entre varios modelos 3D y ajustar su tamaño, color y rotación
# ----------------------------------
#
# R - reset rotación y escala
# +/- - cambiar tamaño
# C - cambiar color
# M - cambiar modelo
# Q - salir
# ----------------------------------
# Los valores están en radianes (cada paso es 0.1 radianes ≈ 5.7 grados)

import cv2
import numpy as np
import os

def load_obj_file(filepath):
    """
    Carga un archivo OBJ simple y devuelve vértices y caras
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
                    # Manejar diferentes formatos de caras (v, v/vt, v/vt/vn)
                    face_vertices = []
                    for part in parts[1:]:
                        vertex_idx = int(part.split('/')[0]) - 1  # OBJ usa índices base 1
                        face_vertices.append(vertex_idx)
                    if len(face_vertices) >= 3:
                        faces.append(face_vertices)
        
        print(f"Modelo OBJ cargado: {len(vertices)} vértices, {len(faces)} caras")
        return np.array(vertices, dtype=np.float32), faces
    
    except Exception as e:
        print(f"Error cargando archivo OBJ: {e}")
        return None, None

def load_ply_file(filepath):
    """
    Carga un archivo PLY simple
    """
    vertices = []
    faces = []
    
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        # Buscar header
        vertex_count = 0
        face_count = 0
        header_end = 0
        
        for i, line in enumerate(lines):
            if 'element vertex' in line:
                vertex_count = int(line.split()[-1])
            elif 'element face' in line:
                face_count = int(line.split()[-1])
            elif line.strip() == 'end_header':
                header_end = i + 1
                break
        
        # Leer vértices
        for i in range(header_end, header_end + vertex_count):
            if i < len(lines):
                parts = lines[i].split()
                if len(parts) >= 3:
                    x, y, z = float(parts[0]), float(parts[1]), float(parts[2])
                    vertices.append([x, y, z])
        
        # Leer caras
        for i in range(header_end + vertex_count, header_end + vertex_count + face_count):
            if i < len(lines):
                parts = lines[i].split()
                if len(parts) >= 4:  # Primer número es cantidad de vértices en la cara
                    num_vertices = int(parts[0])
                    if len(parts) >= num_vertices + 1:
                        face_vertices = [int(parts[j]) for j in range(1, num_vertices + 1)]
                        faces.append(face_vertices)
        
        print(f"Modelo PLY cargado: {len(vertices)} vértices, {len(faces)} caras")
        return np.array(vertices, dtype=np.float32), faces
    
    except Exception as e:
        print(f"Error cargando archivo PLY: {e}")
        return None, None

def create_simple_cube():
    """
    Crea un cubo simple como ejemplo
    """
    vertices = np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Cara trasera (z=-1)
        [-1, -1, 1],  [1, -1, 1],  [1, 1, 1],  [-1, 1, 1]   # Cara frontal (z=1)
    ], dtype=np.float32)
    
    faces = [
        [0, 1, 2, 3],  # Trasera
        [4, 7, 6, 5],  # Frontal
        [0, 4, 5, 1],  # Inferior
        [2, 6, 7, 3],  # Superior
        [0, 3, 7, 4],  # Izquierda
        [1, 5, 6, 2]   # Derecha
    ]
    
    print("Usando cubo de ejemplo: 8 vértices, 6 caras")
    return vertices, faces

def create_pyramid():
    """
    Crea una pirámide simple
    """
    vertices = np.array([
        [-1, -1, 0],  # Base
        [1, -1, 0],
        [1, 1, 0],
        [-1, 1, 0],
        [0, 0, 2]     # Vértice superior
    ], dtype=np.float32)
    
    faces = [
        [0, 1, 2, 3],  # Base
        [0, 1, 4],     # Cara 1
        [1, 2, 4],     # Cara 2
        [2, 3, 4],     # Cara 3
        [3, 0, 4]      # Cara 4
    ]
    
    print("Usando pirámide de ejemplo: 5 vértices, 5 caras")
    return vertices, faces

def normalize_model(vertices):
    """
    Normaliza el modelo para que tenga un tamaño consistente
    """
    if len(vertices) == 0:
        return vertices
    
    # Calcular el centro del modelo
    center = np.mean(vertices, axis=0)
    centered_vertices = vertices - center
    
    # Calcular el tamaño máximo
    max_distance = np.max(np.linalg.norm(centered_vertices, axis=1))
    
    if max_distance > 0:
        # Normalizar para que el modelo tenga un radio de 1
        normalized_vertices = centered_vertices / max_distance
        return normalized_vertices
    
    return vertices

def project_3d_model(vertices, faces, rvec, tvec, camera_matrix, dist_coeffs,
                     scale=0.02, rot_x=0.0, rot_y=0.0, rot_z=0.0):
    """
    Proyecta un modelo 3D al espacio de la cámara con rotación en X, Y, Z
    """
    try:
        # Normalizar y escalar el modelo
        normalized_vertices = normalize_model(vertices)
        scaled_vertices = normalized_vertices * scale

        # 🔴 Rotación en X
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(rot_x), -np.sin(rot_x)],
            [0, np.sin(rot_x),  np.cos(rot_x)]
        ], dtype=np.float32)

        # 🟢 Rotación en Y
        Ry = np.array([
            [np.cos(rot_y), 0, np.sin(rot_y)],
            [0, 1, 0],
            [-np.sin(rot_y), 0, np.cos(rot_y)]
        ], dtype=np.float32)

        # 🔵 Rotación en Z
        Rz = np.array([
            [np.cos(rot_z), -np.sin(rot_z), 0],
            [np.sin(rot_z),  np.cos(rot_z), 0],
            [0, 0, 1]
        ], dtype=np.float32)

        # ✅ Matriz de rotación combinada
        R = Rx @ Ry @ Rz

        # Aplicar la rotación al modelo
        rotated_vertices = scaled_vertices @ R.T

        # Proyectar vértices 3D a 2D
        projected_points, _ = cv2.projectPoints(
            rotated_vertices, rvec, tvec, camera_matrix, dist_coeffs)

        projected_points = projected_points.reshape(-1, 2).astype(np.int32)

        return projected_points

    except Exception as e:
        print(f"⚠️ Error proyectando modelo: {e}")
        return np.array([])


def draw_3d_model(frame, projected_points, faces, color=(0, 255, 0), thickness=2):
    """
    Dibuja el modelo 3D proyectado en el frame
    """
    if len(projected_points) == 0:
        return
    
    try:
        # Dibujar las caras como líneas
        for face in faces:
            if len(face) >= 3:
                # Verificar que todos los índices sean válidos
                valid_face = True
                for vertex_idx in face:
                    if vertex_idx < 0 or vertex_idx >= len(projected_points):
                        valid_face = False
                        break
                
                if valid_face:
                    # Dibujar las aristas de la cara
                    for i in range(len(face)):
                        start_idx = face[i]
                        end_idx = face[(i + 1) % len(face)]
                        
                        start_point = tuple(projected_points[start_idx])
                        end_point = tuple(projected_points[end_idx])
                        
                        # Verificar que los puntos estén dentro del frame
                        if (0 <= start_point[0] < frame.shape[1] and 0 <= start_point[1] < frame.shape[0] and
                            0 <= end_point[0] < frame.shape[1] and 0 <= end_point[1] < frame.shape[0]):
                            cv2.line(frame, start_point, end_point, color, thickness)
    
    except Exception as e:
        print(f"Error dibujando modelo: {e}")

def main():
    print("Iniciando programa ArUco con modelo 3D...")
    
    # Verificar OpenCV
    print(f"Versión OpenCV: {cv2.__version__}")
    
    # Obtener el directorio donde está el script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_folder = os.path.join(script_dir, "img_aruco")
    
    print(f"Buscando modelos 3D en: {model_folder}")
    
    # Buscar archivos 3D
    model_files = []
    if os.path.exists(model_folder):
        for file in os.listdir(model_folder):
            if file.lower().endswith(('.obj', '.ply')):
                model_files.append(os.path.join(model_folder, file))
        
        if model_files:
            print(f"Archivos 3D encontrados: {[os.path.basename(f) for f in model_files]}")
    
    # Cargar modelo 3D
    vertices = None
    faces = None
    current_model = 0
    
    def load_current_model():
        nonlocal vertices, faces, current_model
        
        if model_files and current_model < len(model_files):
            model_path = model_files[current_model]
            print(f"Cargando modelo: {os.path.basename(model_path)}")
            
            if model_path.lower().endswith('.obj'):
                vertices, faces = load_obj_file(model_path)
            elif model_path.lower().endswith('.ply'):
                vertices, faces = load_ply_file(model_path)
        else:
            # Modelos de ejemplo
            example_models = [create_simple_cube, create_pyramid]
            model_func = example_models[current_model % len(example_models)]
            vertices, faces = model_func()
    
    load_current_model()
    
    if vertices is None or faces is None:
        print("Error: No se pudo cargar ningún modelo 3D")
        return
    
    print(f"Modelo actual: {len(vertices)} vértices, {len(faces)} caras")
    
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
        try:
            aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
            parameters = cv2.aruco.DetectorParameters_create()
            use_new_api = False
            print("Usando API antigua de ArUco")
        except Exception as e:
            print(f"Error configurando ArUco: {e}")
            return
    
    # Tamaño del marcador ArUco en metros
    marker_size = 0.05
    
    # Iniciar cámara
    print("Intentando abrir la cámara...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Intentando cámara 1...")
        cap = cv2.VideoCapture(1)
        
    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara")
        return
    
    print("Cámara abierta correctamente")
    print("Controles:")
    print("- Presiona 'q' para salir")
    print("- Presiona 'c' para cambiar color del modelo")
    print("- Presiona 'm' para cambiar modelo")
    print("- Presiona '+' o '-' para cambiar tamaño")
    print("- Presiona 'r' para reset del tamaño")
    print("- Muestra un marcador ArUco a la cámara")
    
    # Variables de control
    model_scale = 0.03
    color_index = 0
    colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error leyendo frame de la cámara")
            break
        
        frame_count += 1
        
        try:
            # Detectar marcadores ArUco
            if use_new_api:
                corners, ids, rejected = detector.detectMarkers(frame)
            else:
                corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
        except Exception as e:
            print(f"Error detectando marcadores: {e}")
            corners, ids, rejected = [], None, []
        
        # Mostrar información
        color_name = ['Verde', 'Rojo', 'Azul', 'Amarillo', 'Magenta', 'Cian', 'Blanco'][color_index % len(colors)]
        info_text = f"Frame: {frame_count} | ArUcos: {len(ids) if ids is not None else 0} | Escala: {model_scale:.3f} | Color: {color_name}"
        cv2.putText(frame, info_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        if ids is not None and len(ids) > 0:
            try:
                # Dibujar marcadores
                cv2.aruco.drawDetectedMarkers(frame, corners, ids)
                
                # Estimar pose
                pose_estimated = False
                try:
                    if hasattr(cv2.aruco, 'estimatePoseSingleMarkers'):
                        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                            corners, marker_size, camera_matrix, dist_coeffs)
                        pose_estimated = True
                    else:
                        # Método alternativo
                        rvecs, tvecs = [], []
                        for corner in corners:
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
                        pose_estimated = len(rvecs) > 0
                
                except Exception as e:
                    print(f"Error estimando pose: {e}")
                    pose_estimated = False
                
                if pose_estimated:
                    for i in range(min(len(ids), len(rvecs), len(tvecs))):
                        try:
                            # Dibujar ejes del marcador
                            if hasattr(cv2, 'drawFrameAxes'):
                                cv2.drawFrameAxes(frame, camera_matrix, dist_coeffs, 
                                                rvecs[i], tvecs[i], marker_size)
                            elif hasattr(cv2.aruco, 'drawAxis'):
                                cv2.aruco.drawAxis(frame, camera_matrix, dist_coeffs, 
                                                 rvecs[i], tvecs[i], marker_size)
                            
                            # Proyectar y dibujar modelo 3D
                            projected_points = project_3d_model(
                                vertices, faces,
                                rvec, tvec,
                                camera_matrix, dist_coeffs,
                                scale=0.05,
                                rot_x=np.radians(90),   # Rotacion X 🔴
                                rot_y=np.radians(0),   # Rotacion Y 🟢
                                rot_z=np.radians(0)    # Rotacion Z 🔵
                            )

                            
                            if len(projected_points) > 0:
                                draw_3d_model(frame, projected_points, faces, 
                                            colors[color_index % len(colors)], 2)
                            
                        except Exception as e:
                            print(f"Error procesando marcador {i}: {e}")
                            continue
                
            except Exception as e:
                print(f"Error general procesando ArUcos: {e}")
        
        # Instrucciones
        cv2.putText(frame, "q:salir | c:color | m:modelo | +/-:tamaño | r:reset", 
                   (10, frame.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f"Modelo: {current_model} | Vertices: {len(vertices) if vertices is not None else 0}", 
                   (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Mostrar frame
        cv2.imshow('ArUco 3D Model Viewer', frame)
        
        # Controles
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Saliendo...")
            break
        elif key == ord('c'):
            color_index += 1
            color_name = ['Verde', 'Rojo', 'Azul', 'Amarillo', 'Magenta', 'Cian', 'Blanco'][color_index % len(colors)]
            print(f"Color cambiado a: {color_name}")
        elif key == ord('m'):
            current_model += 1
            print(f"Cambiando al modelo {current_model}...")
            load_current_model()
            if vertices is not None:
                print(f"Nuevo modelo cargado: {len(vertices)} vértices, {len(faces)} caras")
        elif key == ord('+') or key == ord('='):
            model_scale *= 1.2
            print(f"Escala aumentada a: {model_scale:.3f}")
        elif key == ord('-'):
            model_scale *= 0.8
            print(f"Escala reducida a: {model_scale:.3f}")
        elif key == ord('r'):
            model_scale = 0.03
            print(f"Escala reseteada a: {model_scale:.3f}")
    
    # Limpiar
    cap.release()
    cv2.destroyAllWindows()
    print("Programa terminado")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error general: {e}")
        import traceback
        traceback.print_exc()
    
    input("Presiona Enter para cerrar...")