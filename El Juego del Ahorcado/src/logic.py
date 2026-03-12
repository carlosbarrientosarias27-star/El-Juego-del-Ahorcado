def validar_letra(entrada):
    """
    Verifica que la entrada del usuario sea un único carácter alfabético.
    
    Args:
        entrada (str): La cadena introducida por el usuario.
        
    Returns:
        str: La letra en mayúsculas si es válida, None en caso contrario.
    """
    entrada = entrada.lower()
    if len(entrada) == 1 and entrada.isalpha():
        return entrada.upper() 
    return None

def comprobar_victoria(palabra, letras_adivinadas):
    """
    Evalúa si todas las letras de la palabra objetivo han sido adivinadas.
    
    Args:
        palabra (str): La palabra que se debe adivinar.
        letras_adivinadas (list): Lista de letras que el jugador ha acertado.
        
    Returns:
        bool: True si la palabra está completa, False de lo contrario.
    """
    return all(letra in letras_adivinadas for letra in palabra)