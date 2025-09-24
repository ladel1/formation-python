from forme import Forme
import math

class Cercle(Forme): # implementation de "l'interface" Forme
    
    def __init__(self,r):
        self.r = r

    def aire(self):
        return math.pi * self.r**2
    

c = Cercle(12)
print(c.aire())