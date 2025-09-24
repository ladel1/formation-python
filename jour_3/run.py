from file import File

with File("test.txt") as f:
    f.ouvrir("w")
    f.ecrire("aaaaaa")
    
# f = File("test.txt")
# f.ouvrir("w")
# f.ecrire("blabalbabla")