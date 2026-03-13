import unittest
import sys
import os

# Ajuste de path para encontrar la carpeta 'ui'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from ui.visuals import obtener_dibujo

class TestVisuals(unittest.TestCase):

    def test_dibujo_inicial(self):
        """Verifica que el estado 0 (inicio) contenga la estructura base sin el personaje."""
        dibujo = obtener_dibujo(0)
        self.assertIn("------", dibujo)
        self.assertNotIn("O", dibujo)  # No debería haber cabeza
        self.assertNotIn("/", dibujo)  # No debería haber extremidades

    def test_dibujo_final(self):
        """Verifica que el estado 6 (derrota) contenga el cuerpo completo."""
        dibujo = obtener_dibujo(6)
        self.assertIn("O", dibujo)    # Cabeza
        self.assertIn("/|\\", dibujo) # Tronco y brazos
        self.assertIn("/ \\", dibujo) # Piernas

    def test_todos_los_estados_son_strings(self):
        """Asegura que todos los niveles (0-6) devuelvan un string válido."""
        for i in range(7):
            with self.subTest(intentos=i):
                dibujo = obtener_dibujo(i)
                self.assertIsInstance(dibujo, str)
                self.assertGreater(len(dibujo), 20)

    def test_indice_fuera_de_rango(self):
        """Verifica que el código lance un error si se piden más de 6 intentos."""
        with self.assertRaises(IndexError):
            obtener_dibujo(7)
    
    def test_limite_exacto_dibujo(self):
        """Asegura que el dibujo 6 es efectivamente el último disponible."""
        with self.assertRaises(IndexError):
            obtener_dibujo(7) # El intento 7 debe dar error porque el juego acaba en el 6

if __name__ == '__main__':
    unittest.main()