from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")

def messege() :
    messagebox.showwarning("ALERT!!","STOP!! VIRUS FOUND!!")

def messege1():
    messagebox.askquestion("question","Do you want to continue using your dangerous device?")

def messege2():
    messagebox.showinfo("contact","For more detail,subscribe to our page")


btn = Button(root,text="Scan for virus",command=messege)
btn.place(x = 40, y=80)

btn1 = Button(root,text="Continue",command=messege1)
btn1.place(x = 40, y = 160)

btn2= Button(root,text="contact",command=messege2)
btn2.place(x=40,y = 240)



root.mainloop()