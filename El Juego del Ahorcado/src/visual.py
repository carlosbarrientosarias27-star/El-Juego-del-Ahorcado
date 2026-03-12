def obtener_dibujo(intentos_fallidos):
    """
    Proporciona la representación visual en ASCII del ahorcado.
    
    Args:
        intentos_fallidos (int): Número de errores cometidos (0 a 6).
        
    Returns:
        str: El dibujo correspondiente al estado actual del juego.
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
    Crea una representación visual de la palabra con guiones bajos para letras ocultas.
    
    Args:
        palabra (str): La palabra completa a mostrar.
        letras_adivinadas (list): Letras que el usuario ya ha descubierto.
        
    Returns:
        str: Cadena formateada (ej. "P _ T _ O N").
    """
    progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra]
    return f"Palabra: {' '.join(progreso)}"