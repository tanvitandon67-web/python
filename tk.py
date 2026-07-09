from tkinter import *

def age():
    year = int(box.get())
    answer.config(text=2026 - year)

window = Tk()

Label(window, text="Birth Year").pack()

box = Entry(window)
box.pack()

Button(window, text="Age", command=age).pack()

answer = Label(window, text="")
answer.pack()

window.mainloop()