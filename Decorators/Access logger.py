import functools
import datetime

def log_access(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        result = func(*args, **kwargs)
        print(f"Accessed {func.__name__} at {current_time} is: {result}")
        return result
    return wrapper

class Arithematic_Calculations:
    @staticmethod
    @log_access
    def addition(a, b):
        return a + b
    
    @staticmethod
    @log_access
    def subtraction(a, b):
        return a - b
    
    @staticmethod
    @log_access
    def multiplication(a, b):
        return a * b
    
    @staticmethod
    @log_access
    def division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

calc = Arithematic_Calculations()
calc.addition(a, b)
calc.subtraction(a, b)
calc.multiplication(a, b)
calc.division(a, b)