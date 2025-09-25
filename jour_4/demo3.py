import os
from pathlib import Path
import sys

print("Répertoire courant: ", os.getcwd())
print("Liste fichiers: ", os.listdir())
print("Nom de l'utilisateur: ",os.getlogin())
print("Nombre CPU: ",os.cpu_count())

for dir in os.listdir():
    print("Dir: ",dir)

dossier = Path(".")
for f in dossier.iterdir():
    if f.is_file():
        print(f"Name: {f.name}, fichier: {f.is_file()}")

print(f"System: {sys.version}")