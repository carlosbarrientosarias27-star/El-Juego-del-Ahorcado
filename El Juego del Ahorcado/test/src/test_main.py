import unittest
import os
import sys
from unittest.mock import patch, MagicMock

# 1. Configuración de rutas para encontrar 'src'
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_raiz = os.path.abspath(os.path.join(directorio_actual, "..", ".."))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

# 2. Importación del módulo main
import src.main as main

class TestMain(unittest.TestCase):

    @patch('src.main.conectar_db')
    @patch('builtins.input')
    def test_agregar_palabra_exito(self, mock_input, mock_db):
        """Prueba que agregar_palabra inserta datos correctamente en la DB."""
        # Simulamos las entradas del usuario: Palabra, Categoría, Dificultad
        mock_input.side_effect = ["TEST", "CATEGORIA_TEST", "FACIL"]
        
        # Simulamos el comportamiento de la base de datos
        mock_conn = MagicMock()
        mock_db.return_value = mock_conn
        
        main.agregar_palabra()
        
        # Verificamos que se intentó insertar en la base de datos
        mock_conn.cursor().execute.assert_called()
        mock_conn.commit.assert_called_once()

    @patch('src.main.obtener_palabra_aleatoria')
    @patch('src.main.conectar_db')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_jugar_victoria_rapida(self, mock_print, mock_input, mock_db, mock_palabra):
        """Simula una partida donde el usuario gana rápidamente."""
        # 1. Mock de la DB para las categorías
        mock_conn = MagicMock()
        mock_db.return_value = mock_conn
        mock_conn.cursor().fetchall.return_value = [("CIENCIA",)]
        
        # 2. Mock de la palabra seleccionada
        mock_palabra.return_value = "SOL"
        
        # 3. Simulamos entradas: Categoría "CIENCIA", letras "S", "O", "L"
        mock_input.side_effect = ["CIENCIA", "S", "O", "L"]
        
        main.jugar()
        
        # Verificamos que el mensaje de VICTORIA se haya impreso
        # Buscamos si alguno de los prints llamados contiene la palabra "VICTORIA"
        llamadas_print = [call.args[0] for call in mock_print.call_args_list if call.args]
        victoria_detectada = any("VICTORIA" in s for s in llamadas_print)
        
        self.assertTrue(victoria_detectada, "El juego debería terminar en victoria para la palabra SOL")

    @patch('builtins.input')
    def test_menu_salir(self, mock_input):
        """Verifica que la opción 4 del menú cierra el programa."""
        # Simulamos que el usuario presiona "4"
        mock_input.return_value = "4"
        
        # Si el menú no fuera un bucle infinito protegido, esto terminaría
        with patch('builtins.print') as mock_p:
            main.menu()
            # Verificamos el mensaje de despedida
            mock_p.assert_any_call("¡Gracias por jugar!")

if __name__ == '__main__':
    unittest.main()