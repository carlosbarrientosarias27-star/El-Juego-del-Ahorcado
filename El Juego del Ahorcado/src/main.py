from database import conectar_db, obtener_palabra_aleatoria 
from visual import obtener_dibujo, mostrar_progreso 
from logic import validar_letra, comprobar_victoria 

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