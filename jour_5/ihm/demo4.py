from tkinter import Tk, Label, Entry, Button, Radiobutton, Checkbutton

root = Tk()

Label(root,text="Prénom").pack(pady=5)
Entry(root).pack(pady=5,padx=10)
Label(root,text="Genre").pack(pady=5)
Radiobutton(root,text="F",value=1).pack(pady=5)
Radiobutton(root,text="M",value=0).pack(pady=5)
Checkbutton(root,text="lbalba").pack(pady=5)
Button(root,text="Valider").pack(pady=5)

root.mainloop()