from tkinter import Tk, Button, Toplevel, Label

class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("App")
        Button(self, text="Open 1", command=self.open1).pack(padx=5, pady=5)
        Button(self, text="Open 2", command=self.open2).pack(padx=5, pady=5)
    

    def open1(self):
        fenetre_secondaire = Toplevel(self)
        Label(fenetre_secondaire, text="Fenêtre Secondaire 1").pack(padx=5,pady=5)
    
    def open2(self):
        fenetre_secondaire = Toplevel(self)
        Label(fenetre_secondaire, text="Fenêtre Secondaire 2").pack(padx=5,pady=5)

app = App()
app.mainloop()