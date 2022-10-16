from ast import operator
from distutils import text_file
from tkinter import *
from matplotlib import test
from numpy import number


root = Tk()
root.title("Simple Calculator")
root.configure(bg="#1b4f72")

textField = Entry(width=25, highlightthickness=5, bg="#d6eaf8", font="Cambria 11")
textField.configure(highlightbackground = "#1b4f72", highlightcolor= "#1b4f72")
textField.grid(row=0, column=0, columnspan=4)


def button_click(number):
    value = textField.get()
    textField.delete(0, END)
    textField.insert(0, str(value)+str(number))
    
def buttonClear():
    textField.delete(0, END)
    
def add():
    global first
    global operators
    operators = "+"
    first = textField.get()
    textField.delete(0, END)
    
def subtract():
    global first
    global operators
    operators = "-"
    first = textField.get()
    textField.delete(0, END)
    
def divide():
    global first
    global operators
    operators = "/"
    first = textField.get()
    textField.delete(0, END)

def multiply():
    global first
    global operators
    operators = "*"
    first = textField.get()
    textField.delete(0, END)
    
def equal():
    second = textField.get()
    textField.delete(0, END)
    try:
        if operators=="+":
            textField.insert(0, int(first)+int(second))
        elif operators=="-":
            textField.insert(0, int(first)-int(second))
        elif operators=="*":
            textField.insert(0, int(first)*int(second))
        elif operators=="/":
            try:
                textField.insert(0, int(first)/int(second))
            except ZeroDivisionError:
                textField.insert(0, "Zero Division")
    except ValueError:
        if operators=="+":
            textField.insert(0, float(first)+float(second))
        elif operators=="-":
            textField.insert(0, float(first)-float(second))
        elif operators=="*":
            textField.insert(0, float(first)*float(second))
        elif operators=="/":
            try:
                textField.insert(0, float(first)/float(second))
            except ZeroDivisionError:
                textField.insert(0, "Zero Division")

button_1 = Button(root, text="1", bg= '#2980b9', command=lambda: button_click(1), pady=10, padx=20, font="Cambria 11")
button_2 = Button(root, text="2", bg= '#2980b9', command=lambda: button_click(2), pady=10, padx=20, font="Cambria 11")
button_3 = Button(root, text="3", bg= '#2980b9', command=lambda: button_click(3), pady=10, padx=20, font="Cambria 11")
button_4 = Button(root, text="4", bg= '#2980b9', command=lambda: button_click(4), pady=10, padx=20, font="Cambria 11")
button_5 = Button(root, text="5", bg= '#2980b9', command=lambda: button_click(5), pady=10, padx=20, font="Cambria 11")
button_6 = Button(root, text="6", bg= '#2980b9', command=lambda: button_click(6), pady=10, padx=20, font="Cambria 11")
button_7 = Button(root, text="7", bg= '#2980b9', command=lambda: button_click(7), pady=10, padx=20, font="Cambria 11")
button_8 = Button(root, text="8", bg= '#2980b9', command=lambda: button_click(8), pady=10, padx=20, font="Cambria 11")
button_9 = Button(root, text="9", bg= '#2980b9', command=lambda: button_click(9), pady=10, padx=20, font="Cambria 11")
button_0 = Button(root, text="0", bg= '#2980b9', command=lambda: button_click(0), pady=10, padx=20, font="Cambria 11")
button_dot = Button(root, text=".", bg= '#2980b9', command=lambda: button_click("."), pady=10, padx=22, font="Cambria 11")


buttonClear = Button(root, text="Clear", bg= '#2980b9', command=buttonClear, pady=10, padx=97, font="Cambria 11")
buttonAdd = Button(root, text="+", bg= '#2980b9', command=add, pady=10, padx=20, font="Cambria 11")
buttonSubtract = Button(root, text="-", bg= '#2980b9', command=subtract, pady=10, padx=21, font="Cambria 11")
buttonMultiply = Button(root, text="X", bg= '#2980b9', command=multiply, pady=10, padx=20, font="Cambria 11")
buttonDivide = Button(root, text="/", bg= '#2980b9', command=divide, pady=10, padx=20, font="Cambria 11")
buttonEqual = Button(root, text="=", bg= '#2980b9', command=equal, pady=10, padx=20, font="Cambria 11")


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)
buttonEqual.grid(row=4, column=2)

buttonAdd.grid(row=1, column=3)
buttonSubtract.grid(row=2, column=3)
buttonMultiply.grid(row=3, column=3)
buttonDivide.grid(row=4,column=3)
buttonClear.grid(row=5, column=0, columnspan=4)


root.mainloop()

