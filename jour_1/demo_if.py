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

operation = input("Choisir l'operation (1: pour créditer et 2: pour débiter)\n")
montant = input("Entrez un montant:\n")

if operation == "1":
    crediter(float(montant))
else:
    debiter(float(montant))

print(f"Votre solde est: {solde}")

if solde > 1000000 and solde < 1000000000:
    print("Vous etes multimillionaire")
