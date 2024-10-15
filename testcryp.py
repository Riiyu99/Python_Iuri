import string

class Cryptage: 
    def __init__(self, nom):
        self.nom = nom

    def crypt(self, message):
        
        caracteres = string.ascii_letters + string.digits + string.punctuation
        message_crypte = ""
        
        for char in message:
            print(f"Caractère en cours de traitement : {char}")
            if char == " ":
                message_crypte += "!"
            elif char in caracteres:
                index = caracteres.index(char)
                next_char = caracteres[(index + 1) % len(caracteres)]
                print(f"Index actuel : {index}, Caractère suivant : {next_char}")
                message_crypte += next_char
            else:
                # Si le caractère ne fait pas partie de notre table, on le garde inchangé
                message_crypte += char
            print(f"Message crypté jusqu'à présent : {message_crypte}")
        
        print(f"Message final crypté : {message_crypte}")
        return message_crypte  # Renvoie la chaîne cryptée