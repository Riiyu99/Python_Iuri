import string

class Cryptage: 
    def __init__(self, nom):
        self.nom = nom

    def crypt(self, message):
        caracteres = string.ascii_letters + string.digits + string.punctuation + " "
        message_crypte = ""
        
        