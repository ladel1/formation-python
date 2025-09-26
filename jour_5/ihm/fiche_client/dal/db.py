"""
DAL: Data Access Layer
Gérer la BDD (CRUD: Create, Read, Update, Delete)
récupérer la connexion
"""
import sqlite3

DB_NAME = "fiche_client.db"

def get_connection():
    return sqlite3.connect(DB_NAME)
    

def init_db():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS clients(
                            id INTEGER PRIMARY KEY,
                            nom TEXT NOT NULL,
                            prenom TEXT NOT NULL,
                            adresse TEXT,
                            tel TEXT                    
                       )
                       """)
        connection.commit()
    except:
        print("aaaa")
        connection.close()