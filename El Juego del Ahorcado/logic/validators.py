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