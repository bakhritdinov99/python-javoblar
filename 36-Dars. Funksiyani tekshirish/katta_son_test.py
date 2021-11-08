import unittest
from main import katta_son

class KattaTest(unittest.TestCase):
    def test_katta_son(self):
        self.assertEqual(katta_son(7,25,4),25)
        self.assertEqual(katta_son(100,147,1547),1547)

unittest.main()