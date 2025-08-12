# TRIANGLE * PATTERN

chance = 0

while (chance<4):
    row = int(input("Enter the number of rows you want: "))

    print("\nBelow is the triangle pattern\n")

    for i in range(1, row+1):
        print(" " * (row-i), end ="") # supposed user enter row as 5 so I used i cause its value will increase and spaces will decrease so that * will be printed in center.
        print("*" * (2*i-1)) # 2*i-1 is used to get an odd number, end = "" removes the new line.
        # print("") # this is printed so that the next row comes in new line.

    # DIAMOND * PATTERN

    print("\nBelow is the diamond pattern\n")

    # row = int(input("Enter the number of rows you want: "))

    for i in range(1, row+1):
        print(" " * (row-i), end ="")
        print("*" * (2*i-1))

    for i in range(row-1, 0, -1): # row-1 is used so the 5th row (last of triangle up and first of triangle down) doesn't repeat. -1 indicate step means go backward by 1 each time.
        print(" " * (row-i), end ="") # supposed user enter row as 5 so I used i cause its value will increase and spaces will decrease so that * will be printed in center.
        print("*" * (2*i-1)) # 2*i-1 is used to get an odd number, end = "" removes the new line.

    chance += 1
    print(f"Chance used {chance}/4")

print("You have used all 4 chances")

'''
print("") # this is printed so that the next row comes in new line
no need for this anymore because I removed end = "" in the last line
'''