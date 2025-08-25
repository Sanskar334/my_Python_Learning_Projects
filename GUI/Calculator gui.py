import tkinter as tk

window = tk.Tk()
window.geometry("500x600") # This is the default size of the frame.
window.title("Basic Calculator")

title = tk.Label(window, text="Welcome to basic calculator", font = ("Helvetica", 18))
title.pack(padx=10, pady=20)

'''Creating textbox(where the) here.'''
textbox = tk.Text(window, height = 3, font = ("Helvetica", 16))
textbox.pack(padx=10, pady=10)

# button = tk.Button(window, text = "Click Me", font = ("Helvetica", 14))
# button.pack(padx=10, pady=10)

'''Create the button grid here.'''
buttonframe = tk.Frame(window)
for i in range(5):
    buttonframe.rowconfigure(i, weight=1) # Ensures that rows are filled equally if extra space is available.
for j in range(4):
    buttonframe.columnconfigure(j, weight=1) # # Ensures that columns(buttons) are filled equally if extra space is available.

'''This is what each row and column should contains string is text "CE", middle number 0 is row number, the next one 1 is column number.'''
buttons = [
    ("CE", 0, 0), ("C", 0, 1), ("❌", 0, 2), ("/", 0, 3),
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
    ("+/-", 4, 0), ("0", 4, 1), (".", 4, 2), ("=", 4, 3)
]

'''Creates several buttons and then aligns them in a grid.'''
for text, row, column in buttons:
    btn = tk.Button(buttonframe, text=text, font = ("Helvetica", 14), height = 2)
    btn.grid(row = row, column = column, sticky = "nsew") # nsew stands for north, south (top & bottom), east, west (left & right).

buttonframe.pack(padx = 10, pady = 20, expand = True, fill = "both") # This truely expands and fill the buttons according to the frame.

window.mainloop()

'''Logic not added yet. Only GUI is prepared.'''