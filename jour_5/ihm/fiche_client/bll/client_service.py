"""
BLL = la logique métier, les regles, la validation
"""
from dal.client_repository import ClientRepository
from bo.client import Client
class ClientService:

    def __init__(self):
        self.client_repository = ClientRepository() 

    def creer_client(self, prenom: str, nom: str, tel: str, adresse: str):
        # 1) étape de validation de données !!!
        
        # 2) creation de client
        client = Client(None,prenom,nom,adresse,tel)
        # 3) sauvgarder le client
        self.client_repository.create(client)
