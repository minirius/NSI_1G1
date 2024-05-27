from premier_exemple_resolu import tri_pairs

import unittest

class test_tri_pairs(unittest.TestCase):

    def test_ok_vide(self):
        self.assertEqual( tri_pairs([]), [], "(Attendu : [])")
    def test_ok_pairs(self):
        self.assertEqual( tri_pairs([1,2,3,4,5,6,7,8,9,10]),  [2,4,6,8,10], "(Attendu :   [2,4,6,8,10])")

    def test_ok_desordonnee(self):
        self.assertEqual( tri_pairs([10,93,24,55,26,77,38,9,130]), [10,24,26,38,130], "(Attendu : [10,24,26,38,130])")

    def test_ok_impairs(self):
        self.assertEqual( tri_pairs([1,3,5,7,9]), [], "(Attendu : [])")
    
if __name__ == '__main__':
    unittest.main()



