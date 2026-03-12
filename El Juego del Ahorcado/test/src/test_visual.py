import unittest
import os
import sys

# Configuración de ruta para encontrar 'src'
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_raiz = os.path.join(directorio_actual, "..", "..")
sys.path.insert(0, os.path.abspath(ruta_raiz))

from src.visual import obtener_dibujo, mostrar_progreso

class TestVisual(unittest.TestCase):

    def test_obtener_dibujo_inicial(self):
        """Verifica que el dibujo inicial (0 intentos) no tenga la cabeza."""
        dibujo = obtener_dibujo(0)
        # CORRECCIÓN: Usamos assertNotIn para verificar ausencia
        self.assertNotIn("O", dibujo, "El dibujo inicial no debería tener la cabeza 'O'")
        self.assertIsInstance(dibujo, str)

    def test_obtener_dibujo_final(self):
        """Verifica que el dibujo final (6 intentos) contenga el cuerpo completo."""
        dibujo = obtener_dibujo(6)
        self.assertIn("O", dibujo)
        # CORRECCIÓN: Buscamos la representación real del cuerpo y las piernas
        # En el dibujo final de visual.py, el tronco y brazos se ven como "/|\\"
        self.assertIn("/|\\", dibujo) 
        self.assertIn("/ \\", dibujo)

    def test_mostrar_progreso_vacio(self):
        """Verifica la visualización sin letras adivinadas."""
        palabra = "PYTHON"
        letras_adivinadas = []
        resultado = mostrar_progreso(palabra, letras_adivinadas)
        self.assertEqual(resultado, "Palabra: _ _ _ _ _ _")

    def test_mostrar_progreso_parcial(self):
        """Verifica la visualización con algunas letras adivinadas."""
        palabra = "SQLITE"
        letras_adivinadas = ["S", "L", "E"]
        resultado = mostrar_progreso(palabra, letras_adivinadas)
        self.assertEqual(resultado, "Palabra: S _ L _ _ E")

if __name__ == '__main__':
    unittest.main()