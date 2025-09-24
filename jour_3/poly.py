from bateau import Bateau
from moto import Moto

vehicules = [
    Bateau("Boston-whaler","100","France"),
    Moto("Yamaha","652","0km"),
    Bateau("Jeanneau","250","Italie"),
    Moto("Honda","X200","5000km"),
    Bateau("Bayliner","30","USA"),
    Moto("Kawasaki","30","1500km")
]

for vehicule in vehicules:
    vehicule.afficher() # polymorphisme
    print(type(vehicule))