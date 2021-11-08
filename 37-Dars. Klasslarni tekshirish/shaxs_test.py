import unittest

from shaxs import Shaxs, Talaba

class ShaxsTest(unittest.TestCase):
    def setUp(self):
        ism = "Farrux"
        familya = "Baxritdinov"
        pasport = "AB4225327"
        tyil = 1999

        self.shaxs1 = Shaxs(ism,familya,pasport,tyil)
        self.talaba1 = Talaba("Farrux","Baxritdinov","AB4225327",1999,3884848,"Urgut")

    def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)

    def test_get_info(self):
        info = f"Farrux Baxritdinov. Passport:AB4225327, 1999-yilda tug'ilgan"
        self.assertEqual(self.shaxs1.get_info(), info)

    def test_get_age(self):
        yil = 2021
        self.assertEqual(self.shaxs1.get_age(yil),22)

    def test_isinstance(self):
        self.assertIsInstance(self.talaba1,Shaxs)
