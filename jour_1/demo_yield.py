def read_large_file(file:str):
    """
        Générateur pour lire un gros fichier
    """
    with open(file,"r",encoding="UTF-8") as file:
        for line in file:
            yield line.strip()


for line in read_large_file("notes.txt"):
    print(line)