import string

class Cryptage: 
    def __init__(self, nom):
        self.nom = nom

    def crypt(self, message):
        caracteres = string.ascii_letters + string.digits + string.punctuation + " "
        message_crypte = ""
        
        for char in message:
            if char in caracteres:
                index = caracteres.index(char)
                message_crypte += caracteres[(index + 1) % len(caracteres)]  
            else:
                message_crypte += char  
        
        return message_crypte