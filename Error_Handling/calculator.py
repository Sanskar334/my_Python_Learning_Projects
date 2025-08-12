class Menu:
    def __init__(self):
        print(f'''\nWelcome to the calculator menu\n
1. Arithematic Functions.\n2. Generate Table. \n3. Convert Unit.''')
        # print("\nNote: you can exit by typing \"Exit\".")

class ArithematicFunctions:
    def userinput(self):
        while True:
            try:
                self.number_1 = float(input("\nEnter 1st number: "))
                self.number_2 = float(input("Enter 2nd number: "))
                break
            except ValueError:
                # raise ValueError("The input is not a valid number.") # I can also rasie cutom error here
                print("\nYour input is not a valid number.\n")
        
    def addition(self):
            self.userinput()
            add = self.number_1 + self.number_2
            print(f"\nThe addition of {self.number_1} and {self.number_2} is: {add}\n")

    def subtraction(self):
        self.userinput()
        subtract = self.number_1 - self.number_2
        print(f"\nThe subtraction of {self.number_1} and {self.number_2} is: {subtract}\n")

    def multiplication(self):
        self.userinput()
        multiplication = self.number_1 * self.number_2
        print(f"\nThe multiplication of {self.number_1} and {self.number_2} is: {multiplication}\n")

    def division(self):
        try:
            self.userinput()
            division = self.number_1 / self.number_2
            print(f"\nThe division of {self.number_1} and {self.number_2} is: {division}\n")
        except:
            print("Any number divided by 0 is not defined.")

class TableGenerator:
    def table(self):
        while True:
            try:
                self.input = int(input("\nEnter a number to generate it's table: "))
                break
            except:
                print("\nYour input is not a valid number.\n")

        for i in range(1, 11):
            print(f"{self.input} X {i} = {self.input*i}")

class UnitConverter:
    def userinput(self):
        try:
            self.number = float(input("Enter the number you want to convert: "))
        except:
            print("\nYour input is not a valid number.")

    def miles_to_kilometres(self):
        self.userinput()
        convert = self.number * 1.60934
        print(f"{self.number}miles is: {convert}km")

    def metre_to_cm(self):
        self.userinput()
        convert = self.number * 100
        print(f"{self.number}m is: {convert}cm")

    def metre_to_inches(self):
        self.userinput()
        convert = self.number * 39.3701
        print(f"{self.number}m is: {convert}inches")

    def inches_to_feets(self):
        self.userinput()
        convert = self.number / 12
        print(f"{self.number}inches is: {convert}feets")

# Script begin from here.

while True:
    Menu()
    choice = input("\nWhat would you like to perform?\n").lower()

    if choice in ["arithematic operation", "arithematic", "calculations"]:

        call = ArithematicFunctions()

        print('''\nWe support the following operations:
1. Addition\n2. Subtraction\n3. Multiplication\n4. Division''')
        operation = input("\nWhich operation do you wish to perform?\n").lower()

        if operation in ["addition", "add"]:
            subcall = call.addition()
            # break
        elif operation in ["subtraction", "subtract"]:
            subcall = call.subtraction()
            # break
        elif operation in ["multiplication", "multiply"]:
            subcall = call.multiplication()
            # break
        elif operation in ["division", "divide"]:
            subcall = call.division()
            # break
        else:
            print("\nPlease enter a valid input\n")

    elif choice in ["generate table", "table generate", "table"]:
        call = TableGenerator()
        call.table()
        # break

    elif choice in ["unit converter", "unit", "converter", "convert"]:
        call = UnitConverter()

        print('''\nWe support the following units:
1. Miles to Kilometre\n2. Metre to Centimetre\n3. Metre to Inches\n4. Inches to Feets''')
        operation = input("\nWhich operation do you wish to perform?\n").lower()

        if operation in ["miles to kilometre", "kilometre converter", "mile", "kilometre", "miles"]:
            subcall = call.miles_to_kilometres()
            # break
        elif operation in ["metre to centimetre", "centimeter converter", "metre", "centimetre", "metres"]:
            subcall = call.metre_to_cm()
            # break
        elif operation in ["metre to inches", "inche", "inch converter", "inches"]:
            subcall = call.metre_to_inches()
            # break
        elif operation in ["inches to feet", "feet converter", "feet", "feets", "inch to feets", "inch to feet"]:
            subcall = call.inches_to_feets()
            # break
        else:
            print("\nPlease enter a valid input\n")

    else:
        print("\nPlease enter a valid input.")