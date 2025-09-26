"""
IHM Frame
"""
from tkinter import Tk, Frame, Label, Button, Toplevel

root = Tk()
root.title("Conteneurs")

frame = Frame(root,bg = "red",borderwidth=2,relief="groove")
frame.pack(padx=20,pady=20)

label = Label(frame,bg= "red", text="Label dans un frame et le frame dans la fenêtre!")
label.pack(padx=5, pady=5)

def open_window():
    win = Toplevel(root)
    label = Label(win, text="Nouvelle fenetre")
    label.pack(padx=5)

button = Button(root,text="Ouvrir",command=open_window)
button.pack(pady=10)

root.mainloop()
