from livre import Livre
from bibliotheque import Bibliotheque
from livre_indisponible import LivreIndisponible


# main

b = Bibliotheque()
l1 = Livre("The wolf of wall street", "Jordan Belfort","2012")
l2 = Livre("Dune", "Franck Herbert","1965")
l3 = Livre("L'Étranger", "Albert Camus", 1942)
l4 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
# on ajoute les livres dans la biblio
b.ajouter_livre(l1)
b.ajouter_livre(l2)
b.ajouter_livre(l3)
b.ajouter_livre(l4)
print("Catalogue")
for livre in b:
    print(livre)
print("Recherche")
for livre in b.chercher("wolf"):
    print(livre)
