from quiz import QCM
from questionAida import Question


if __name__ == "__main__":
    questions = [
        Question("Quelle est la capitale de la France ?", [ "Paris",  "Londres", "Rome"], "Paris"),
        Question("Quel est le plus grand océan de la Terre ?", ["Océan Pacifique", "Océan Atlantique", "Océan Indien"], "Océan Pacifique"),
        Question("Qui a peint la Joconde ?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"], "Leonardo da Vinci"),
        Question("Quelle est la plus grande planète du système solaire ?", ["Jupiter", "Saturne", "Mars"], "Jupiter"),
        Question("Quel est le plus long fleuve du monde ?", ["Le Nil", "L'Amazone", "Le Mississippi"], "L'Amazone"),
        Question("Qui a découvert la gravité en observant une pomme tomber ?", ["Isaac Newton", "Albert Einstein", "Galilée"], "Isaac Newton"),
        Question("Quel pays est célèbre pour sa Grande Muraille ?", ["Chine", "Russie", "Inde"], "Chine"),
        Question("Quel est l'animal national de l'Australie ?", ["Kangourou", "Koala", "Dingo"], "Kangourou"),
        Question("Quelle planète est surnommée la 'Planète Rouge' ?", ["Mars", "Vénus", "Jupiter"], "Mars"),
        Question("Qui a écrit 'Romeo et Juliette' ?", ["William Shakespeare", "Charles Dickens", "Jane Austen"], "William Shakespeare")
    ]

    qcm = QCM(questions)
    qcm.executer_qcm()

