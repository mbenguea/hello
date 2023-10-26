# password_strength.py
import math
import re

class PasswordStrengthTester:
    def __init__(self, password):
        self.password = password

    def calculate_entropy(self):
        # Calcul de l'entropie en utilisant les critères de l'ANSSI
        length = len(self.password)
        lowercase_chars = bool(re.search(r'[a-z]', self.password))
        uppercase_chars = bool(re.search(r'[A-Z]', self.password))
        digit_chars = bool(re.search(r'\d', self.password))
        special_chars = bool(re.search(r'[^a-zA-Z\d]', self.password))

        # Définir les valeurs pour chaque critère
        length_value = length
        lowercase_value = 26 if lowercase_chars else 0
        uppercase_value = 26 if uppercase_chars else 0
        digit_value = 10 if digit_chars else 0
        special_value = 32 if special_chars else 0

        # Calcul de l'entropie
        entropy = length_value * (lowercase_value + uppercase_value + digit_value + special_value)

        return entropy

    def password_strength(self):
        entropy = self.calculate_entropy()
        
        if entropy < 28:
            return "Très faible"
        elif entropy < 36:
            return "Faible"
        elif entropy < 60:
            return "Moyenne"
        else:
            return "Forte"

# Example usage:
# tester = PasswordStrengthTester("MotDePasse123!")
# strength = tester.password_strength()
# print(f"Force du mot de passe : {strength}")
