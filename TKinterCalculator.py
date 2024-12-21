from tkinter import *
from tkinter import messagebox
from decimal import Decimal
import math

# Globally declare the expression variable
expression = "0"

# Function to update expression
def press(num):
    global expression
    if expression == "0" and num != ".":
        expression = str(num)
    elif expression == "0" and num == "-":
        expression = "-"
    elif num == "." and "." not in expression.split()[-1]:
        expression += str(num)
    elif num != ".":
        expression += str(num)
    equation.set(expression)  # Update the display

def key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/.%":
        press(key)
    elif key == "=" or key == "\r":  # Enter key
        equalpress()
    elif key == "\x08":  # Backspace key
        backspace()
    elif key == "\x7f":  # DEL key
        backspace()

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        
        total = Decimal(total).normalize()  
        equation.set(str(total))
        expression = str(total)
    except Exception:
        equation.set("Error")
        expression = "0"

# Function to clear the contents
def clear():
    global expression
    expression = "0"
    equation.set("0")

# Function to delete the last character (backspace)
def backspace():
    global expression
    # Remove the last character, reset to "0" if empty
    expression = expression[:-1] if len(expression) > 1 else "0"
    equation.set(expression)

# Scientific Functions
def sin_func():
    try:
        global expression
        result = math.sin(math.radians(float(expression)))  # Convert input to radians
        equation.set(result)
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = "0"

def cos_func():
    try:
        global expression
        result = math.cos(math.radians(float(expression)))  # Convert input to radians
        equation.set(result)
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = "0"

def tan_func():
    try:
        global expression
        result = math.tan(math.radians(float(expression)))  # Convert input to radians
        equation.set(result)
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = "0"

def rad_to_deg():
    try:
        global expression
        result = math.degrees(float(expression))  # Convert radians to degrees
        equation.set(result)
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = "0"

def deg_to_rad():
    try:
        global expression
        result = math.radians(float(expression))  # Convert degrees to radians
        equation.set(result)
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = "0"

def exponent_func():
    try:
        global expression
        result = math.exp(float(expression))  # Exponentiation
        equation.set(result)
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = "0"

def log_func():
    try:
        global expression
        result = math.log10(float(expression))  # Logarithm (base 10)
        equation.set(result)
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = "0"

def ln_func():
    try:
        global expression
        result = math.log(float(expression))  # Natural logarithm
        equation.set(result)
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = "0"

def pi_func():
    global expression
    equation.set(math.pi)
    expression = str(math.pi)

def round_func():
    try:
        global expression
        result = round(float(expression), 2)  # Round to 2 decimal places
        equation.set(result)
        expression = str(result)
    except ValueError:
        equation.set("Error")
        expression = "0"

# Function to calculate dynamic font size
def calculate_font_size():
    window_width = gui.winfo_width()  # Get the current width of the window
    window_height = gui.winfo_height()  # Get the current height of the window

    # Base font size that adjusts dynamically
    font_size = min(window_width, window_height) // 18  # Adjust this divisor to change responsiveness
    return font_size

# Function to display About information
def about():
    messagebox.showinfo(
        "About",
        "Calculator App\n"
        "Programmer: Cesar M. Celestial Jr.\n"
        "Description: A simple calculator application that supports basic and scientific calculations.\n"
        "It includes functions like sin, cos, tan, log, and more."
    )

# Function to exit the application
def exit_application():
    gui.destroy()

# Driver code
if __name__ == "__main__":

    # Create a GUI window
    gui = Tk()
    gui.title("Calculator")
    gui.geometry("340x480")
    gui.configure(bg="#1e1e1e")

    # StringVar() instance
    equation = StringVar()
    equation.set(expression)

    # Menu bar
    menubar = Menu(gui)

    # File menu
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="Scientific Calculator", command=lambda: switch_to_scientific())
    file_menu.add_command(label="Basic Calculator", command=lambda: switch_to_basic())
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_application)
    menubar.add_cascade(label="File", menu=file_menu)

    # Help menu
    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=about)
    menubar.add_cascade(label="Help", menu=help_menu)
    
    # Display the menu
    gui.config(menu=menubar)

    # Get the dynamic font size
    font_size = calculate_font_size()

    # Button style options
    button_params = {
        'fg': 'white',
        'bg': '#333333',
        'font': ('Arial', font_size),
        'height': 2,
        'width': 4,
        'bd': 0,
        'highlightthickness': 0,
    }
    operator_params = {
        'fg': 'white',
        'bg': '#ff9500',
        'font': ('Arial', font_size),
        'height': 2,
        'width': 4,
        'bd': 0,
        'highlightthickness': 0,
    }
    special_params = {
        'fg': 'black',
        'bg': '#d3d3d3',
        'font': ('Arial', font_size),
        'height': 2,
        'width': 4,
        'bd': 0,
        'highlightthickness': 0,
    }

    # Button layout for scientific calculator
    def switch_to_scientific():
        global expression
        expression = "0"
        equation.set(expression)

        # Remove all existing buttons and create new ones
        for widget in gui.grid_slaves():
            widget.grid_forget()

         # Display expression field
        expression_field = Entry(gui, textvariable=equation, font=('Arial', 24), bg="#1e1e1e", fg="white", bd=0, justify=RIGHT)
        expression_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=(20, 10), sticky="we")

        # Scientific buttons
        scientific_buttons = [
             ('AC', 1, 0, special_params, clear), 
            ('⌫', 1, 1, special_params, backspace),
            ('sin', 1, 2, special_params, sin_func),
            ('cos', 1, 3, special_params, cos_func),

            ('tan', 2, 0, special_params, tan_func),
            ('deg->rad', 2, 1, special_params, deg_to_rad),
            ('rad->deg', 2, 2, special_params, rad_to_deg),
            ('exp', 2, 3, special_params, exponent_func),

            ('log', 3, 0, special_params, log_func),
            ('ln', 3, 1, special_params, ln_func),            
            ('π', 3, 2, special_params, pi_func),
            ('round', 3, 3, special_params, round_func),           

            ('7', 4, 0, button_params, lambda: press(7)),
            ('8', 4, 1, button_params, lambda: press(8)),
            ('9', 4, 2, button_params, lambda: press(9)),
            ('/', 4, 3, operator_params, lambda: press('/')),

            ('4', 5, 0, button_params, lambda: press(4)),
            ('5', 5, 1, button_params, lambda: press(5)),
            ('6', 5, 2, button_params, lambda: press(6)),
            ('*', 5, 3, operator_params, lambda: press('*')),

            ('1', 6, 0, button_params, lambda: press(1)),
            ('2', 6, 1, button_params, lambda: press(2)),
            ('3', 6, 2, button_params, lambda: press(3)),
            ('-', 6, 3, operator_params, lambda: press('-')),

            ('0', 7, 0, button_params, lambda: press(0)),
            ('.', 7, 1, button_params, lambda: press('.')),
            ('=', 7, 2, operator_params, equalpress),
            ('+', 7, 3, operator_params, lambda: press('+')),
        ]

        # Add scientific buttons to the grid
        for (text, row, col, params, cmd) in scientific_buttons:
            Button(gui, text=text, command=cmd, **params).grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        # Configure rows and columns to make them resize with the window
        for i in range(8):  # Rows for scientific
            gui.grid_rowconfigure(i, weight=1)
        for j in range(4):  # Columns for scientific
            gui.grid_columnconfigure(j, weight=1)

    # Button layout for basic calculator
    def switch_to_basic():
        global expression
        expression = "0"
        equation.set(expression)

        # Remove all existing buttons and create basic buttons
        for widget in gui.grid_slaves():
            widget.grid_forget()

        # Display expression field
        expression_field = Entry(gui, textvariable=equation, font=('Arial', 24), bg="#1e1e1e", fg="white", bd=0, justify=RIGHT)
        expression_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=(20, 10), sticky="we")
        
        basic_buttons = [
            ('AC', 1, 0, special_params, clear), 
            ('⌫', 1, 1, special_params, backspace), 
            ('%', 1, 2, special_params, lambda: press('%')), 
            ('/', 1, 3, operator_params, lambda: press('/')),

            ('7', 2, 0, button_params, lambda: press(7)), 
            ('8', 2, 1, button_params, lambda: press(8)), 
            ('9', 2, 2, button_params, lambda: press(9)), 
            ('*', 2, 3, operator_params, lambda: press('*')),

            ('4', 3, 0, button_params, lambda: press(4)), 
            ('5', 3, 1, button_params, lambda: press(5)), 
            ('6', 3, 2, button_params, lambda: press(6)), 
            ('-', 3, 3, operator_params, lambda: press('-')),

            ('1', 4, 0, button_params, lambda: press(1)), 
            ('2', 4, 1, button_params, lambda: press(2)), 
            ('3', 4, 2, button_params, lambda: press(3)), 
            ('+', 4, 3, operator_params, lambda: press('+')),

            ('0', 5, 0, button_params, lambda: press(0)), 
            ('.', 5, 2, button_params, lambda: press('.')), 
            ('=', 5, 3, operator_params, equalpress),
        ]        

        # Add basic buttons to the grid
        for (text, row, col, params, cmd) in basic_buttons:
            if text == '0':
                Button(gui, text=text, command=cmd, **params).grid(row=row, column=col, columnspan=2, sticky="nsew", padx=1, pady=1)
            else:
                Button(gui, text=text, command=cmd, **params).grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

        # Configure rows and columns for basic mode
        for i in range(6):  # Rows for basic
            gui.grid_rowconfigure(i, weight=1)
        for j in range(4):  # Columns for basic
            gui.grid_columnconfigure(j, weight=1)

    # Start with basic calculator
    switch_to_basic()

    # Set the key press event
    gui.bind("<Key>", key_press)

    # Start the GUI loop
    gui.mainloop()
