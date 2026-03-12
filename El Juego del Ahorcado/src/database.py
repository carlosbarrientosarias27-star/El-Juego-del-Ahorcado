import sqlite3 
import os 

def conectar_db():
    """Establece conexión con SQLite y crea la tabla si no existe."""
    if not os.path.exists('data'):
        os.makedirs('data')
    
    conexion = sqlite3.connect('data/palabras.db')
    cursor = conexion.cursor()
    
    # Crear tabla con campos: id, palabra, categoria, dificultad (Commit 2)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT UNIQUE NOT NULL,
            categoria TEXT NOT NULL,
            dificultad TEXT NOT NULL
        )
    ''')
    
    # Población inicial de la BD (Commit 2)
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
    
    # Insert OR IGNORE para evitar duplicados (Commit 7)
    cursor.executemany('INSERT OR IGNORE INTO palabras (palabra, categoria, dificultad) VALUES (?, ?, ?)', palabras_iniciales)
    conexion.commit()
    return conexion

def obtener_palabra_aleatoria(categoria=None):
    """Obtiene una palabra de la BD, opcionalmente filtrada por categoría."""
    conn = conectar_db()
    cursor = conn.cursor()
    
    if categoria:
        cursor.execute("SELECT palabra FROM palabras WHERE categoria = ? ORDER BY RANDOM() LIMIT 1", (categoria,))
    else:
        cursor.execute("SELECT palabra FROM palabras ORDER BY RANDOM() LIMIT 1")
    
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None