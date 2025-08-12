def userinput():
        try:
        #     number = float(input("Enter the number you want to convert: "))
            float(input("Enter the number you want to convert: "))
        except:
            print("\nYour input is not a valid number.")

def miles_to_kilometres():
        userinput()
        convert = userinput() * 1.60934
        print(f"{userinput}miles is: {convert}km")

def metre_to_cm():
        userinput()
        convert = userinput() * 100
        print(f"{userinput}m is: {convert}cm")

def metre_to_inches():
    userinput()
    convert = userinput() * 393701
    print(f"{userinput}m is: {convert}inches")

def inches_to_feets():
    userinput()
    convert = userinput() / 12
    print(f"{userinput}inches is: {convert}feets")