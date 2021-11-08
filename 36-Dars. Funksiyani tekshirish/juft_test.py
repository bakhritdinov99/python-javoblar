import unittest
from main import juft

class Juft(unittest.TestCase):
    def test_juft(self):
        self.assertEqual(juft([8,9,10,11,12]),[8,10,12])
