import unittest
from testcryp import Cryptage 

class TestCryptage(unittest.TestCase):
    
    def setUp(self):
        print("------------Nouveau Test-------------------")
        self.monInstance = Cryptage("MonInstance")
    
    def test_cryptage_simple(self):
        self.assertEqual(self.monInstance.crypt("abc", 1), "bcd1")
        self.assertEqual(self.monInstance.crypt("ABC", 1), "BCD1")
        self.assertEqual(self.monInstance.crypt("123", 1), "2341")
        self.assertEqual(self.monInstance.crypt("! ", 1), '"!1')

    def test_cryptage_espace(self):
        self.assertEqual(self.monInstance.crypt("hello world", 1), "ifmmp!xpsme1")

    def test_cryptage_avec_pas(self):
        self.assertEqual(self.monInstance.crypt("hello world", 2), "jgnnq!yqtnf2")

    def test_pas_invalide(self):
        with self.assertRaises(ValueError):
            self.monInstance.crypt("test", 10)
            
    def test_decryptage_simple(self):
        self.assertEqual(self.monInstance.decrypt("bcd1"), "abc")
        self.assertEqual(self.monInstance.decrypt("BCD1"), "ABC")
        self.assertEqual(self.monInstance.decrypt("2341"), "123")
        self.assertEqual(self.monInstance.decrypt('"!1'), "! ")

   

    def tearDown(self):
        print("-----------------Fin du Test--------------")

if __name__ == '__main__':
    unittest.main()
