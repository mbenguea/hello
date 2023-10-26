# passphrase_generator.py

import random

class PassphraseGenerator:
    def __init__(self, word_list):
        self.word_list = word_list

    def generate_passphrase(self, dice_rolls):
        passphrase = []

        for roll in dice_rolls:
            dice_values = [int(char) for char in roll]
            word_index = sum([(dice_values[i] - 1) * (6 ** (4 - i)) for i in range(5)])
            passphrase.append(self.word_list[word_index])

        return ' '.join(passphrase)

# Example usage:
# word_list = ["mot1", "mot2", ...]  # Remplacez par la liste complète de mots
# generator = PassphraseGenerator(word_list)
# passphrase = generator.generate_passphrase(["12345", "54321", ...])  # Remplacez par les lancers de dés
# print(f"Passphrase générée : {passphrase}")
