from tkinter import*

screen = Tk()
screen.geometry("450x500")
screen.config(background="white")

username = Label(screen, text = "Username", foreground= "black", font=("Calibri"))
username.place(x = 70, y=100)

password = Label(screen, text = "password", foreground="black", font=("Calibri"))
password.place( x= 70, y= 150)

entry_box1 = Entry(screen,width = 30 )
entry_box1.place( x= 165, y = 105) 

entry_box2 = Entry(screen,width = 30 )
entry_box2.place( x= 165, y = 155) 

submit_button = Button(screen, text = "Submit", foreground= "White", font=("Arial"), background="Navy")
submit_button.place(x= 70, y=200)

screen.mainloop()
