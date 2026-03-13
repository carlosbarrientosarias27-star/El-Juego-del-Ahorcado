from logic.game_engine import jugar
from database.db_handler import conectar_db
import sqlite3

def agregar_palabra():
    """
    Solicita al usuario una palabra nueva y la inserta en la base de datos.
 
    Pide interactivamente la palabra, su categoría y su dificultad.
    Valida que la palabra contenga solo letras antes de intentar
    la inserción. Informa al usuario si la operación fue exitosa o si
    ocurrió algún error (por ejemplo, palabra duplicada).
    """
    nueva = input("Introduce la palabra: ").upper()
    if not nueva.isalpha():
        print("Error: Solo letras.")
        return
    cat = input("Categoría: ").upper()
    dif = input("Dificultad: ").upper()
    
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        # Nota: Corregí el error de dedo de tu código original (era dicultad -> dificultad)
        cursor.execute("INSERT INTO palabras (palabra, categoria, dificultad) VALUES (?, ?, ?)", (nueva, cat, dif))
        conn.commit()
        print("Palabra añadida.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def menu():
    """
    Punto de entrada visual de la aplicación.
    
    Gestiona el bucle infinito del menú principal, permitiendo al usuario navegar
    entre jugar, añadir contenido, listar la base de datos o cerrar el programa.
    """
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