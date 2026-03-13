import unittest
from unittest.mock import patch, MagicMock
import sys
import os
import io

# --- SOLUCIÓN PARA VS CODE: Configuración de rutas ---
# Esto permite que el test encuentre las carpetas 'logic', 'database', etc.
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

# Ahora importamos las funciones de main.py
from main import agregar_palabra, menu

class TestMain(unittest.TestCase):

    @patch('main.conectar_db')
    @patch('main.input')
    def test_agregar_palabra_exitosa(self, mock_input, mock_conectar):
        """Prueba que se puede añadir una palabra correctamente."""
        # Configurar mocks
        mock_input.side_effect = ["NARANJA", "FRUTAS", "FACIL"]
        mock_conn = MagicMock()
        mock_conectar.return_value = mock_conn
        
        # Ejecutar y capturar salida
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            agregar_palabra()
            output = fake_out.getvalue()
        
        # Verificaciones
        self.assertIn("Palabra añadida", output)
        mock_conn.cursor().execute.assert_called()
        mock_conn.commit.assert_called()

    @patch('main.input')
    def test_agregar_palabra_invalida(self, mock_input):
        """Prueba que rechaza palabras con números o símbolos."""
        mock_input.return_value = "12345"
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            agregar_palabra()
            output = fake_out.getvalue()
            
        self.assertIn("Error: Solo letras", output)

    @patch('main.jugar')
    @patch('main.input')
    def test_menu_opcion_jugar_y_salir(self, mock_input, mock_jugar):
        """Prueba que la opción 1 llama a jugar y la 4 cierra el programa."""
        # El usuario elige 1 (jugar) y luego 4 (salir)
        mock_input.side_effect = ["1", "4"]
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            menu()
            output = fake_out.getvalue()
            
        # Verificamos que se llamó a la función jugar
        mock_jugar.assert_called_once()
        self.assertIn("¡Gracias por jugar!", output)

    @patch('main.conectar_db')
    @patch('main.input')
    def test_menu_ver_palabras(self, mock_input, mock_conectar):
        """Prueba la visualización de la lista de palabras (Opción 3)."""
        mock_input.side_effect = ["3", "4"]
        
        # Simulamos datos en la DB
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [("PYTHON", "PROGRAMACION")]
        mock_conectar.return_value = mock_conn
        
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            menu()
            output = fake_out.getvalue()
            
        self.assertIn("- PYTHON (PROGRAMACION)", output)

if __name__ == '__main__':
    unittest.main()