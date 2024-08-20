# tests/test_app.py
import unittest
from app import create_app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        """Preparar el entorno de prueba."""
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_index_route(self):
        """Probar que la ruta index carga correctamente."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Data in Redis:', response.data.decode())

    def test_add_data_route(self):
        """Probar la adición de datos a través del formulario."""
        response = self.client.post('/add', data={'data': 'test data'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('test data', response.data.decode())

if __name__ == '__main__':
    unittest.main()
