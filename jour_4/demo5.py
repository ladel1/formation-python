import sqlite3

# à voir: Archtectures: Dev en couches (IHM,BO,BLL,DAL), MVC(Model, view, Controller)
class Article : 
    def __init__(self,titre,prix,description,id=None):
        self.id = id
        self.titre = titre
        self.prix = prix
        self.description = description
        self.__connexion = None
        self.__c = None 
    
    def __enter__(self):
        self.__connexion = sqlite3.connect("articles.db")
        self.__c = self.__connexion.cursor()
        self.__c.execute("CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, titre TEXT, prix REAL, description TEXT)")
        return self

    def save(self):
        self.__c.execute("INSERT INTO articles (titre, prix, description) VALUES (?, ?, ?)",(self.titre, self.prix, self.description))
        self.__connexion.commit()

    def find_all(self):
        self.__c.execute("SELECT * FROM articles")
        articles_tuple = self.__c.fetchall()
        # mapping
        articles = []
        for a in articles_tuple:
            articles.append(Article(a[1],a[2],a[3],a[0]))
        return articles

    def __exit__(self,_,__,___):# self, exc_type, exc_value, exc_traceback
        if(self.__connexion is None): return        
        self.__connexion.close()

    def __str__(self):
        return f"Id: {self.id}, Titre: {self.titre}, Prix: {self.prix}, Description: {self.description}"
    
with Article("Samsung",500,"Smartphone...") as a:
    a.save()
    articles = a.find_all()
    for article in articles:
        print(article)
