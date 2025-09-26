"""
MainWindow c'est une interface graphique (fenetre principale)
"""
from tkinter import Tk, Label, Entry, Button
from bll.client_service import ClientService

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Fiche Client")
        self.client_service = ClientService()

        self.prenom_label = Label(self, text= "Prénom:")
        self.prenom_label.grid(row = 0, column=0)
        self.prenom_entry = Entry(self)
        self.prenom_entry.grid(row = 0, column = 1)

        self.nom_label = Label(self, text= "Nom:")
        self.nom_label.grid(row = 1, column=0)
        self.nom_entry = Entry(self)
        self.nom_entry.grid(row = 1, column = 1)

        self.adresse_label = Label(self, text= "Adresse:")
        self.adresse_label.grid(row = 2, column=0)
        self.adresse_entry = Entry(self)
        self.adresse_entry.grid(row = 2, column = 1)

        self.tel_label = Label(self, text= "Tel°:")
        self.tel_label.grid(row = 3, column=0)
        self.tel_entry = Entry(self)
        self.tel_entry.grid(row = 3, column = 1)

        self.sauvgarder_btn = Button(text="Sauvgarder", command=self.sauvgarder)
        self.sauvgarder_btn.grid(row=4,columnspan=2)

    def sauvgarder(self):
        prenom = self.prenom_entry.get()
        nom = self.nom_entry.get()
        adresse = self.adresse_entry.get()
        tel = self.tel_entry.get()
        self.client_service.creer_client(prenom, nom, tel, adresse)

