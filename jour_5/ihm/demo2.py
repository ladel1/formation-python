from tkinter import Tk, Label, Button

root = Tk()
root.title("Afficher un Label")
label = Label(root,text="Bonjour tout le monde!")
label.pack(padx=20,pady=5)

def on_click():
    print("blablabalab")

button = Button(root,text="ok", command=on_click)
button.pack(padx=5,pady=5)
root.mainloop()