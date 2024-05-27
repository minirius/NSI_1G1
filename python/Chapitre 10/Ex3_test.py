import unittest
from Ex3 import plus_grand_v2 as plus_grand

class test_annee_bissextile(unittest.TestCase):

    def test_good_1(self):
        self.assertEqual(plus_grand(15, 25, 60), 60)

    def test_good_2(self):
        self.assertEqual(plus_grand(15, 25, 10), 25)

    def test_good_3(self):
        self.assertEqual(plus_grand(45, 25, 15), 45)
    
    def test_good_4(self):
        self.assertEqual(plus_grand(45.4, 25.5, 15.7), 45.4)

    def test_good_5(self):
        self.assertEqual(plus_grand(-45, -25, -15), -15)

    def test_bad_type(self):
        with self.assertRaises(TypeError):
            plus_grand('0', 5, [0,5])

if __name__ == '__main__':
    unittest.main()