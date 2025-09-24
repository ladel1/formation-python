class Vehicule:

    def __init__(self,marque,modele):
        self.marque = marque
        self.modele = modele

    def _traitement_pour_classes_filles(self):# protected
        pass        
        
    def afficher(self):
        print(f"Marque: {self.marque}, Modele: {self.modele}")

    def __str__(self):
        return f"Marque: {self.marque}, Modele: {self.modele}"