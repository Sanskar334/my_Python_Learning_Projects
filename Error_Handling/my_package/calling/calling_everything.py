# from basic_calculator.arithmetic_functions import all_functions
# from ..basic_calculator.arithematic_functions import * # if got an error remember that you have imported userinput twice once in init and another in arithematic_functions
from . import *

while True:
    print(f'''\nWelcome to the calculator menu\n
1. Arithematic Functions.\n2. Generate Table. \n3. Convert Unit.''')
    choice = input("\nWhat would you like to perform?\n").lower()

    if choice in ["arithematic operation", "arithematic", "calculations"]:

        # call = ArithematicFunctions()

        print('''\nWe support the following operations:
1. Addition\n2. Subtraction\n3. Multiplication\n4. Division''')
        operation = input("\nWhich operation do you wish to perform?\n").lower()

        if operation in ["addition", "add"]:
            subcall = addition()
            # break
        elif operation in ["subtraction", "subtract"]:
            subcall = subtraction()
            # break
        elif operation in ["multiplication", "multiply"]:
            subcall = multiplication()
            # break
        elif operation in ["division", "divide"]:
            subcall = division()
            # break
        else:
            print("\nPlease enter a valid input\n")

    elif choice in ["generate table", "table generate", "table"]:
        call = table()
        # call.table()
        break

    elif choice in ["unit converter", "unit", "converter", "convert"]:
        # call = UnitConverter()

        print('''\nWe support the following units:
1. Miles to Kilometre\n2. Metre to Centimetre\n3. Metre to Inches\n4. Inches to Feets''')
        operation = input("\nWhich operation do you wish to perform?\n").lower()

        if operation in ["miles to kilometre", "kilometre converter", "mile", "kilometre", "miles"]:
            subcall = miles_to_kilometres()
            # break
        elif operation in ["metre to centimetre", "centimeter converter", "metre", "centimetre", "metres"]:
            subcall = metre_to_cm()
            # break
        elif operation in ["metre to inches", "inche", "inch converter", "inches"]:
            subcall = metre_to_inches()
            # break
        elif operation in ["inches to feet", "feet converter", "feet", "feets", "inch to feets", "inch to feet"]:
            subcall = inches_to_feets()
            # break
        else:
            print("\nPlease enter a valid input\n")

    else:
        print("\nPlease enter a valid input.")