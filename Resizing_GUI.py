from tkinter import *

root = Tk()


def hw():
    print("Updating...")
    root.geometry(f"{height.get()}x{width.get()}")
    print("Updated....")


root.geometry("500x500")
root.title("Resizable Gui")
height = Label(root, text="Height").grid(row=1, column=3)
width = Label(root, text="Width").grid(row=2, column=3)
height = StringVar()
width = StringVar()
hentry = Entry(root, textvariable=height).grid(row=1, column=5)
wentry = Entry(root, textvariable=width).grid(row=2, column=5)
Button(text="Align Height and Width", command=hw).grid(row=5, column=5)

root.mainloop()
