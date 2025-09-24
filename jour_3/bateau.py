from vehicule import Vehicule

class Bateau(Vehicule):

    def __init__(self, marque, modele, drapeau):
        super().__init__(marque,modele)
        self.drapeau = drapeau

    def afficher(self):
        super().afficher()
        print(f"Drapeau {self.drapeau}")
    
    def __traitement_interne(self):# private 
        """
        bien 
        """
        pass

    def __str__(self):
        return f"{super().__str__()} Drapeau: {self.drapeau}"

b = Bateau("Dufour Yachts","100","France")
b.afficher()

print(isinstance(b,Bateau))