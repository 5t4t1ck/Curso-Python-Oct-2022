from tkinter import *

root = Tk()
root.title("Abacom")
root.geometry("800x600")

frame = LabelFrame(root, text="Login")
frame.pack(padx=50, pady=200)

#label = Label(frame, text="Este texto es parte de un frame")
label = Label(frame, padx=10, pady=10, borderwidth=10)
btn = Button(frame, text="Salir", command=root.quit)

label.pack()
btn.pack()

root.mainloop()