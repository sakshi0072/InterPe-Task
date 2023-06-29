import tkinter as tk
import math

def evaluate_expression():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def append_to_expression(value):
    entry.insert(tk.END, value)

def calculate_square_root():
    expression = entry.get()
    try:
        result = math.sqrt(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Scientific Calculator")

# Create an entry field for the expression
entry = tk.Entry(window, width=40)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for numbers and operations
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3)
]

for button in buttons:
    value, row, col = button
    tk.Button(window, text=value, width=10, command=lambda v=value: append_to_expression(v)).grid(row=row, column=col)

# Create additional buttons for special operations
tk.Button(window, text="Clear", width=10, command=clear_entry).grid(row=5, column=0)
tk.Button(window, text="√", width=10, command=calculate_square_root).grid(row=5, column=1)
tk.Button(window, text="Evaluate", width=10, command=evaluate_expression).grid(row=5, column=2)
tk.Button(window, text="Quit", width=10, command=window.quit).grid(row=5, column=3)

# Run the main event loop
window.mainloop()
