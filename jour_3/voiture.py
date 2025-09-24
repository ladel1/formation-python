class Voiture:   
    # constructeur 
    def __init__(self, marque, modele):
        # attributs privés
        self.__marque = marque
        self.__modele = modele

    # méthode classique
    def afficher(self):
        print(f"Marque: {self.__marque} Modele: {self.__modele}")

    # getters et setters
    @property
    def marque(self): # getter de la marque
        return self.__marque
    
    @marque.setter
    def marque(self,marque): #setter de la marque
        self.__marque = marque

    @property
    def modele(self): # getter de modele
        return self.__modele
    
    @modele.setter
    def modele(self,modele): #setter du modele
        self.__modele = modele    

# creation instance
v = Voiture("Bugatti","Chiron")
# appeler la méthode afficher
v.afficher()
# appeler le getter ou property marque
print(f"Marque: {v.marque} ")

