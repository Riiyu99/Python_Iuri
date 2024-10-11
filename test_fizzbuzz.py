import unittest
from test import FizzBuzzs


class testFizz(unittest.TestCase):

    def setUp(self):
        print("------------Nouveau Test-------------------")
        self.monInstance = FizzBuzzs("MonInstance")
    
    def test_mon_premier_test(self):
        self.assertEqual(self.monInstance.affiche(), "klhbflihblh")

    def tearDown(self):
        print("-----------------Fin du Test--------------")


if __name__ == "__main__":
    unittest.main()