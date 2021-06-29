from tkinter import *

root = Tk()


def storeval():
    print("Submit")
    print(f"{nameval.get(), conval.get(), payval.get(), cashval.get()}")
    with open("VE_record.txt", "a") as f:
        f.write(f"1.{nameval.get(), conval.get(), payval.get(), cashval.get()}\n")


def accval():
    f = open("VE_record.txt", "r")
    print(f.read())


root.geometry("500x300")
root.title("VE Software")
Label(root, text="Vishal Enterprises", font="Gabriola 15", pady=10).grid(row=0, column=3)
name = Label(root, text="Name")
con = Label(root, text="Contact Details")
amt = Label(root, text="Amount")
pay = Label(root, text="Payment Mode")
# Pack The Form
name.grid(row=1, column=2)
con.grid(row=2, column=2)
amt.grid(row=3, column=2)
# Store Value
nameval = StringVar()
conval = StringVar()
payval = IntVar()
cashval = IntVar()
amtval = IntVar()
# Entry
nameentry = Entry(root, textvariable=nameval)
conentry = Entry(root, textvariable=conval)
amtentry = Entry(root, textvariable=amtval)
# Pack Entry
nameentry.grid(row=1, column=3)
conentry.grid(row=2, column=3)
amtentry.grid(row=3, column=3)
Label(root, text="Payment Gateway", font="Gabriola 15", pady=10).grid(row=4, column=3)
C1 = Radiobutton(root, text="Cash", variable=payval, value=1)
C1.grid(row=6, column=2)
C2 = Radiobutton(root, text="E-Pay", variable=payval, value=2)
C2.grid(row=8, column=2)
Button(text="Submit", command=storeval).grid(row=9, column=4)
Button(text="Access The File", command=accval).grid(row=10, column=4)

root.mainloop()
