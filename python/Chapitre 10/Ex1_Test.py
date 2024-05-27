import unittest
from Ex1 import anne_bissextile

class test_annee_bissextile(unittest.TestCase):
    def test_nbr_negatif(self):
        self.assertRaises('AssertionError', anne_bissextile(-100))

    def test_nbr_float(self):
        self.assertRaises('AssertionError', anne_bissextile(2020.5))

    def test_nbr_null(self):
        self.assertTrue(anne_bissextile(0))

    def test_nbr_bissextile(self):
        self.assertTrue(anne_bissextile(2024))

    def test_nbr_bissextile_400(self):
        self.assertTrue(anne_bissextile(1600))

    def test_nbr_bissextile_100(self):
        self.assertFalse(anne_bissextile(1700))

    def test_nbr_aleatoire(self):
        self.assertAlmostEqual(first, second)

if __name__ == '__main__':
    unittest.main()