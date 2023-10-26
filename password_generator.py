# password_generator.py
import random
import string

class PasswordGenerator:
    def __init__(self, num_lowercase, num_uppercase, num_digits, num_special):
        self.num_lowercase = num_lowercase
        self.num_uppercase = num_uppercase
        self.num_digits = num_digits
        self.num_special = num_special

    def generate_password(self):
        # Créez des groupes de caractères en fonction des critères
        lowercase_chars = ''.join(random.choice(string.ascii_lowercase) for _ in range(self.num_lowercase))
        uppercase_chars = ''.join(random.choice(string.ascii_uppercase) for _ in range(self.num_uppercase))
        digit_chars = ''.join(random.choice(string.digits) for _ in range(self.num_digits))
        special_chars = ''.join(random.choice(string.punctuation) for _ in range(self.num_special))
        
        # Concaténez les groupes de caractères et mélangez-les
        all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars
        password_list = list(all_chars)
        random.shuffle(password_list)
        password = ''.join(password_list)
        
        return password

# Example usage:
# generator = PasswordGenerator(4, 4, 2, 2)
# password = generator.generate_password()
# print(f"Mot de passe généré : {password}")
