import unittest
from main import katta_harf

class KattaTest(unittest.TestCase):
    def test_katta_harf(self):
        self.assertEqual(katta_harf(['salom','alik']),['Salom','Alik'])
        self.assertEqual(katta_harf(['Daryo', 'kun']), ['Daryo', 'Kun'])
