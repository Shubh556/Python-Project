from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x655")
root.title("Slider GUI")
def rating():
    tmsg.showinfo("File Saved","Your File has been Saved")
    # print("Thanks For Your Rating")
    with open("Rating_record.txt","a") as f:
        f.write(f"The Rating is {myslider.get()}\n")
def getrating():
    tmsg.showinfo("File Opening","Your File is Openning ")
    f=open("Rating_record.txt","r")
    print(f.read())
Label(root,text="Based On Our Service Kindly RATE US ").pack()
myslider=Scale(root,from_=0,to=10,orient=HORIZONTAL,tickinterval=5)
myslider.set(8)
myslider.pack()
Button(root,text="Submit Your Rating",command=rating).pack()
Button(root,text="View Customer Rating",command=getrating).pack()
root.mainloop()