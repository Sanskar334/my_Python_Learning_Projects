from .take_number import userinput

def addition(number_1, number_2):
            return number_1 + number_2
            # print(f"\nThe addition of {number_1} and {number_2} is: {add}\n")

def subtraction(number_1, number_2):

        return number_1 - number_2

def multiplication(number_1, number_2):
    return number_1 * number_2
    # print(f"\nThe multiplication of {number_1} and {number_2} is: {multiplication}\n")

def division(number_1, number_2):
    if number_2 == 0:
        # print("Any number divided by 0 is not defined.")
        return("Any number divided by 0 is not defined.")
    else:
        return number_1 / number_2
        # print(f"\nThe division of {number_1} and {number_2} is: {division}\n")