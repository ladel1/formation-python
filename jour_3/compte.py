class SoldeInsuffisant(Exception): pass


class Compte:
    
    def __init__(self, solde = 0):
        self.solde = solde

    def debiter(self,montat):
        if self.solde - montat < 0:
            raise SoldeInsuffisant("Vous n'avez pas assez d'argent!") # arrete la fonction (sortir de la fonction avec une erreur)
        self.solde = self.solde - montat

c = Compte(10)
try:
    c.debiter(100)
except SoldeInsuffisant:
    print("lablablabbla")
print("Fin ")