from tkinter import *
root=Tk()
root.geometry("455x656")
def intro():
    print("My Self Jarvis")


f1=Frame(root,borderwidth=6,bg="yellow",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")
b1=Button(f1,fg="black",text="Click Here",command=intro)
b1.pack(side=RIGHT,pady=25)
root.mainloop()


