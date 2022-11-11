# Crear una aplicación que transforme Pies a Metros

from tkinter import *

root = Tk()
root.title("Pies a Metros")
root.geometry("800x600")

def calcaular(*args):
    try:
        value = float(pies.get())
        m = int(0.3048 * value * 10000 + 0.5)/10000
        metros.set(m)
    except ValueError:
        metros.set("Error")

frame = Frame(root, pady=3, padx=12)
frame.grid(row=0, column=0)

pies = StringVar()
pies_input = Entry(frame, width=7, textvariable=pies)
pies_input.grid(row=0, column=1)

metros = StringVar()
Label(frame, textvariable=metros).grid(row=1, column=1)

Button(frame, text="Calcular", command=calcaular).grid(row=2, column=2)

Label(frame, text="Pies").grid(row=0, column=0)
Label(frame, text="es igual a").grid(row=1, column=0)
Label(frame, text="metros").grid(row=1, column=2)

pies_input.focus()
root.bind("<Return>")


root.mainloop()