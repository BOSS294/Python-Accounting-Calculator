import tkinter as tk
from tkinter import ttk

def add():
    try:
        result.set(float(num1.get()) + float(num2.get()))
    except ValueError:
        result.set("Invalid Input")

def subtract():
    try:
        result.set(float(num1.get()) - float(num2.get()))
    except ValueError:
        result.set("Invalid Input")

def multiply():
    try:
        result.set(float(num1.get()) * float(num2.get()))
    except ValueError:
        result.set("Invalid Input")

def divide():
    try:
        result.set(float(num1.get()) / float(num2.get()))
    except ValueError:
        result.set("Invalid Input")
    except ZeroDivisionError:
        result.set("Cannot divide by zero")

def clear():
    num1.set("")
    num2.set("")
    result.set("")

# Create the main window
root = tk.Tk()
root.title("Accounting Calculator")
root.configure(bg='blue')  # Set the background color to blue


# Create input fields
num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

entry1 = ttk.Entry(root, textvariable=num1, font=('Arial', 15))
entry2 = ttk.Entry(root, textvariable=num2, font=('Arial', 15))
entry1.grid(row=0, column=0, padx=10, pady=10)
entry2.grid(row=0, column=1, padx=10, pady=10)

# Create operator buttons
button_add = ttk.Button(root, text="Add", command=add)
button_subtract = ttk.Button(root, text="Subtract", command=subtract)
button_multiply = ttk.Button(root, text="Multiply", command=multiply)
button_divide = ttk.Button(root, text="Divide", command=divide)
button_clear = ttk.Button(root, text="Clear", command=clear)

button_add.grid(row=1, column=0, padx=5, pady=5)
button_subtract.grid(row=1, column=1, padx=5, pady=5)
button_multiply.grid(row=2, column=0, padx=5, pady=5)
button_divide.grid(row=2, column=1, padx=5, pady=5)
button_clear.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create the result label
label_result = ttk.Label(root, textvariable=result, font=('Arial', 20))
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
