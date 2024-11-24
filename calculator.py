from tkinter import *

# Function to update the expression on the screen
def button_click(char):
    global expression
    expression = expression + str(char)
    equation.set(expression)

# Function to clear the display
def button_clear():
    global expression
    expression = ""
    equation.set(expression)

# Function to evaluate the expression
def button_equal():
    try:
        global expression
        result = str(eval(expression))  # Evaluate the expression using eval
        equation.set(result)
        expression = result
    except:
        equation.set("Error")

# Main function
if __name__ == "__main__":
    expression = ""  # Stores the current expression

    # Create the main window
    calculator = Tk()
    calculator.title("Simple Calculator")

    # Create the display
    equation = StringVar()
    display = Entry(calculator, textvariable=equation)
    display.grid(columnspan=4, padx=10, pady=10)

    # Create buttons for numbers
    button7 = Button(calculator, text='7', width=3, command=lambda: button_click(7))
    button7.grid(row=1, column=0)
    button8 = Button(calculator, text='8', width=3, command=lambda: button_click(8))
    button8.grid(row=1, column=1)
    button9 = Button(calculator, text='9', width=3, command=lambda: button_click(9))
    button9.grid(row=1, column=2)
    button_div = Button(calculator, text='/', width=3, command=lambda: button_click('/'))
    button_div.grid(row=1, column=3)

    button4 = Button(calculator, text='4', width=3, command=lambda: button_click(4))
    button4.grid(row=2, column=0)
    button5 = Button(calculator, text='5', width=3, command=lambda: button_click(5))
    button5.grid(row=2, column=1)
    button6 = Button(calculator, text='6', width=3, command=lambda: button_click(6))
    button6.grid(row=2, column=2)
    button_mul = Button(calculator, text='*', width=3, command=lambda: button_click('*'))
    button_mul.grid(row=2, column=3)

    button1 = Button(calculator, text='1', width=3, command=lambda: button_click(1))
    button1.grid(row=3, column=0)
    button2 = Button(calculator, text='2', width=3, command=lambda: button_click(2))
    button2.grid(row=3, column=1)
    button3 = Button(calculator, text='3', width=3, command=lambda: button_click(3))
    button3.grid(row=3, column=2)
    button_sub = Button(calculator, text='-', width=3, command=lambda: button_click('-'))
    button_sub.grid(row=3, column=3)

    button0 = Button(calculator, text='0', width=3, command=lambda: button_click(0))
    button0.grid(row=4, column=0)
    button_dot = Button(calculator, text='.', width=3, command=lambda: button_click('.'))
    button_dot.grid(row=4, column=1)
    button_clear = Button(calculator, text='C', width=3, command=button_clear)
    button_clear.grid(row=4, column=2)
    button_add = Button(calculator, text='+', width=3, command=lambda: button_click('+'))
    button_add.grid(row=4, column=3)

    button_equal = Button(calculator, text='=', width=3, command=button_equal)
    button_equal.grid(row=5, columnspan=4)

    calculator.mainloop()
