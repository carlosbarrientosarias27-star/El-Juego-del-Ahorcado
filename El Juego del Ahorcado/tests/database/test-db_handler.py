import unittest
import os
import sqlite3
import sys
import os

# Añade la carpeta raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
# Ahora sí encontrará 'database'
from database.db_handler import conectar_db, obtener_palabra_aleatoria

class TestDBHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta antes de todas las pruebas para asegurar un entorno limpio."""
        # Si existe una DB de prueba previa, la borramos para empezar de cero
        if os.path.exists('data/palabras.db'):
            pass # O podrías borrarla si prefieres un test totalmente aislado

    def test_1_conexion_y_creacion(self):
        """Prueba que la conexión se cree y la tabla exista con datos iniciales."""
        conn = conectar_db()
        self.assertIsInstance(conn, sqlite3.Connection)
        
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM palabras")
        count = cursor.fetchone()[0]
        
        # Verificamos que al menos se insertaron las 20 palabras iniciales
        self.assertGreaterEqual(count, 20)
        conn.close()

    def test_2_obtener_palabra_aleatoria(self):
        """Prueba que se obtenga una palabra (no sea None)."""
        palabra = obtener_palabra_aleatoria()
        self.assertIsNotNone(palabra)
        self.assertIsInstance(palabra, str)

    def test_3_obtener_palabra_por_categoria(self):
        """Prueba el filtrado por categoría."""
        categoria_test = 'CIENCIA'
        palabra = obtener_palabra_aleatoria(categoria=categoria_test)
        
        # Verificamos que la palabra obtenida realmente pertenezca a esa categoría
        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute("SELECT categoria FROM palabras WHERE palabra = ?", (palabra,))
        res = cursor.fetchone()
        conn.close()
        
        self.assertEqual(res[0], categoria_test)

    def test_4_categoria_inexistente(self):
        """Prueba que retorne None si la categoría no existe."""
        palabra = obtener_palabra_aleatoria(categoria="CATEGORIA_FANTASMA")
        self.assertIsNone(palabra)

    def test_5_limite_palabra_aleatoria(self):
        """Verifica que el sistema no falle si se pide una palabra en una DB vacía."""
        # Caso borde: Intentar obtener palabra de una categoría que no existe
        palabra = obtener_palabra_aleatoria(categoria="NO_EXISTO")
        self.assertIsNone(palabra)    

if __name__ == '__main__':
    unittest.main()