from tkinter import *

window = Tk()
# window size

# Application title
window.title("SimpleCalculator")
# Screen size defined
screen = Entry(window, width=40, borderwidth=4)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current_Value = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current_Value) + str(number))


def eraser():
    screen.delete(0, END)


def addition():
    first_num = screen.get()
    global value1
    global operation
    operation = "addition"
    value1 = int(first_num)
    screen.delete(0, END)


def subtraction():
    first_num = screen.get()
    global value1
    global operation
    operation = "subtraction"
    value1 = int(first_num)
    screen.delete(0, END)


def division():
    first_num = screen.get()
    global value1
    global operation
    operation = "division"
    value1 = int(first_num)
    screen.delete(0, END)


def multiply():
    first_num = screen.get()
    global value1
    global operation
    operation = "multiply"
    value1 = int(first_num)
    screen.delete(0, END)


def equals():
    value2 = screen.get()
    screen.delete(0, END)
    if operation == "addition":
        screen.insert(0, value1 + int(value2))
    elif operation == "subtraction":
        screen.insert(0, value1 - int(value2))
    elif operation == "multiplication":
        screen.insert(0, value1 * int(value2))
    elif operation == "division":
        screen.insert(0, value1 / int(value2))


button_1 = Button(window, text="1", padx=38, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=38, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=38, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=38, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=38, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=38, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=38, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=38, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=38, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="+", padx=37, pady=20, command=addition)
button_zero = Button(window, text="0", padx=38, pady=20, command=lambda: button_click(0))
button_del = Button(window, text="Del", padx=32, pady=20, bg="red", fg="white", command=lambda: eraser())
button_sub = Button(window, text="-", padx=39, pady=20, command=subtraction)
button_div = Button(window, text="/", padx=39, pady=20, command=division)
button_equal = Button(window, text="=", padx=37, pady=20, bg="blue", command=equals)
# position of buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_zero.grid(row=4, column=1)
button_del.grid(row=4, column=2)

button_sub.grid(row=5, column=0)
button_div.grid(row=5, column=1)
button_equal.grid(row=5, column=2)

window.mainloop()
