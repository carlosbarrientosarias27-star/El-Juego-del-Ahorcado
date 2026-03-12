def validar_letra(entrada):
    """Valida que la entrada sea una sola letra del alfabeto."""
    entrada = entrada.lower()
    if len(entrada) == 1 and entrada.isalpha():
        return entrada.upper() 
    return None

def comprobar_victoria(palabra, letras_adivinadas):
    return all(letra in letras_adivinadas for letra in palabra)