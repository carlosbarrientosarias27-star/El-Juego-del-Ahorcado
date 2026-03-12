import unittest
import sys
import os

# Configuración de rutas para encontrar 'src'
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_raiz = os.path.join(directorio_actual, "..", "..")
sys.path.insert(0, os.path.abspath(ruta_raiz))

from src.logic import validar_letra, comprobar_victoria 

class TestLogic(unittest.TestCase):

    def test_validar_letra_formato(self):
        """
        CORRECCIÓN: validar_letra solo recibe la LETRA.
        Verifica que la función devuelve la letra procesada (ej. en mayúsculas).
        """
        entrada = "p"
        resultado = validar_letra(entrada)
        # Ajusta esto según lo que haga tu función: ¿Devuelve la letra o un Booleano?
        # Si devuelve la letra en mayúsculas:
        self.assertEqual(resultado, "P", "La función debería normalizar la letra a mayúsculas")

    def test_comprobar_victoria_exitosa(self):
        """Verifica que el juego detecta cuando se han adivinado todas las letras."""
        palabra_objetivo = "SOL"
        letras_adivinadas = ["S", "O", "L"]
        self.assertTrue(comprobar_victoria(palabra_objetivo, letras_adivinadas))

    def test_no_victoria_incompleta(self):
        """
        CORRECCIÓN: Usamos 'BARCO' porque todas sus letras son únicas.
        Si falta la 'O', debe devolver False.
        """
        palabra_objetivo = "BARCO"
        letras_adivinadas = ["B", "A", "R", "C"]
        # Esto ahora sí devolverá False correctamente
        self.assertFalse(comprobar_victoria(palabra_objetivo, letras_adivinadas), "Debería ser False porque falta la letra O")

    def test_victoria_con_letras_repetidas(self):
        """Verifica que 'CASA' se gane solo con C, A, S."""
        palabra = "CASA"
        letras = ["C", "A", "S"]
        self.assertTrue(comprobar_victoria(palabra, letras), "En CASA, adivinar la 'A' cubre ambas posiciones")

if __name__ == '__main__':
    unittest.main()