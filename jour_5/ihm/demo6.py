from tkinter import Tk

root = Tk()
def clic(event):
    print(f"Clique e, x: {event.x}, y: {event.y}")
# <Button-1> -> clique gauche
# <Button-3> -> clique droite
root.bind("<Double-3>", clic)

root.mainloop()