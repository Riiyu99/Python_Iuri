import string

class Cryptage: 
    def __init__(self, nom):
        self.nom = nom

    def crypt(self, message):
        caracteres = string.ascii_letters + string.digits + string.punctuation + " "
        message_crypte = ""
          
        for char in message:
            print(f"Caractère en cours de traitement : {char}")  # Ajout pour voir les caractères traités
            if char in caracteres:
                index = caracteres.index(char)
                # Ajout pour voir les indices et le caractère suivant
                print(f"Index actuel : {index}, Caractère suivant : {caracteres[(index + 1) % len(caracteres)]}")  
                # Ajoute le caractère suivant dans la chaîne
                message_crypte += caracteres[(index + 1) % len(caracteres)]
            else:
                # Si le caractère ne fait pas partie de notre table, on le garde inchangé
                message_crypte += char
            print(f"Message crypté jusqu'à présent : {message_crypte}")  # Ajout pour suivre la concaténation
        
        print(f"Message final crypté : {message_crypte}")  
        return message_crypte  
