import unittest
from  testcryp import Cryptage 

class TestCryptage(unittest.TestCase):
    
    def setUp(self):
        print("------------Nouveau Test-------------------")
        self.monInstance = Cryptage("MonInstance")
    
    def test_cryptage_simple(self):
        self.assertEqual(self.monInstance.crypt("abc"), "bcd")
        self.assertEqual(self.monInstance.crypt("ABC"), "BCD")
        self.assertEqual(self.monInstance.crypt("123"), "234")
        self.assertEqual(self.monInstance.crypt("! "), '"!')
    
    def tearDown(self):
        print("-----------------Fin du Test--------------")


if __name__ == '__main__':
    unittest.main()
