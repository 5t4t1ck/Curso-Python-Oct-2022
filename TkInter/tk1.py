from tkinter import *

root = Tk()
root.title("Abacom")
root.geometry("800x600")

label = Label(root, text="Abacom")

def click():
    label.pack()

btn = Button(root, text="Click", command=click, fg="#fff000", bg="black")
btn.pack()

root.mainloop()