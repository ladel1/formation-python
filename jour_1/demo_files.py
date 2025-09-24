with open("notes.txt","w", encoding="UTF-8") as file:
    enter = input("Entrez une phrase\n")
    file.write(enter)

with open("notes.txt","r",encoding="UTF-8") as file:
    text = file.read()
    print(text)