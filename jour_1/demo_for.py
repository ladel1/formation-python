#          0,1,2........................,12
nombres = [5,9,5,2,34,5,4,987,3,43,4,64,654]

# d'afficher uniquement les nombres pair
for nombre in nombres:
    if(nombre % 2 == 0):
        print(nombre)

print("****************")

for index in range(0,len(nombres)):
    print(nombres[index])
