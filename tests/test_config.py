import unittest
import os
import sys

import unittest

# Get the parent directory path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


# Add the parent directory to the beginning of the sys.path list
sys.path.insert(0, parent_dir)

from config import Config  

class TestConfig(unittest.TestCase):

    def test_secret_key(self):
        config = Config()
        self.assertEqual(config.SECRET_KEY, '5791628bb0b13ce0c676dfde280ba245')

    def test_database_uri(self):
        config = Config()
        self.assertEqual(config.SQLALCHEMY_DATABASE_URI, 'sqlite:///site.db')

    def test_track_modifications(self):
        config = Config()
        self.assertFalse(config.SQLALCHEMY_TRACK_MODIFICATIONS)

if __name__ == '__main__':
    unittest.main()
