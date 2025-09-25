from livre_indisponible import LivreIndisponible

class Livre:
    """
        La classe Livre représente livre empruntable de la bibilio
    """
    def __init__(self,titre: str,auteur: str,annee: int,disponible: bool = True):
        self._titre = titre
        self._auteur = auteur
        self._annee = annee
        self._disponible = disponible
    
    @property
    def titre(self):
        return self._titre
    
    @property
    def auteur(self):
        return self._auteur
    
    @property
    def annee(self):
        return self._annee
    
    @property
    def disponible(self):
        return self._disponible
    
    def emprunter(self):
        if not self._disponible:
            raise LivreIndisponible(self._titre)            
        self._disponible = False

    def rendre(self):
        self._disponible = True
    
    def __str__(self):
        return f"Titre: {self._titre}, Auteur: {self._auteur}, Année: {self._annee}, Disponible: {self._disponible}"