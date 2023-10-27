# Classe Question pour représenter une question à choix multiple
class Question:
    def __init__(self, question, reponses, reponse_correcte):
        # Initialise une instance de Question avec une question, des réponses et la réponse correcte.
        self.question = question  # Stocke la question
        self.reponses = reponses  # Stocke les options de réponse
        self.reponse_correcte = reponse_correcte  # Stocke la réponse correcte

    def est_correcte(self, reponse_prof):
        # Méthode pour vérifier si la réponse donnée par l'utilisateur est correcte
        # reponse_prof : La réponse fournie par l'utilisateur

        # Compare la réponse de l'utilisateur (en minuscules) avec la réponse correcte (en minuscules)
        return reponse_prof.lower() == self.reponse_correcte.lower()
