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
    """
    if not entrada or len(entrada) != 1:
        return None

    # Normalización: convierte 'á' en 'a' + '´' y luego filtramos el acento
    entrada_normalizada = "".join(
        c for c in unicodedata.normalize('NFD', entrada)
        if unicodedata.category(c) != 'Mn'
    )

    if entrada_normalizada.isalpha():
        return entrada_normalizada.upper()
    
    return None
    