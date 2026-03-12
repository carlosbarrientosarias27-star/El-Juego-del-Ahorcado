import sqlite3
import random
import os
import re

# --- CONFIGURACIÓN DE BASE DE DATOS (Commits 2, 7, 9) ---

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

# --- LÓGICA DE VALIDACIÓN (Commit 8) ---

def validar_letra(entrada):
    """Valida que la entrada sea una sola letra del alfabeto."""
    entrada = entrada.lower()
    if len(entrada) == 1 and entrada.isalpha():
        return entrada
    return None

# --- ARTE ASCII (Commit 5) ---

def obtener_dibujo(intentos_fallidos):
    """Devuelve el estado del ahorcado basado en errores."""
    estados = [
        """
           ------
           |    |
           |
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        ---------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ---------
        """
    ]
    return estados[intentos_fallidos]

# --- FUNCIONES DE JUEGO (Commits 3, 4, 6, 9) ---

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

def jugar():
    """Bucle principal de la partida."""
    # Selección de categoría (Commit 9)
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT categoria FROM palabras")
    categorias = [c[0] for c in cursor.fetchall()]
    conn.close()

    print("\n--- NUEVA PARTIDA ---")
    print(f"Categorías disponibles: {', '.join(categorias)}")
    eleccion = input("Elige una categoría (o pulsa Enter para aleatoria): ").upper()
    
    palabra_objetivo = obtener_palabra_aleatoria(eleccion if eleccion in categorias else None)
    
    if not palabra_objetivo:
        print("No se encontraron palabras.")
        return

    letras_adivinadas = []
    letras_incorrectas = []
    intentos_max = 6
    errores = 0

    while errores < intentos_max:
        print(obtener_dibujo(errores))
        
        # Mostrar palabra oculta (Commit 3)
        progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_objetivo]
        print(f"Palabra: {' '.join(progreso)}")
        print(f"Letras usadas: {', '.join(letras_incorrectas)}")
        
        # Victoria (Commit 6)
        if "_" not in progreso:
            print(f"\n¡VICTORIA! Has adivinado: {palabra_objetivo}")
            break
            
        letra = validar_letra(input("Introduce una letra: "))
        
        if not letra:
            print("Entrada no válida. Introduce solo una letra.")
            continue
            
        letra = letra.upper()

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print(f"Ya habías usado la letra '{letra}'.")
            continue

        if letra in palabra_objetivo:
            print(f"¡Bien! La '{letra}' está en la palabra.")
            letras_adivinadas.append(letra)
        else:
            print(f"Lo siento, la '{letra}' no está.")
            letras_incorrectas.append(letra)
            errores += 1

    if errores == intentos_max:
        print(obtener_dibujo(errores))
        print(f"\n¡DERROTA! La palabra era: {palabra_objetivo}")

# --- GESTIÓN DE PALABRAS (Commit 7, 10) ---

def agregar_palabra():
    """Añade una nueva palabra a la base de datos con validaciones."""
    nueva = input("Introduce la palabra: ").upper()
    if not nueva.isalpha():
        print("Error: La palabra solo debe contener letras.")
        return
        
    cat = input("Categoría: ").upper()
    dif = input("Dificultad (FACIL/INTERMEDIO/DIFICIL): ").upper()
    
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO palabras (palabra, categoria, dicultad) VALUES (?, ?, ?)", (nueva, cat, dif))
        conn.commit()
        print(f"Palabra '{nueva}' añadida con éxito.")
    except sqlite3.IntegrityError:
        print("Error: La palabra ya existe en la base de datos.")
    except Exception as e:
        print(f"Error de base de datos: {e}")
    finally:
        conn.close()

# --- MENÚ PRINCIPAL (Commit 10) ---

def menu():
    while True:
        print("\n=== JUEGO DEL AHORCADO CON SQLITE ===")
        print("1. Jugar")
        print("2. Añadir nueva palabra")
        print("3. Ver todas las palabras")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            jugar()
        elif opcion == "2":
            agregar_palabra()
        elif opcion == "3":
            conn = conectar_db()
            cursor = conn.cursor()
            cursor.execute("SELECT palabra, categoria FROM palabras")
            for p in cursor.fetchall():
                print(f"- {p[0]} ({p[1]})")
            conn.close()
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()