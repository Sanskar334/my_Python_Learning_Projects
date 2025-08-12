def table():
    while True:
        try:
            input = int(input("\nEnter a number to generate it's table: "))
            break
        except:
            print("\nYour input is not a valid number.\n")

    for i in range(1, 11):
        print(f"{input} X {i} = {input*i}")