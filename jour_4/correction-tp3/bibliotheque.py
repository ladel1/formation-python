from livre import Livre

class Bibliotheque:

    def __init__(self):
        self._catalogue: list[Livre] = []

    def chercher(self, mot_clef: str) -> list[Livre] :
        livres = []
        for livre in self._catalogue:
            if mot_clef.lower() in livre.titre.lower():
                livres.append(livre)
        return livres
        
    def ajouter_livre(self,livre: Livre) -> None:
        self._catalogue.append(livre)        

    def emprunter(self, titre: str) -> bool:
        for livre in self._catalogue:
            if livre.titre.lower() == titre and livre.disponible == True:
                livre.disponible = False                
                return True
        return False

    def rendre(self, titre: str) -> bool:
        for livre in self._catalogue:
            if livre.titre.lower() == titre and livre.disponible == False:
                livre.disponible = True
                return True
        return False  

    def __len__(self) -> int:
        return len(self._catalogue)  
    
    def __iter__(self):
        for livre in self._catalogue:
            yield livre