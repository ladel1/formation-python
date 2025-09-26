"""
DAL
client repository => CRUD
"""
from bo.client import Client
from .db import get_connection, init_db

class ClientRepository:

    def __init__(self):
        init_db ()

    def create(self, client: Client) -> int:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
                       INSERT INTO clients (nom, prenom, tel, adresse) VALUES (?, ?, ?, ?)
                       """, (client.nom, client.prenom, client.tel, client.adresse))        
        connection.commit()
        return cursor.lastrowid