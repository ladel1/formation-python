"""
Correction TP 1 gestion d'une mini bilio
"""

# partie 1 - structure de donées dictionnaire
bibliotheque = {
    "livres": []
}

# partie 2 - Ajout de fonctions
def ajouter_livre(bibliotheque: dict, titre: str, auteur: str, annee: int) -> None:
    livre = {
        "titre": titre.strip(),
        "auteur": auteur.strip(),
        "annee": annee,
        "disponible": True
    }
    bibliotheque["livres"].append(livre)

def afficher_livres(bibliotheque):
    if not bibliotheque["livres"]:
        print("Aucun livre dans la bibliotheque!")
        return
    # TODO: formatage de livre
    for livre in bibliotheque["livres"]:
        print(livre)
    
def chercher_livre(bibliotheque, mot_clef):
    for livre in bibliotheque["livres"]:
        if mot_clef.lower() in livre["titre"].lower():
            return livre

def emprunter_livre(bibliotheque, titre):
    for livre in bibliotheque["livres"]:
        if livre["titre"].lower() == titre and livre["disponible"] == True:
            livre["disponible"] = False
            print("Livre emprunté avec succès")
            return
    print("Livre introuvable.")

def rendre_livre(bibliotheque, titre):
    for livre in bibliotheque["livres"]:
        if livre["titre"].lower() == titre and livre["disponible"] == False:
            livre["disponible"] = True
            print("Livre redu avec succès")
            return
    print("Livre introuvable")

# Partie 3 - Sauvegarde et chargement dans un fichier
def sauvegarder(bibliotheque, fichier):
    with open(fichier,"w", encoding="utf-8") as file:
        for livre in bibliotheque["livres"]:
            line = f"{livre["titre"]} - {livre["auteur"]} ({livre["annee"]}) - {"Disponible" if livre["disponible"] == True else "Emprunté"}\n"
            file.write(line)


def charger(fichier):
    bib = {}
    with open(fichier, "r", encoding="utf-8") as file:
        for line in file:
            titre, auteur_date, disponible = line.strip().split("-")
            auteur, _date = auteur_date.split("(")
            date = _date.strip()
            is_disponible = disponible.strip().lower() == "disponible"
            bib["livres"].append({
                "titre":titre.strip(),
                "auteur": auteur.strip(),
                "date":date[:len(date)-1], # slicing pour enlever le parenthese fermant
                "disponible": is_disponible
            })


# Partie 5 - Générateurs
def livres_disponibles(bibliotheque):
    for livre in bibliotheque["livres"]:
        if livre["disponible"] == True:
            yield livre

# Partie 4 - Boucles et interaction utilisateur
while True:
    print("1) Afficher les livres")
    print("2) Ajouter un livre")
    print("3) Chercher un livre")
    print("4) Emprunter un livre")
    print("5) Rendre un livre")
    print("6) Sauvegarder et quitter")
    print("7) afficher les livres disponbile")


    choix = input("Votre choix:\n")

    if choix == "1":
        afficher_livres(bibliotheque)
    elif choix == "2":
        titre = input("Entrez un titre:\n")
        auteur = input("Entrez un auteur:\n")
        annee = input("Entrez une année:\n")
        ajouter_livre(bibliotheque,titre,auteur,int(annee))
    elif choix == "3":
        mot_clef = input("Entrez le mot clef:\n")
        chercher_livre(bibliotheque,mot_clef)
    elif choix == "4":
        titre = input("Entrez un titre de livre à emprunter:\n")
        emprunter_livre(bibliotheque,titre)
    elif choix == "5":
        titre = input("Entrez un titre de livre à rendre:\n")
        rendre_livre(bibliotheque,titre)
    elif choix == "6":
        fichier = "bibliotheque.txt"
        sauvegarder(bibliotheque,fichier)
        break
    elif choix == "7":
        livres_disponibles = livres_disponibles(bibliotheque)
        for livre in livres_disponibles:
            print(livre)
    else:
        print("Choix invalide!")
 
