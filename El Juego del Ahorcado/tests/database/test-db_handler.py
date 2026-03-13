import unittest
import os
import sys

# Subimos DOS niveles (..) para llegar a la raíz del proyecto
# 1. De 'src' a 'test'
# 2. De 'test' a 'El Juego del Ahorcado'
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(root_path)

# Ahora Python sí encontrará la carpeta 'src' que está en la raíz
from src.database import conectar_db, obtener_palabra_aleatoria

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test. Preparamos un entorno limpio."""
        self.db_path = 'data/palabras.db'
        # La función conectar_db ya crea la carpeta y la tabla, 
        # así que solo la llamamos para inicializar.
        self.conn = conectar_db()

    def tearDown(self):
        """Se ejecuta después de cada test. Cerramos conexión y limpiamos."""
        self.conn.close()
        # Opcional: Eliminar la DB de prueba para que cada test sea 100% independiente
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_conexion_crea_tabla(self):
        """Verifica que la tabla 'palabras' se cree correctamente."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='palabras'")
        tabla = cursor.fetchone()
        self.assertIsNotNone(tabla, "La tabla 'palabras' debería existir.")

    def test_poblacion_inicial(self):
        """Verifica que los datos iniciales se inserten al conectar."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM palabras")
        cantidad = cursor.fetchone()[0]
        self.assertGreater(cantidad, 0, "La base de datos debería tener palabras iniciales.")

    def test_obtener_palabra_aleatoria_sin_filtro(self):
        """Verifica que devuelve una cadena de texto cuando no hay filtro."""
        palabra = obtener_palabra_aleatoria()
        self.assertIsInstance(palabra, str)
        self.assertGreater(len(palabra), 0)

    def test_obtener_palabra_por_categoria(self):
        """Verifica que el filtro por categoría funcione."""
        categoria_test = 'CIENCIA'
        palabra = obtener_palabra_aleatoria(categoria=categoria_test)
        
        # Comprobar que la palabra obtenida pertenece realmente a esa categoría
        cursor = self.conn.cursor()
        cursor.execute("SELECT categoria FROM palabras WHERE palabra = ?", (palabra,))
        res = cursor.fetchone()
        self.assertEqual(res[0], categoria_test)

    def test_obtener_palabra_categoria_inexistente(self):
        """Verifica que devuelve None si la categoría no existe."""
        palabra = obtener_palabra_aleatoria(categoria="CATEGORIA_FANTASMA")
        self.assertIsNone(palabra)

if __name__ == '__main__':
    unittest.main()