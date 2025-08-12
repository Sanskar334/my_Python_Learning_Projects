print ("Welcome to BMI calculator")

a = int(input("Enter your weight (in kg): "))
b = float(input("Enter your height (in meter): "))

square = b**2

BMI = a/square

print ("Your BMI is:", BMI)

# BMI = float(input("Enter your BMI: ")) # This was used for testing the if-else statements below

if BMI < 18.5:
    print ("You are underweight")
elif 18.5 <= BMI <= 23.9:
    print ("You weight is normal")
elif 24 <= BMI <= 29.9:
    print ("You are overweight")
else:
    print ("You are obese")