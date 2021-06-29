from tkinter import *


def getval():
    print(f"The Username is {userval.get()}")
    print(f"The Password is {passval.get()}")


root = Tk()
root.geometry("544x699")
user = Label(root, text="UserName")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)
userval = StringVar()
passval = StringVar()
serve = IntVar()
userentery = Entry(root, textvariable=userval)
passentry = Entry(root, textvariable=passval)
userentery.grid(row=0, column=1)
passentry.grid(row=1, column=1)
Button(text="Submit", command=getval).grid()
root.mainloop()
