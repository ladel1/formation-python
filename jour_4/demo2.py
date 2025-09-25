import re

texte = "balbaba mon email: adel@gmail.com dskjhsdlkjfhsdq adel.latibi@outlook.fr"

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-z]{2,}"
email = "adel@gmail.com"
resultat = re.findall(pattern,texte)
print(resultat)
print(re.match(pattern,email))