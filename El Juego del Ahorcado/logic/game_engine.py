from database.db_handler import conectar_db, obtener_palabra_aleatoria
from ui.visuals import obtener_dibujo
from logic.validators import validar_letra
import sqlite3
import unicodedata 

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
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT categoria FROM palabras")
    categorias = [c[0] for c in cursor.fetchall()]
    conn.close()

    print("\n--- NUEVA PARTIDA ---")
    print(f"Categorías disponibles: {', '.join(categorias)}")
    eleccion = input("Elige una categoría (o pulsa Enter para aleatoria): ").upper()
    
    palabra_objetivo = obtener_palabra_aleatoria(eleccion if eleccion in categorias else None)

    if palabra_objetivo:
    # Normalizamos la palabra secreta para que no tenga tildes
        palabra_objetivo = "".join(
        c for c in unicodedata.normalize('NFD', palabra_objetivo)
        if unicodedata.category(c) != 'Mn'
    ).upper()
    
    if not palabra_objetivo:
        print("No se encontraron palabras.")
        return

    letras_adivinadas = []
    letras_incorrectas = []
    intentos_max = 6
    errores = 0

    while errores < intentos_max:
        print(obtener_dibujo(errores))
        progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra_objetivo]
        print(f"Palabra: {' '.join(progreso)}")
        
        if "_" not in progreso:
            print(f"\n¡VICTORIA! Has adivinado: {palabra_objetivo}")
            break
            
        letra = validar_letra(input("Introduce una letra: "))
        if not letra:
            print("Entrada no válida.")
            continue
            
        letra = letra.upper()
        if letra in letras_adivinadas or letra in letras_incorrectas:
            print(f"Ya habías usado la letra '{letra}'.")
            continue

        if letra in palabra_objetivo:
            letras_adivinadas.append(letra)
        else:
            letras_incorrectas.append(letra)
            errores += 1

    if errores == intentos_max:
        print(obtener_dibujo(errores))
        print(f"\n¡DERROTA! La palabra era: {palabra_objetivo}")