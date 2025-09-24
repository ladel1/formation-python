# déclaration d'une classe
class Personne:
    # constructeur
    def __init__(self,prenom,nom):
        # attributs
        self.prenom = prenom
        self.nom = nom
    # méthode
    def afficher(self):
        print(f"Prénom: {self.prenom}, Nom: {self.nom}")