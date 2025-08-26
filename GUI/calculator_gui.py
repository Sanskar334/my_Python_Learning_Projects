import re
import tkinter as tk
import sys
sys.path.append(r"F:\Python Programming") # This is the file location.
from Error_Handling import my_package # importing calculation functions which I have created previously in my first few days of learning.

class calculator_gui:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x600") # This is the default size of the frame.
        self.window.title("Basic Calculator")

        self.title = tk.Label(self.window, text="Welcome to basic calculator", font = ("Helvetica", 18))
        self.title.pack(padx=10, pady=20)

        '''Creating textbox(where the) here.'''
        self.textbox = tk.Entry(self.window, font = ("Helvetica", 16))
        self.textbox.pack(padx=10, pady=10)

        # button = tk.Button(window, text = "Click Me", font = ("Helvetica", 14))
        # button.pack(padx=10, pady=10)

        '''Create the button grid here.'''
        self.buttonframe = tk.Frame(self.window)
        for i in range(5):
            self.buttonframe.rowconfigure(i, weight=1) # Ensures that rows are filled equally if extra space is available.
        for j in range(4):
            self.buttonframe.columnconfigure(j, weight=1) # # Ensures that columns(buttons) are filled equally if extra space is available.

        '''This is what each row and column should contains string is text "CE", middle number 0 is row number, the next one 1 is column number.'''
        self.buttons = [
            ("CE", 0, 0), ("C", 0, 1), ("%", 0, 2), ("/", 0, 3),
            ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
            ("+/-", 4, 0), ("0", 4, 1), (".", 4, 2), ("=", 4, 3)
        ]

        '''Creates several buttons and then aligns them in a grid.'''
        for text, row, column in self.buttons:
            btn = tk.Button(self.buttonframe, text=text, font = ("Helvetica", 14), height = 2, command = lambda t = text: self.on_button_click(t))
            btn.grid(row = row, column = column, sticky = "nsew") # nsew stands for north, south (top & bottom), east, west (left & right).

        self.buttonframe.pack(padx = 10, pady = 20, expand = True, fill = "both") # This truely expands and fill the buttons according to the frame.

        self.window.mainloop()

    '''Performing all the calculation operations using buttons.'''

    def on_button_click(self, press):
        match press:
            case "C":
                self.textbox.delete(0, "end")
            case "CE":
                current = self.textbox.get()
                self.textbox.delete(0, "end")
                self.textbox.insert(0, current[:-1])
            case "=":
                expression = self.textbox.get()
                try:
                    expression = re.sub(r"(\d+)%(\d+)", r"(\1/100)*\2", expression) # Replaces input%input with (input/100)*input for converting percentage into number.
                    result = eval(expression)
                    self.textbox.delete(0, "end")
                    self.textbox.insert(0, result)
                except:
                    self.textbox.delete(0, "end")
                    self.textbox.insert(0, "Error")
            case _:
                self.textbox.insert("end", press)