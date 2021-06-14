from tkinter import *
root=Tk()
root.geometry("455x655")
root.title("Slider GUI")
def rating():
    print("Thanks For Your Rating")
    with open("Rating_record.txt","a") as f:
        f.write(f"The Rating is {myslider.get()}\n")
def getrating():
    f=open("Rating_record.txt","r")
    print(f.read(7))
Label(root,text="Based On Our Service Kindly RATE US ").pack()
myslider=Scale(root,from_=0,to=10,orient=HORIZONTAL,tickinterval=5)
myslider.set(8)
myslider.pack()
Button(root,text="Submit Your Rating",command=rating).pack()
Button(root,text="View Customer Rating",command=getrating).pack()
root.mainloop()