from tkinter import *


window = Tk()
window.title("Event Handler")
window.geometry("400x300")

def handler_keypress(event) :
    print(event.char)
    
window.bind("<Key>",handler_keypress)

def handler_click(event):
    print("\n The button was clicked")

btn = Button(text='clickme')
btn.pack()

btn.bind("<Button-1>",handler_click)


window.mainloop()