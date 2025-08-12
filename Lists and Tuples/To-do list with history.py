days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")

days_task = {              # I can use dictionary like a type of database.
    "monday": [],
    "tuesday": [],
    "wednesday": [],
    "thursday": [],
    "friday": [],
    "saturday": [],
    "sunday": []
}

# print(days)

# task_on_days = []

# Select_day = input("\nWhich day's task you want to create: ")

def input_tasks(selected_day):
    for items in range(1, 6):
        task = input(f"Task {items}: ")
        days_task[selected_day].append(task)

def create_histroy(Select_day):
    history = open(f"{Select_day}.txt", "w")
    history.write("\n".join(days_task[Select_day]))
    history.close()
        
def selection_of_day():

    while True:

        Select_day = input("\nWhich day's task you want to create: ").lower()

        if (Select_day in days):
            input_tasks(Select_day)

            create_histroy(Select_day)

            # history = open(f"{Select_day}.txt", "w")
            # history.write("\n".join(days_task[Select_day]))
            # history.close()
            
            break

        else:
            Select_day = input("Invalid day. Please enter a valid day: ").lower()
            if (Select_day in days):
                input_tasks(Select_day)

            else:
                print("Still invail :(")
                return

            break

    print(f"\n{Select_day} tasks are:")
    for i, task in enumerate(days_task[Select_day], 1):
        print(f"{i}. {task}")
    print("")

total_days = 1

while (total_days <= 7):

    selection_of_day()

    repeat = input("Do you want to add tasks to other days as well? - Yes/No: ").lower()

    if (repeat == "yes"):
        # selection_of_day()
        total_days += 1

    else:
        print("all tasks are assigned.\n")
        break

if (total_days > 7):
    print("all tasks are assigned for all days of the week.\n")