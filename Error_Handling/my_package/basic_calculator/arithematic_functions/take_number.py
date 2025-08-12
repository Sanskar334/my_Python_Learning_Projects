def userinput():
    while True:
        try:
            number_1 = float(input("\nEnter 1st number: "))
            number_2 = float(input("Enter 2nd number: "))
            break
        except ValueError:
            # raise ValueError("The input is not a valid number.") # I can also rasie cutom error here
            print("\nYour input is not a valid number.\n")