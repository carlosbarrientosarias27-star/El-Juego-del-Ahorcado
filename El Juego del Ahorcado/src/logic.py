import unicodedata

def normalizar_texto(texto):
    """
    Elimina tildes, diéresis y otros modificadores, convirtiendo el texto a mayúsculas.
    
    Es fundamental para permitir que el jugador gane aunque no escriba tildes 
    (ej. que 'Á' se valide con 'A'). Utiliza la normalización NFD para separar 
    los caracteres de sus acentos.

    Args:
        texto (str): La cadena original (ej. "MÉXICO").

    Returns:
        str: La cadena normalizada y en mayúsculas (ej. "MEXICO").
    """
    texto = texto.upper()
    # Transforma 'Á' en 'A', 'É' en 'E', etc.
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
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