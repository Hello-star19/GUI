from tkinter import *
import tkinter
from tkinter.ttk import*
from tkinter.filedialog import askopenfile

window = Tk()
window.geometry("350x200")
window.title("Open File")
window.config(bg="Green")

def open_file():
   file = askopenfile(mode= "r", filetypes= [("Python Files", "*.py")]) 
   if file is not None: 
      content = file.read()
      print(content)

button = tkinter.Button(window,text="Open", bd=7, bg ="Blue",fg="Yellow",command=open_file)
button.pack(side=TOP, pady=15)


window.mainloop()
