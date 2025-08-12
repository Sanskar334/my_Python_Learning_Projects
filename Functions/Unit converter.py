def cm_converter(a):
    m_to_cm = a*100
    return(f"{m_to_cm} cm") # return is used instead of print because print gives an output and returns give a value which can be used in program.

def feet_converter(a):
    f_to_cm = a*30.48
    return(f"{f_to_cm} cm")

def g_converter(a):
    g_to_kg = a/1000
    return(f"{g_to_kg} kg")

def inch_converter(a):
    inch_to_feet = a/12
    return(f"{inch_to_feet} feet")

for i in range(1, 6):

    # print("") # Can also use this to create a sperate line. In this case I have used end = "\n\n" in line 39.

    a = float(input("Enter the number without unit: "))
    unit = str(input("Enter the unit (m, inch, ft, g): ")).lower()

    if unit in ["m", "meter", "meters"]: # I can also use list like this no need to create a sperate one. I have broke each if elif else table in a seperate unit so that any one condition gets true.
        print(f"{a} meters is {cm_converter(a)}")

    elif unit in ["in", "inch", "inches"]:
        print(f"{a} inches is {inch_converter(a)}")

    elif unit in ["ft", "feet", "feets"]:
        print(f"{a} feets is {feet_converter(a)}")

    elif unit in ["g", "gram", "grams"]:
        print(f"{a} grams is {g_converter(a)}")

    else:
        print(f"\"{unit}\" is an unsupported unit")

    print(f"Chance used {i}/5", end = "\n\n") # \" is used to enter characters like "" in between print statements if \ not used for it then python will relate it with print's "" and will throw an error.
    i += 1

print("You have used all 5 chances, please restart")