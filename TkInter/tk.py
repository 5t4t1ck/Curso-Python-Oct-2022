from tkinter import *

root = Tk()
root.title("Abacom")
root.geometry("800x600")

label0 = Label(root, text="Bienvenidos a Interfaces Gráficas!!!")
label1 = Label(root, text="Esto es una segunda línea")
label2 = Label(root, text="Esto es una tercera línea")
label3 = Label(root, text="                         ")
label4 = Label(root, text="                         ")

"""label0.pack()
label1.pack()
label2.pack()"""

label0.grid(row=0,column=0)
label3.grid(row=1, column=1)
label1.grid(row=2,column=2)
label4.grid(row=3,column=3)
label2.grid(row=4,column=4)

root.mainloop()

