import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo


def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension='.txt',
                           filetype=[("All Files", "*.*"), ("Text Document", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetype=[("All Files", "*.*"), ("Text Document", "*.txt")])
        # print("Hii")
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            showinfo("File Saved", "Your File Has BEen Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def Exit():
    root.destroy()


def about():
    showinfo("Notepad", "Created By DDX")


def Cut():
    TextArea.event_generate(("<<Cut>>"))


def Copy():
    TextArea.event_generate(("<<Copy>>"))


def Paste():
    TextArea.event_generate(("<<Paste>>"))


if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("455x655")
    TextArea = Text(root, font="InkDraft 12")
    file = None
    TextArea.pack(expand=True, fill=BOTH)
    MenuBar = Menu(root)
    # File MENU Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newfile)
    FileMenu.add_command(label="Open", command=openfile)
    FileMenu.add_command(label="Save", command=savefile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=Exit)
    # MenuBar.add_cascade(label="File",menu=FileMenu)
    # FileMenu.add_separator()
    # FileMenu.add_command(label="Change Fonts", command=Change_Fonts)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # submenu.add_cascade(label="File",menu=FileMenu)
    # Edit MENU Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=Cut)
    EditMenu.add_command(label="Copy", command=Copy)
    EditMenu.add_command(label="Paste", command=Paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # Help MENU Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    root.config(menu=MenuBar)
    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    root.mainloop()
