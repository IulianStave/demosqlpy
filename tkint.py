# Tkinter widgets, states
from tkinter import *

def convert_from_kg():
    grams = 1000 * float(e1_value.get())
    t1.delete("1.0", END)
    t1.insert(END, grams)

    pounds = 2.20462 * float(e1_value.get())
    t2.delete("1.0", END)
    t2.insert(END, pounds)

    ounces = 35.274 * float(e1_value.get())
    t3.delete("1.0", END)
    t3.insert(END, ounces)

window = Tk()

b1 = Button(window, text = "Convert", command = convert_from_kg)
b1.grid(row = 0, column = 2)

l1 = Label(window, text = "Kg")
l1.grid(row = 0, column = 0)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row=1, column =0)

t2 = Text(window, height = 1, width = 20)
t2.grid(row=1, column =1)

t3 = Text(window, height = 1, width = 20)
t3.grid(row=1, column =2)


window.mainloop()
