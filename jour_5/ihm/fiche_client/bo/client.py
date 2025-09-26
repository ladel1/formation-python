"""
BO = les classes métier
Client 
"""
from dataclasses import dataclass

@dataclass
class Client:
    id: int | None
    prenom: str
    nom: str
    adresse: str
    tel: str
