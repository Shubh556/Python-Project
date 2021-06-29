from tkinter import *
root=Tk()
root.geometry("300x300")
root.title("GUI")
lab=Label(text="Ready",bg="yellow",fg="green")
lab.pack(side=BOTTOM,anchor="se",fill=X)
lab.pack()
root.mainloop()