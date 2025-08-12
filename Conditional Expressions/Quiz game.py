print ("Welcome to the GK quiz! Answer the following question")

score = 0

a1 = input("Question 1: Which planet is known as the Red Planet? \n")
if a1.replace(" ", "").lower() == "mars":
    score += 1

a2 = input("Question 2: What is the largest ocean in the world? \n")
if a2.replace(" ", "").lower() == "pacificocean":
    score += 1

a3 = input("Question 3: Who was the first Prime Minister of India? \n")
if a3.replace(" ", "").lower() == "jawaharlalnehru":
    score += 1

a4 = input("Question 4: What is the chemical symbol for Gold? \n")
if a4.replace(" ", "").lower() == "au":
    score += 1

print (f"You scored {score}/4")