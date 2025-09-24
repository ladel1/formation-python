solde = 0

def crediter(montant): # not pure
    global solde
    solde = solde + montant

def debiter(montant): # not pure
    global solde
    if(solde - montant < 0):
        print("Le solde est insuffisant\n")
        return
    solde = solde - montant

while True:
    
    operation = input("Choisir l'operation:\n1) pour créditer\n2) pour débiter\n3) pour quitter\n")
    
    if operation == "3":
        break

    montant = input("Entrez un montant:\n")

    if operation == "1":
        crediter(float(montant))
    else:
        debiter(float(montant))

    print(f"Votre solde est: {solde}")

    if solde > 1000000 and solde < 1000000000:
        print("Vous etes multimillionaire")
