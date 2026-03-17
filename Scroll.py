from tkinter import *
background = Tk()
background.geometry("450x300")
background.config(bg = "Blue")
w = Label(background,text = "Helo", font= "60^")
w.pack()
Scroll_bar = Scrollbar(background)
Scroll_bar.pack(side = RIGHT , fill=Y)

my_list = Listbox(background, yscrollcommand=Scroll_bar.set)
for line in range(52):
    my_list.insert(END,"ITEM Number" + str(line) + " Hi Mahid ")


my_list.pack(side = LEFT, fill=BOTH)
Scroll_bar.config(command = my_list.yview)
background.mainloop()
