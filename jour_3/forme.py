"""
Déclaration d'une interface Forme
"""
from abc import abstractmethod, ABC

# interface
class Forme(ABC):
    @abstractmethod
    def aire(self): pass 