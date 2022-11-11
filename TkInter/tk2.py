from tkinter import *

root=Tk()
root.title("Abacom")
root.geometry("800x600")

input = Entry(root, width=60)
input.pack()
input.insert(0, "Por favor ingresa un texto")

def click():
    text = input.get()
    label.configure(text=text)
    input.delete(0, END)

btn = Button(root, text="click", command=click)
btn.pack()

label = Label(root, text="Por favor ingresa un texto")
label.pack()

root.mainloop()