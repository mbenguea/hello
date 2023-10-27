# passphrase_generator.py

class PassphraseGenerator:
    def __init__(self, word_list):
        self.word_list = word_list

    def generate_passphrase(self, dice_rolls):
        passphrase = []

        for roll in dice_rolls:
            # Convertir le lancer en un entier et soustraire 1 pour tenir compte de l'indexation à partir de zéro
            word_index = int(roll) - 1

            # Vérifier si l'indice est valide
            if 0 <= word_index < len(self.word_list):
                passphrase.append(self.word_list[word_index])
            else:
                return "Lancer de dés non valide : le nombre est en dehors de la plage."

        return ' '.join(passphrase)

def load_eff_wordlist(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

if __name__ == "__main__":
    eff_word_list = load_eff_wordlist("eff_wordlist.txt")
    generator = PassphraseGenerator(eff_word_list)
    dice_rolls = input("Entrez les lancers de dés (séparés par des espaces) : ").split()
    passphrase = generator.generate_passphrase(dice_rolls)
    print("Passphrase générée :", passphrase)
