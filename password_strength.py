# password_strength.py
import math
import re

class PasswordStrengthTester:
    def __init__(self, password):
        self.password = password

    def password_strength(self, min_length=8, require_lowercase=True, require_uppercase=True, require_digits=True, require_special=False):
        while not self.password:
            print("Le mot de passe ne peut pas être vide. Veuillez réessayer.")
            self.password = input("Entrez un mot de passe : ")

        # Calculez la longueur du mot de passe
        length = len(self.password)

        # Vérifiez si le mot de passe contient des minuscules
        has_lowercase = any(char.islower() for char in self.password)

        # Vérifiez si le mot de passe contient des majuscules
        has_uppercase = any(char.isupper() for char in self.password)

        # Vérifiez si le mot de passe contient des chiffres
        has_digits = any(char.isdigit() for char in self.password)

        # Vérifiez si le mot de passe contient des caractères spéciaux
        has_special = bool(re.search(r'[!@#$%^&*()-_=+[\]{}|;:\'"<>,.?/]', self.password))

        # Calculez l'entropie du mot de passe
        entropy = calculate_entropy(self.password)

        # Appliquez les critères de l'ANSSI pour évaluer la force
        if length >= 12 and has_lowercase and has_uppercase and has_digits and has_special and entropy >= 70:
            strength = "Mot de passe fort"
        elif length >= 8 and has_lowercase and has_uppercase and (has_digits or has_special) and entropy >= 50:
            strength = "Mot de passe moyen"
        else:
            strength = "Mot de passe faible"

        return strength, entropy
def calculate_entropy(password):

    # Calcul de la longueur du mot de passe
    length = len(password)

    # Compteur de caractères différents
    unique_chars = len(set(password))

    # Si le mot de passe contient uniquement des lettres (minuscules et majuscules) et des chiffres, l'entropie est réduite
    is_alphanumeric = password.isalnum()

    # Appliquez un facteur de complexité en fonction du type de caractères
    if is_alphanumeric:
        complexity_factor = 1.0
    else:
        complexity_factor = 1.5  # Un mot de passe contenant des caractères spéciaux est plus complexe

    # Calcul de l'entropie
    entropy = length * math.log(unique_chars, 2) * complexity_factor

    return int(entropy)  # Arrondi à l'entier le plus proche

