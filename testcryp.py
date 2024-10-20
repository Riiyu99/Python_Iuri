import string

class Cryptage:
    def __init__(self, nom):
        self.nom = nom

    
    def crypt(self, message, pas):
        
        if not (1 <= pas <= 9):
            raise ValueError("Le pas doit être un entier entre 1 et 9.")
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        message_crypte = ""

        for char in message:
            if char == " ":
                message_crypte += "!"
            elif char in caracteres:
                index = caracteres.index(char)
                next_char = caracteres[(index + pas) % len(caracteres)]
                message_crypte += next_char
            else:
                message_crypte += char
        
        return message_crypte + str(pas)
