import sqlite3

connexion = sqlite3.connect("demo4.db")

c = connexion.cursor()

c.execute("CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, nom TEXT)")

c.execute("INSERT INTO articles(nom) VALUES(?)",("Iphone",))
connexion.commit()

c.execute("SELECT * FROM articles")
print(c.fetchall())

connexion.close()

