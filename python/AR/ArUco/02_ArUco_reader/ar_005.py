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
        
        print(f"Modelo cargado: {len(vertices)} vértices, {len(faces)} caras")
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
            parts = lines[i].split()
            if len(parts) >= 3:
                x, y, z = float(parts[0]), float(parts[1]), float(parts[2])
                vertices.append([x, y, z])
        
        # Leer caras
        for i in range(header_end + vertex_count, header_end + vertex_count + face_count):
            parts = lines[i].split()
            if len(parts) >= 4:  # Primer número es cantidad de vértices en la cara
                face_vertices = [int(parts[j]) for j in range(1, int(parts[0]) + 1)]
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
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Cara trasera
        [-1, -1, 1],  [1, -1, 1],  [1, 1, 1],  [-1, 1, 1]   # Cara frontal
    ], dtype=np.float32)
    
    faces = [
        [0, 1, 2, 3],  # Trasera
        [4, 7, 6, 5],  # Frontal
        [0, 4, 5, 1],  # Inferior
        [2, 6, 7, 3],  # Superior
        [0, 3, 7, 4],  # Izquierda
        [1, 5, 6, 2]   # Derecha
    ]
    
    return vertices, faces

def project_3d_model(vertices, faces, rvec, tvec, camera_matrix, dist_coeffs, scale=0.02):
    """
    Proyecta un modelo 3D al espacio de la cámara
    """
    # Escalar el modelo
    scaled_vertices = vertices * scale
    
    # Proyectar vértices 3D a 2D
    projected_points, _ = cv2.projectPoints(
        scaled_vertices, rvec, tvec, camera_matrix, dist_coeffs)
    
    projected_points = projected_points.reshape(-1, 2).astype(np.int32)
    
    return projected_points

def draw_3d_model(frame, projected_points, faces, color=(0, 255, 0), thickness=2):
    """
    Dibuja el modelo 3D proyectado en el frame
    """
    # Dibujar las caras como líneas
    for face in faces:
        if len(face) >= 3:
            # Dibujar las aristas de la cara
            for i in range(len(face)):
                start_idx = face[i]
                end_idx = face[(i + 1) % len(face)]
                
                if start_idx < len(projected_points) and end_idx < len(projected_points):
                    start_point = tuple(projected_points[start_idx])
                    end_point = tuple(projected_points[end_idx])
                    cv2.line(frame, start_point, end_point, color, thickness)

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
        
        print(f"Archivos 3D encontrados: {[os.path.basename(f) for f in model_files]}")
    
    # Cargar modelo 3D
    vertices = None
    faces = None
    
    if model_files:
        model_path = model_files[0]  # Usar el primer modelo encontrado
        print(f"Cargando modelo: {os.path.basename(model_path)}")
        
        if model_path.lower().endswith('.obj'):
            vertices, faces = load_obj_file(model_path)
        elif model_path.lower().endswith('.ply'):
            vertices, faces = load_ply_file(model_path)
    else:
        print("No se encontraron archivos 3D (.obj o .ply)")
        print("Usando cubo de ejemplo...")
        vertices, faces = create_simple_cube()
    
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
    
    print("Cámara abierta correctamente")
    print("Controles:")
    print("- Presiona 'q' para salir")
    print("- Presiona 'c' para cambiar color del modelo")
    print("- Presiona '+' o '-' para cambiar tamaño")
    print("- Muestra un marcador ArUco a la cámara")
    
    # Variables de control
    model_scale = 0.02
    color_index = 0
    colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detectar marcadores ArUco
        if use_new_api:
            corners, ids, rejected = detector.detectMarkers(frame)
        else:
            corners, ids, rejected = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)
        
        # Mostrar información
        info_text = f"Modelo 3D | ArUcos: {len(ids) if ids is not None else 0} | Escala: {model_scale:.3f}"
        cv2.putText(frame, info_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
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
                    
                    # Proyectar y dibujar modelo 3D
                    projected_points = project_3d_model(
                        vertices, faces, rvecs[i], tvecs[i], 
                        camera_matrix, dist_coeffs, model_scale)
                    
                    draw_3d_model(frame, projected_points, faces, 
                                colors[color_index % len(colors)], 2)
                    
            except Exception as e:
                print(f"Error estimando pose: {e}")
        
        # Instrucciones
        cv2.putText(frame, "q:salir | c:color | +/-:tamaño", 
                   (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Mostrar frame
        cv2.imshow('ArUco 3D Model Viewer', frame)
        
        # Controles
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            color_index += 1
            print(f"Color cambiado a: {colors[color_index % len(colors)]}")
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