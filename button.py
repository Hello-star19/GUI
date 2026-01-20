from tkinter import*

window = Tk()
window.geometry("250x200")
window.resizable(False,False)
# label
title = Label(window, text = "Hello", foreground= "blue", font= ("Arial", 20))
title.place(x = 85,y= 30)

# Button
button = Button(window, text = "click me", background= "yellow", foreground= "black", font= ("Arial", 20),command = window.destroy)
button.place(x= 80, y =60)








window.mainloop()


