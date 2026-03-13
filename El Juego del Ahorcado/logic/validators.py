import unicodedata 
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
    
    import unicodedata

def validar_letra(entrada):
    """
    Verifica que la entrada sea un único carácter alfabético y elimina tildes.
 
    Normaliza la entrada usando Unicode NFD para separar los caracteres base
    de sus diacríticos (tildes, diéresis, etc.) y los filtra, permitiendo
    que letras como 'á' o 'ñ' sean tratadas como 'a' y 'n' respectivamente.
 
    Args:
        entrada (str): La cadena introducida por el usuario.
 
    Returns:
        str: La letra normalizada en mayúsculas si es válida, None en caso contrario.
    """
    # comprobar que existe y que solo tiene 1 carácter
    if not entrada or len(entrada) != 1:
        return None

    # normalizar la letra (quitar tildes)
    texto = unicodedata.normalize('NFD', entrada)

    entrada_normalizada = ""
    for caracter in texto:
        if unicodedata.category(caracter) != 'Mn':
            entrada_normalizada += caracter

    # comprobar que sigue siendo una letra
    if entrada_normalizada.isalpha():
        return entrada_normalizada.upper()

    return None
    