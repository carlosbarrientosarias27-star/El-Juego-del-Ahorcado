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