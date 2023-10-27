# Générateur et Testeur de Mot de Passe

Ce projet est un programme Python qui vous permet de générer des mots de passe aléatoires et de tester la force de mots de passe existants en fonction de critères spécifiques.

## Fonctionnalités

Le programme comprend les fonctionnalités suivantes :

1. **Testeur de Mot de Passe** : Évalue la force d'un mot de passe existant en fonction de critères tels que la longueur, la présence de minuscules, de majuscules, de chiffres et de caractères spéciaux, et calcule également l'entropie du mot de passe.

2. **Générateur de Mot de Passe Aléatoire** : Génère un mot de passe aléatoire en fonction des critères que vous spécifiez, notamment le nombre de minuscules, de majuscules, de chiffres et de caractères spéciaux.

3. **Générateur de Passphrase** : Génère une passphrase en utilisant la méthode de dés de l'EFF. Vous pouvez spécifier les mots à utiliser pour générer des passphrases.

## Exigences

Le programme a été développé en Python. Assurez-vous d'avoir Python installé sur votre système.

## Utilisation

1. Clonez ce dépôt sur votre ordinateur.

2. Exécutez le programme en utilisant `python main1.py`.

3. Choisissez l'outil de sécurité que vous souhaitez utiliser en saisissant le numéro correspondant.

4. Suivez les instructions pour tester un mot de passe, générer un mot de passe aléatoire ou générer une passphrase.

## Exemple de Test Unitaire

Le fichier `test_password_strength.py` contient un exemple de test unitaire pour la classe `PasswordStrengthTester`. Vous pouvez l'exécuter pour vérifier que le testeur de mot de passe fonctionne correctement.

import unittest
from password_strength import PasswordStrengthTester

class TestPasswordStrength(unittest.TestCase):
    def test_password_strength(self):
        # Test de mot de passe fort
        tester = PasswordStrengthTester("MotDePasse123!@")
        strength, entropy = tester.password_strength()
        self.assertEqual(strength, "Mot de passe fort")
        
        # Test de mot de passe moyen
        tester = PasswordStrengthTester("MotDePasse123")
        strength, entropy = tester.password_strength()
        self.assertEqual(strength, "Mot de passe moyen")
        
        # Test de mot de passe faible
        tester = PasswordStrengthTester("12345")
        strength, entropy = tester.password_strength()
        self.assertEqual(strength, "Mot de passe faible")

if __name__ == '__main__':
    unittest.main()
