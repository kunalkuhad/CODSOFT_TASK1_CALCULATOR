import tkinter as tk

def add_to_display(value):
    current = display_var.get()
    display_var.set(current + value)

def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

def clear_display():
    display_var.set("")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")

# Create the display widget
display_var = tk.StringVar()
display_var.set("")

display = tk.Entry(window, textvar=display_var, font=("Helvetica", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
for i in range(1, 10):
    row = (i - 1) // 3 + 1
    col = (i - 1) % 3
    number_button = tk.Button(window, text=str(i), font=("Helvetica", 20), command=lambda num=i: add_to_display(str(num)))
    number_button.grid(row=row, column=col, padx=5, pady=5)

# Create the zero button
zero_button = tk.Button(window, text="0", font=("Helvetica", 20), command=lambda: add_to_display("0"))
zero_button.grid(row=4, column=1, padx=5, pady=5)

# Create the arithmetic operation buttons
operations = ["+", "-", "*", "/"]
for i, op in enumerate(operations):
    op_button = tk.Button(window, text=op, font=("Helvetica", 20), command=lambda opr=op: add_to_display(opr))
    op_button.grid(row=i + 1, column=3, padx=5, pady=5)

# Create the equals button
equals_button = tk.Button(window, text="=", font=("Helvetica", 20), command=calculate)
equals_button.grid(row=4, column=2, padx=5, pady=5)

# Create the clear button
clear_button = tk.Button(window, text="C", font=("Helvetica", 20), command=clear_display)
clear_button.grid(row=4, column=0, padx=5, pady=5)

window.mainloop()
