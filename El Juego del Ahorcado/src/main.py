try:
    from src.database import conectar_db, obtener_palabra_aleatoria 
    from src.visual import obtener_dibujo, mostrar_progreso 
    from src.logic import validar_letra, comprobar_victoria, normalizar_texto # <--- Añade normalizar_texto
except ModuleNotFoundError:
    from database import conectar_db, obtener_palabra_aleatoria 
    from visual import obtener_dibujo, mostrar_progreso 
    from logic import validar_letra, comprobar_victoria, normalizar_texto # <--- Añade normalizar_texto
    import sqlite3 

def agregar_palabra():
    """
    Interfaz de consola para insertar manualmente una nueva palabra en la base de datos.
    
    Solicita al usuario la palabra, su categoría y su nivel de dificultad. 
    Maneja excepciones en caso de que la palabra ya exista (vía restricción UNIQUE).
    """
    palabra = input("Introduce la palabra: ").upper()
    categoria = input("Introduce la categoría: ").upper()
    dificultad = input("Introduce la dificultad (FACIL/INTERMEDIO/DIFICIL): ").upper()
    
    conn = conectar_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO palabras (palabra, categoria, dificultad) VALUES (?, ?, ?)", 
                       (palabra, categoria, dificultad))
        conn.commit()
        print("¡Palabra añadida con éxito!")
    except:
        print("Error: La palabra ya existe o los datos son incorrectos.")
    finally:
        conn.close()

def jugar():
    """
    Controlador principal de la partida activa.
    
    Realiza las siguientes tareas:
    1. Permite al usuario elegir una categoría.
    2. Gestiona el bucle de juego (máximo 6 errores).
    3. Normaliza la entrada para evitar problemas con tildes.
    4. Actualiza el estado visual (dibujo y progreso) en cada turno.
    5. Determina y muestra el resultado final (Victoria/Derrota).
    """
    # Lógica de selección de categoría
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT categoria FROM palabras")
    categorias = [c[0] for c in cursor.fetchall()]
    conn.close()

    print("\n--- NUEVA PARTIDA ---")
    print(f"Categorías disponibles: {', '.join(categorias)}")
    eleccion = input("Elige una categoría (o pulsa Enter para aleatoria): ").upper()
    
    palabra_original = obtener_palabra_aleatoria(eleccion if eleccion in categorias else None)
    
    if not palabra_original:
        print("No se encontraron palabras.")
        return

    # REFACTOR: Normalización para casos borde (tildes/eñes)
    palabra_objetivo = normalizar_texto(palabra_original) 
    
    # REFACTOR: Uso de sets para mayor velocidad y evitar duplicados
    letras_adivinadas = set() 
    letras_incorrectas = set()
    intentos_max = 6

    while len(letras_incorrectas) < intentos_max:
        print(obtener_dibujo(len(letras_incorrectas)))
        # Muestra el progreso (usamos la original para que se vean las tildes visualmente)
        print(mostrar_progreso(palabra_original, letras_adivinadas))
        print(f"Letras usadas: {', '.join(letras_incorrectas)}")
        
        # Comprobar victoria antes de pedir letra
        if comprobar_victoria(palabra_original, letras_adivinadas):
            print(f"\n¡VICTORIA! La palabra era: {palabra_original}")
            return 

        entrada = input("Introduce una letra: ")
        letra = validar_letra(entrada)
        
        # Caso Borde: Entrada no válida
        if not letra:
            print("❌ Entrada no válida. Introduce solo una letra (A-Z).")
            continue
            
        # Caso Borde: Letra ya intentada
        if letra in letras_adivinadas or letra in letras_incorrectas:
            print(f"⚠️ Ya habías usado la letra '{letra}'.")
            continue

        # Lógica de acierto/error
        if letra in palabra_objetivo:
            print(f"✅ ¡Bien! La '{letra}' está en la palabra.")
            letras_adivinadas.add(letra)
        else:
            print(f"❌ Lo siento, la '{letra}' no está.")
            letras_incorrectas.add(letra)

    # Caso Borde: Fin de intentos (Derrota)
    if len(letras_incorrectas) == intentos_max:
        print(obtener_dibujo(intentos_max))
        print(f"\n💀 ¡DERROTA! La palabra era: {palabra_original}")
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