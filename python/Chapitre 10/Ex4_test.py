import unittest
from Ex4 import premier

class test_annee_bissextile(unittest.TestCase):

    def test_good_1(self):
        self.assertEqual(premier(1), False)

    def test_good_2(self):
        self.assertEqual(premier(3), True)

    def test_good_2(self):
        self.assertEqual(premier(-3), True)

    def test_good_3(self):
        self.assertEqual(premier(17), True)
    
    def test_good_4(self):
        self.assertEqual(premier(20), False)

    def test_bad_type_1(self):
        with self.assertRaises(TypeError):
            premier('0')

    def test_bad_type_2(self):
        with self.assertRaises(TypeError):
            premier([0, '4'])

if __name__ == '__main__':
    unittest.main()