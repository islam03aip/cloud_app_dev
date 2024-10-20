import unittest
from main import app

class FlaskTestCase(unittest.TestCase):
    
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'task', response.data)
    
    def test_add_task(self):
        tester = app.test_client(self)
        response = tester.post('/add', data=dict(task="Test task"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'task', response.data)

if __name__ == '__main__':
    unittest.main()
