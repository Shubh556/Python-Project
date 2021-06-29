from tkinter import *

root = Tk()
root.geometry("533x655")
f1 = Frame(root, bg="red", borderwidth="8", relief=RAISED)
f1.pack(side=TOP, fill="y")
l =Label(f1,text="Project")
l.pack(padx=150)
f2 = Frame(root, bg="yellow", borderwidth="8", relief=SUNKEN)
f2.pack(side=LEFT, fill="y")
l =Label(f2,text="Tkinter")
l.pack(pady=200)
root.mainloop()
