import random
import string

class PasswordGenerator:
    def __init__(self, num_lowercase, num_uppercase, num_digits, num_special):
        self.num_lowercase = num_lowercase
        self.num_uppercase = num_uppercase
        self.num_digits = num_digits
        self.num_special = num_special

    def generate_password(self):
        # Vérifiez si les critères spécifiés sont valides
        total_length = self.num_lowercase + self.num_uppercase + self.num_digits + self.num_special
        if total_length < 8:
            return "Les critères spécifiés sont insuffisants. Le mot de passe doit avoir au moins 8 caractères."

        # Générez des caractères aléatoires pour chaque catégorie
        lowercase_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(self.num_lowercase))
        uppercase_chars = ''.join(random.choice(string.ascii_uppercase) for _ in range(self.num_uppercase))
        digit_chars = ''.join(random.choice(string.digits) for _ in range(self.num_digits))
        special_chars = ''.join(random.choice("!@#$%^&*()-_=+[]{}|;:'\"<>,.?/") for _ in range(self.num_special))

        # Combinez les caractères de toutes les catégories
        password = lowercase_chars + uppercase_chars + digit_chars + special_chars

        # Mélangez les caractères pour obtenir un mot de passe aléatoire
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        return password
