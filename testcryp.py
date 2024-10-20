import string

class Cryptage:
    def __init__(self, nom):
        self.nom = nom

    
    def crypt(self, message, pas):
        print(f"message: {message}, pas: {pas}")
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


    def decrypt(self, message):
        # Récupère le pas à partir de la fin du message
        pas = int(message[-1])  # Récupère le dernier caractère comme pas
        message = message[:-1]  # Enlève le pas du message

        caracteres = string.ascii_letters + string.digits + string.punctuation
        message_decrypte = ""

        for char in message:
            if char == "!":
                message_decrypte += " "  # Remplace ! par espace
            elif char in caracteres:
                index = caracteres.index(char)
                # Décalage inverse du caractère
                prev_char = caracteres[(index - pas) % len(caracteres)]
                message_decrypte += prev_char
            else:
                message_decrypte += char  # Caractères non définis restent inchangés

        return message_decrypte  # Renvoie le message déchiffré