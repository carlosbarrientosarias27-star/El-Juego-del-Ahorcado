def obtener_dibujo(intentos_fallidos):
    """
    Devuelve la representación gráfica en ASCII del ahorcado según el nivel de error.
    
    Args:
        intentos_fallidos (int): Cantidad de errores actuales (debe estar entre 0 y 6).
        
    Returns:
        str: Un string multilínea con el arte ASCII correspondiente.
    """
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

def mostrar_progreso(palabra, letras_adivinadas):
    """
    Genera la cadena de visualización de la palabra (letras descubiertas y guiones).
    
    Args:
        palabra (str): La palabra original (puede contener tildes).
        letras_adivinadas (iterable): Letras que el usuario ya ha acertado.
        
    Returns:
        str: Una cadena formateada con espacios para facilitar la lectura. 
             Ejemplo: "P Y _ H _ N"
    """
    progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra]
    return f"Palabra: {' '.join(progreso)}"