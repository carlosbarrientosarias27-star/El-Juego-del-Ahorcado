import unittest
import sys
import os

# Aseguramos que Python encuentre la carpeta 'logic'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from logic.validators import validar_letra

class TestValidators(unittest.TestCase):

    def test_letra_valida_minuscula(self):
        """Debe aceptar una letra minúscula y devolverla en mayúscula."""
        self.assertEqual(validar_letra("a"), "A")

    def test_letra_valida_mayuscula(self):
        """Debe aceptar una letra mayúscula y devolverla en mayúscula."""
        self.assertEqual(validar_letra("Z"), "Z")

    def test_entrada_vacia(self):
        """Debe devolver None si la entrada está vacía."""
        self.assertIsNone(validar_letra(""))

    def test_multiples_caracteres(self):
        """Debe rechazar entradas de más de un carácter."""
        self.assertIsNone(validar_letra("ab"))

    def test_numeros(self):
        """Debe rechazar números."""
        self.assertIsNone(validar_letra("1"))

    def test_caracteres_especiales(self):
        """Debe rechazar símbolos y caracteres especiales."""
        self.assertIsNone(validar_letra("@"))
        self.assertIsNone(validar_letra(" "))
    
    def test_normalizacion_tildes(self):
        """Prueba que las tildes se validen correctamente."""
        # Nota: Con tu código actual esto fallará (es un 'buen' fallo para detectar mejoras)
        self.assertEqual(validar_letra("á"), "A")
        self.assertEqual(validar_letra("é"), "E")

if __name__ == '__main__':
    unittest.main()