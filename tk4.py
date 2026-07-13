from tkinter import *

window = Tk()
window.title("convert inches to cm")
window.geometry("400x300") 

def cm():
    x = float(e.get())
    l.config(text=x * 2.54)



e = Entry(window)
e.pack()

Button(window, text="Convert", command=cm).pack()

l = Label(window)
l.pack()

window.mainloop()