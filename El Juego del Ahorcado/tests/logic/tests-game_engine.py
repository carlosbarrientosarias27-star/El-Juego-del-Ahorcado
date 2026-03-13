import unittest
from unittest.mock import patch, MagicMock
import io
import sys
import os

# 1. Calculamos la ruta de la raíz (dos niveles arriba de este archivo)
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

# 2. La añadimos al path si no está ya ahí
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

# 3. Ahora las importaciones funcionarán
from logic.game_engine import jugar

class TestGameEngine(unittest.TestCase):

    @patch('logic.game_engine.conectar_db')
    @patch('logic.game_engine.obtener_palabra_aleatoria')
    @patch('logic.game_engine.input')
    def test_victoria_partida(self, mock_input, mock_obtener_palabra, mock_conectar):
        """Prueba una partida completa donde el usuario gana."""
        
        # 1. Simulamos la base de datos para las categorías
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [('ANIMALES',)]
        mock_conectar.return_value = mock_conn
        
        # 2. Forzamos que la palabra secreta sea 'GATO'
        mock_obtener_palabra.return_value = 'GATO'
        
        # 3. Simulamos las entradas del usuario: 
        # Categoria vacía, luego las letras G, A, T, O
        mock_input.side_effect = ['', 'G', 'A', 'T', 'O']
        
        # Redirigimos la salida de consola para que no ensucie el test
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            jugar()
            output = fake_out.getvalue()
            
        # 4. Verificaciones
        self.assertIn("¡VICTORIA!", output)
        self.assertIn("Has adivinado: GATO", output)

    @patch('logic.game_engine.conectar_db')
    @patch('logic.game_engine.obtener_palabra_aleatoria')
    @patch('logic.game_engine.input')
    def test_derrota_partida(self, mock_input, mock_obtener_palabra, mock_conectar):
        """Prueba una partida donde el usuario agota sus intentos."""
        
        mock_conn = MagicMock()
        mock_conectar.return_value = mock_conn
        mock_obtener_palabra.return_value = 'SOL'
        
        # Entradas: Categoría, y luego 6 letras incorrectas seguidas
        mock_input.side_effect = ['', 'Z', 'X', 'Y', 'W', 'V', 'K']
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            jugar()
            output = fake_out.getvalue()
            
        self.assertIn("¡DERROTA!", output)
        self.assertIn("La palabra era: SOL", output)

    @patch('logic.game_engine.obtener_palabra_aleatoria')
    @patch('logic.game_engine.conectar_db')
    def test_sin_palabras_disponibles(self, mock_conectar, mock_obtener_palabra):
        """Prueba el comportamiento cuando la DB no devuelve palabras."""
        mock_obtener_palabra.return_value = None
        
        with patch('logic.game_engine.input', return_value=''), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            jugar()
            output = fake_out.getvalue()
            
        self.assertIn("No se encontraron palabras.", output)

    @patch('logic.game_engine.input')
    def test_entrada_invalida_no_resta_intentos(self, mock_input):
        """Verifica que números o símbolos no resten intentos."""
        # Simula: Categoría aleatoria (''), entrada '#' (basura), y luego ganar con 'A'
        mock_input.side_effect = ['', '#', 'A']
        
        with patch('logic.game_engine.obtener_palabra_aleatoria', return_value='A'), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            jugar()
            output = fake_out.getvalue()
            
        self.assertIn("Entrada no válida", output)
        self.assertIn("¡VICTORIA!", output)

    @patch('logic.game_engine.input')
    def test_letra_repetida_no_resta_intentos(self, mock_input):
        """Verifica que repetir una letra no cuente como error nuevo."""
        # Simula: Categoría '', letra 'Z' (error), letra 'Z' (repetida), luego ganar con 'A'
        mock_input.side_effect = ['', 'Z', 'Z', 'A']
        
        with patch('logic.game_engine.obtener_palabra_aleatoria', return_value='A'), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            jugar()
            output = fake_out.getvalue()
            
        self.assertIn("Ya habías usado la letra 'Z'", output)
        self.assertIn("¡VICTORIA!", output)

if __name__ == '__main__':
    unittest.main()