from forme import Forme

class Rectangle(Forme): #implémentaion de l'interface Forme
    def __init__(self, longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur
    
r = Rectangle(5,6)
print(r.aire())
