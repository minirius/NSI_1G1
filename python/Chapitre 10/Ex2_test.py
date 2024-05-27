import unittest
from Ex2 import tri_distance_croissante

class test_annee_bissextile(unittest.TestCase):
    def test_bad_type_1(self):
        with self.assertRaises(AssertionError):
            tri_distance_croissante([(2,3),(3,1),(8,3),(7,4),(7,5),(2,6),(1,3),(5,8),(12,43),(7,2)], 0)

    def test_bad_type_2(self):
        with self.assertRaises(AssertionError):
            tri_distance_croissante([4, 5, 6, 7, 8], (0, 0))

    def test_bad_type_3(self):
        with self.assertRaises(AssertionError):
            tri_distance_croissante("hello", (0, 0))

    def test_bad_type_4(self):
        with self.assertRaises(AssertionError):
            tri_distance_croissante(1, (0, 0))

    def test_bad_type_5(self):
        with self.assertRaises(AssertionError):
            tri_distance_croissante(None, None)

    def test_good(self):
        self.assertEqual(tri_distance_croissante([(2,3),(3,1),(8,3),(7,4),(7,5),(2,6),(1,3),(5,8),(12,43),(7,2)], (0, 0)), [(3, 1), (1, 3), (2, 3), (2, 6), (7, 2), (7, 4), (7, 5), (5, 8), (8, 3), (12, 43)], 'AssertionError')


if __name__ == '__main__':
    unittest.main()