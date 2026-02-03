from tkinter import*

from tkinter.ttk import*

screen = Tk()
screen.geometry("400x350")
screen.config(background="white")

screen.title("Menu")
menu_bar = Menu(screen)

File = Menu(menu_bar,tearoff=0 )
menu_bar.add_cascade(label="File",menu=File)
File.add_command(label="New File",command=None)
File.add_command(label="Open File",command=None)
File.add_command(label="Save File",command=None)
File.add_command(label="Delete File",command=None)

Edit = Menu(menu_bar,tearoff=0 )
menu_bar.add_cascade(label="Edit",menu=Edit)
Edit.add_command(label="Undo",command=None)
Edit.add_command(label="Redo",command=None)
Edit.add_command(label="Cut",command=None)
Edit.add_command(label="Copy",command=None)
Edit.add_command(label="Paste",command=None)

View = Menu(menu_bar,tearoff=0 )
menu_bar.add_cascade(label="View",menu=View)
View.add_command(label="Search",command=None)
View.add_command(label="Run",command=None)
View.add_command(label="Extensions",command=None)
View.add_command(label="Output",command=None)

screen.config(menu=menu_bar)






screen.mainloop()
