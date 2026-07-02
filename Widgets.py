from tkinter import *
from datetime import date 

root = Tk()
root.title('Getting started with widgets')
root.geometry('600x400')

lbl = Label(text= 'Hello!',fg= 'white', bg="#072f5f",height= 1, width= 300)
name_lbl = Label(text= 'Full name', bg="#3895d3")
name_entry = Entry()

def display() :
    name = name_entry.get()
    global  message
    message = "Welcome to the application. /n Todays date is : "
    greet = "Hello"+ name + '/n'

    text_box.insert(END.greet)
    text_box.insert(END.messege)
    text_box.insert(END.date.today())

text_box = Text(height= 5,width= 40, bg= 'white',fg='black')

btn = Button(text= 'begin',command='display',height= 1,bg="#1261a0",fg = 'Dark blue')

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()