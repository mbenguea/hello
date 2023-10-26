from password_strength import PasswordStrengthTester
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator

if __name__ == "__main__":
    while True:
        print("Choisissez un outil de sécurité :")
        print("1. Testeur de mot de passe")
        print("2. Générateur de mot de passe aléatoire")
        print("3. Générateur de passphrase (méthode de dés de l'EFF)")
        print("4. Quitter")

        choix = input("Entrez le numéro de l'outil ou '4' pour quitter : ")

        if choix == "1":
            password = input("Entrez un mot de passe : ")
            tester = PasswordStrengthTester(password)
            strength = tester.password_strength()
            print(f"Force du mot de passe : {strength}")
        elif choix == "2":
            num_lowercase = int(input("Nombre de minuscules : "))
            num_uppercase = int(input("Nombre de majuscules : "))
            num_digits = int(input("Nombre de chiffres : "))
            num_special = int(input("Nombre de caractères spéciaux : "))
            generator = PasswordGenerator(num_lowercase, num_uppercase, num_digits, num_special)
            password = generator.generate_password()
            print(f"Mot de passe généré : {password}")
        elif choix == "3":
            # Remplacez word_list par la liste complète de mots pour les passphrases
            word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "iceberg", "jackfruit", "kiwi", "lemon"]
            generator = PassphraseGenerator(word_list)
            dice_rolls = input("Entrez les lancers de dés (ex: 12345 54321) : ").split()
            passphrase = generator.generate_passphrase(dice_rolls)
            print(f"Passphrase générée : {passphrase}")
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir une option valide.")
