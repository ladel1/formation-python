from vehicule import Vehicule
from moteur import Moteur
from dataclasses import dataclass

@dataclass
class Conducteur:
    nom: str
    prenom: str
    num_permis: str
    
class Moto(Vehicule):

    def __init__(self,marque,modele,km,conducteur):        
        super().__init__(marque,modele) # 'super()' toujours en premier
        self.km = km
        self.moteur = Moteur() #association forte: composition
        self.conducteur = conducteur  #association faible: agregation

    def afficher(self): # redéfinition 
        super().afficher() # 'super()' pour appeler méthode parent
        print(f"Km: {self.km}")

# c = Conducteur()
m = Moto("Yamaha","500","10000km",c)
m.afficher()