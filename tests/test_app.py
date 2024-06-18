import unittest
import os
import sys


# Get the parent directory path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


# Add the parent directory to the beginning of the sys.path list
sys.path.insert(0, parent_dir)


# Now import app from app.py
from app import app

class BasicTests(unittest.TestCase):


    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()


    def tearDown(self):
        pass


    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        response_data_str = response.data.decode('utf-8')
        self.assertIn('Welcome to Our Waste Management Platform', response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        

if __name__ == "__main__":
    unittest.main()
