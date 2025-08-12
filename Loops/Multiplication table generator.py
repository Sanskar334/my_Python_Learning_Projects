chance = 0

while(chance<4):

    a = int(input("Enter the number whose table you want: "))

    table = 1

    while(table<11):
        print(f"{a}X{table}={a*table}")
        table += 1

    chance += 1
    print(f"Chances used: {chance}/4")

print("You have used all 4 chances")

# BASIC

# a = int(input("Enter the number whose table you want: "))

# for table in range(11):
#     print(a*table)

# FOR LOOP

# a = int(input("Enter the number whose table you want: "))

# for table in range(1, 11):
#     print(f"{a}X{table}={a*table}")

# WHILE LOOP

# a = int(input("Enter the number whose table you want: "))
# table = 1

# while(table<11):
#     print(f"{a}X{table}={a*table}")
#     table += 1