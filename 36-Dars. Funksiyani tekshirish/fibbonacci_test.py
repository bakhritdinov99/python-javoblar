import unittest
from main import fibbonacci

class Fibbonacci(unittest.TestCase):
    def test_fibb(self):
        self.assertEqual(fibbonacci(5),True)
        self.assertEqual(fibbonacci(6),False)