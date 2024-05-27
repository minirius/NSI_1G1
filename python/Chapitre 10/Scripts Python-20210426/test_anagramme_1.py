from anagramme_2 import anagramme

import unittest

class test_anagramme(unittest.TestCase):

    def test_ok(self):
        self.assertTrue(anagramme('aasdfr','farsda'))    # Attendu :   True

    def test_not_ok_1(self):
        self.assertFalse( anagramme('aasdfr','ffarsda')) # Attendu : False

    def test_not_ok2(self):
        self.assertFalse( anagramme('hjgulj','lujhgh')) # Attendu : False

   
if __name__ == '__main__':
    unittest.main()
    