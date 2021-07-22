import subprocess
import tkinter.messagebox as tmsg
from sys import path
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

root = Tk()
root.title("Python IDE")
root.geometry("1366x768")
file_path = ""


def setfilepath(path):
    global file_path
    file_path = path


def openfile(editor):
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r')as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        setfilepath(path)


def save_as():
    if file_path == "":
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        setfilepath(path)


def run(output):
    if file_path == "":
        tmsg.showinfo("File Not Saved", "Program Won't Run")
        return
    command = f'python {file_path} '
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, error = process.communicate()
    output.insert('1.0', out if not error else error)


menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=lambda: openfile(editor))
# file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

Run_menu = Menu(menu_bar, tearoff=0)
Run_menu.add_command(label='Run', command=lambda: run(output))
menu_bar.add_cascade(label='Run', menu=Run_menu)
root.config(menu=menu_bar)
editor = Text(root,height=10)
output = Text(height=10)
editor.pack()
output.pack()
root.mainloop()
