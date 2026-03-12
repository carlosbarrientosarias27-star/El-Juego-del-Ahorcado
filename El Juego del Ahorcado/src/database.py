import sqlite3 
import os 

def conectar_db():
    """
    Establece la conexión con la base de datos SQLite y asegura la existencia de la tabla.
    
    Crea el directorio 'data' si no existe, inicializa la tabla 'palabras' y 
    realiza una población inicial de datos si la tabla está vacía.
    
    Returns:
        sqlite3.Connection: Objeto de conexión a la base de datos.
    """
    if not os.path.exists('data'):
        os.makedirs('data')
    
    conexion = sqlite3.connect('data/palabras.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT UNIQUE NOT NULL,
            categoria TEXT NOT NULL,
            dificultad TEXT NOT NULL
        )
    ''')
    
    palabras_iniciales = [
        ('PYTHON', 'PROGRAMACION', 'FACIL'), ('SQLITE', 'PROGRAMACION', 'INTERMEDIO'),
        ('ALGORITMO', 'PROGRAMACION', 'DIFICIL'), ('TECLADO', 'TECNOLOGIA', 'FACIL'),
        ('MONITOR', 'TECNOLOGIA', 'FACIL'), ('ELEFANTE', 'ANIMALES', 'FACIL'),
        ('JIRAFA', 'ANIMALES', 'FACIL'), ('ESPAÑA', 'GEOGRAFIA', 'FACIL'),
        ('ARGENTINA', 'GEOGRAFIA', 'INTERMEDIO'), ('HIDROGENO', 'CIENCIA', 'DIFICIL'),
        ('OXIGENO', 'CIENCIA', 'FACIL'), ('PANDEMIA', 'SALUD', 'INTERMEDIO'),
        ('GUITARRA', 'MUSICA', 'INTERMEDIO'), ('VIOLIN', 'MUSICA', 'INTERMEDIO'),
        ('MANZANA', 'FRUTAS', 'FACIL'), ('MELOCOTON', 'FRUTAS', 'INTERMEDIO'),
        ('MURCIELAGO', 'ANIMALES', 'DIFICIL'), ('DICCIONARIO', 'LENGUA', 'INTERMEDIO'),
        ('UNIVERSO', 'CIENCIA', 'FACIL'), ('ESTRELLA', 'CIENCIA', 'FACIL')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO palabras (palabra, categoria, dificultad) VALUES (?, ?, ?)', palabras_iniciales)
    conexion.commit()
    return conexion

def inicializar_db():
    """
    Crea la estructura de la base de datos y carga los datos por defecto.
    
    Esta función está diseñada para ejecutarse una sola vez al inicio del ciclo
    de vida de la aplicación para garantizar que el esquema de la tabla y los 
    registros base estén presentes.
    """
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS palabras (...)''')
        # ... (resto de tu lógica de población inicial)
        conn.commit()

def obtener_palabra_aleatoria(categoria=None):
    """
    Recupera una palabra aleatoria de la base de datos.
    
    Args:
        categoria (str, optional): Categoría específica para filtrar la búsqueda. 
                                   Si es None, elige de cualquier categoría.
    
    Returns:
        str: La palabra seleccionada o None si no se encuentran resultados.
    """
    conn = conectar_db()
    cursor = conn.cursor()
    
    if categoria:
        cursor.execute("SELECT palabra FROM palabras WHERE categoria = ? ORDER BY RANDOM() LIMIT 1", (categoria,))
    else:
        cursor.execute("SELECT palabra FROM palabras ORDER BY RANDOM() LIMIT 1")
    
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None