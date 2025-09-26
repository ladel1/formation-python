from tkinter import Tk, Label, Entry, Button

root = Tk()
root.title("Grid")

Label(root, text="Prénom: ").grid(row = 0, column = 0)
Entry(root).grid(row = 0, column = 1)
Label(root, text="Nom: ").grid(row = 1, column = 0)
Entry(root).grid(row = 1, column = 1)
Button(root, text="Valider").grid(row = 2, column = 0)

root.mainloop()
