from tkinter import *


def calculate_product():
    try:
        num1 = float(name_entry.get())
        num2 = float(name_entry1.get())
        product = num1 * num2
        result_label.config(text=f"The product is = {product}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

window = Tk()
window.title('Getting started with widgets')
window.geometry('400x300')

lbl = Label(window, text="Add two numbers, get the product!", fg="white", bg="#072F5F", height=1, width=300)
lbl.pack(pady=10)

name_lbl = Label(window, text="Enter the first number", bg="#3895D3")
name_lbl.pack()
name_entry = Entry(window)
name_entry.pack()

name_lbl1 = Label(window, text="Enter the second number", bg="#3895D3")
name_lbl1.pack()
name_entry1 = Entry(window)
name_entry1.pack()

calculate_btn = Button(window, text="Calculate Product", command=calculate_product)
calculate_btn.pack(pady=10)

result_label = Label(window, text="The product is =", bg="lightgray")
result_label.pack(pady=10)

window.mainloop()
