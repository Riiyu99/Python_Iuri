import unittest
from testcryp import Cryptage 

class TestCryptage(unittest.TestCase):

    def setUp(self):
        self.monInstance = Cryptage("Mon instance")  

    def test_cryptage_simple(self):
        message_crypte = self.monInstance.crypt("abc", 1)
        print(f"{message_crypte} = abc")
        self.assertEqual(message_crypte, "bcd1")

    def test_cryptage_espace(self):
        message_crypte = self.monInstance.crypt("hello world", 1)
        print(f"{message_crypte} = hello world")
        self.assertEqual(message_crypte, "ifmmp!xpsme1")

    def test_cryptage_avec_pas(self):
        message_crypte = self.monInstance.crypt("hello world", 2)
        print(f"{message_crypte} = hello world")
        self.assertEqual(message_crypte, "jgnnq!yqtnf2")

    def test_pas_invalide(self):
        with self.assertRaises(ValueError):
            self.monInstance.crypt("test", 10) 

    def test_decryptage(self):
        decrypted_message = self.monInstance.decrypt("bcd1")
        print(f"{decrypted_message} = bcd1")
        self.assertEqual(decrypted_message, "abc") 
        
        decrypted_message = self.monInstance.decrypt("ifmmp!xpsme1")
        print(f"{decrypted_message} = ifmmp!xpsme1")
        self.assertEqual(decrypted_message, "hello world")  
        
        decrypted_message = self.monInstance.decrypt("jgnnq!yqtnf2")
        print(f"{decrypted_message} = jgnnq!yqtnf2")
        self.assertEqual(decrypted_message, "hello world")  

if __name__ == '__main__':
    unittest.main()
