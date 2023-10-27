import random
from questionAida import Question

# Classe QCM pour gérer le quiz
class QCM:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.reponses_correctes = {}  # Dictionnaire pour stocker les réponses correctes

    def afficher_question(self, question):
        print(question.question)

        lettres = ["a)", "b)", "c)"]

        # Mélange aléatoirement les réponses tout en maintenant l'ordre "a), b), c)"
        reponses_personnalisees = random.sample(question.reponses, len(question.reponses))

        for lettre, reponse in zip(lettres, reponses_personnalisees):
            print(f"{lettre} {reponse}")


    def afficher_score(self):
        print(f"Votre score final est de {self.score}/{len(self.questions)}.")
        self.afficher_corrigé()

    def poser_questions(self):
        random.shuffle(self.questions)
        for question in self.questions:
            self.afficher_question(question)
            while True:
                reponse_utilisateur = input("Votre réponse : ")
                if reponse_utilisateur.lower() == 'a' or reponse_utilisateur.lower() == 'b' or reponse_utilisateur.lower() == 'c':
                    break
                else:
                    print("Veuillez répondre uniquement par 'a,' 'b,' ou 'c.'")
            if question.est_correcte(reponse_utilisateur):
                self.score += 1
            self.reponses_correctes[question] = question.reponse_correcte


    def afficher_corrigé(self):
        print("Corrigé :")
        for question, reponse_correcte in self.reponses_correctes.items():
            print(f"{question.question} - Réponse correcte : {reponse_correcte}")

    def executer_qcm(self):
        print("Bonjour,Bienvenue au QCM de Aida MBENGUE!")
        self.poser_questions()
        self.afficher_score()

