import tkinter as tk

calculation = ""  

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)  # Add the symbol or number to the calculation string
    text_result.delete(1.0, "end")  # Clear the display field
    text_result.insert(1.0, calculation)  # Update the display field with the current calculation

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))  # Use eval to calculate the result of the calculation
        calculation = result  # Update the calculation with the result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)  # Show the result on the display field
    except:
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, "Error")  # Show error in case of invalid input

def backspace():
    global calculation
    calculation = calculation[:-1]  # Remove the last character
    text_result.delete(1.0, "end")  # Clear the display field
    text_result.insert(1.0, calculation)  # Update the display field with the current calculation

def toggle_parenthesis():
    global calculation
    # Count how many open and close parentheses are in the calculation
    open_parens = calculation.count('(')
    close_parens = calculation.count(')')
    
    if open_parens == close_parens:
        # If the number of open and close parentheses are equal, add an opening parenthesis
        calculation += '('
    else:
        # Otherwise, add a closing parenthesis
        calculation += ')'
    
    # Update the text field
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def clear_field():
    global calculation
    calculation = ""  # Reset the calculation string
    text_result.delete(1.0, "end")  # Clear the display field

root = tk.Tk()
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))  # Display field for showing calculations
text_result.grid(columnspan=5)

# Buttons to handle the calculator inputs
btn_1 = tk.Button(root, text="CE", command=lambda: clear_field(), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="C", command=lambda: clear_field(), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="B", command=lambda: backspace(), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_4.grid(row=2, column=4)

btn_5 = tk.Button(root, text="7", command=lambda: add_to_calculation("7"), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(root, text="8", command=lambda: add_to_calculation("8"), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=2)
btn_7 = tk.Button(root, text="9", command=lambda: add_to_calculation("9"), width=5, font=("Arial", 14))
btn_7.grid(row=3, column=3)
btn_8 = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_8.grid(row=3, column=4)

btn_9 = tk.Button(root, text="4", command=lambda: add_to_calculation("4"), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=1)
btn_10 = tk.Button(root, text="5", command=lambda: add_to_calculation("5"), width=5, font=("Arial", 14))
btn_10.grid(row=4, column=2)
btn_11 = tk.Button(root, text="6", command=lambda: add_to_calculation("6"), width=5, font=("Arial", 14))
btn_11.grid(row=4, column=3)
btn_12 = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_12.grid(row=4, column=4)

btn_13 = tk.Button(root, text="1", command=lambda: add_to_calculation("1"), width=5, font=("Arial", 14))
btn_13.grid(row=5, column=1)
btn_14 = tk.Button(root, text="2", command=lambda: add_to_calculation("2"), width=5, font=("Arial", 14))
btn_14.grid(row=5, column=2)
btn_15 = tk.Button(root, text="3", command=lambda: add_to_calculation("3"), width=5, font=("Arial", 14))
btn_15.grid(row=5, column=3)
btn_16 = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_16.grid(row=5, column=4)

btn_17 = tk.Button(root, text="()", command=toggle_parenthesis, width=5, font=("Arial", 14))
btn_17.grid(row=6, column=1)
btn_18 = tk.Button(root, text="0", command=lambda: add_to_calculation("0"), width=5, font=("Arial", 14))
btn_18.grid(row=6, column=2)
btn_19 = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_19.grid(row=6, column=3)
btn_20 = tk.Button(root, text="=", command=lambda: evaluate_calculation(), width=5, font=("Arial", 14), bg="#007BFF")
btn_20.grid(row=6, column=4)

root.mainloop()
