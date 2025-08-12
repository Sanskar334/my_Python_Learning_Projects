from datetime import datetime
import os

now = datetime.now()
# print(now.time())
date_time = (f"{now.strftime("%d/%m/%y")}\n{now.strftime("%I:%M %p")}")

# menu_content = ["create new journal entry.", "edit existing journal entry.", "delete a journal entry."]

while True:

    print('''\nWelcome to the journal entry menu.
1. Create New Journal Entry.
2. Edit Existing Journal Entry.
3. Delete a Journal Entry.\n\n
Note: You can exit by typing "Nothing"\n''')

    menu = input("What would you like to do?\n").lower()

    if menu in ["create new journal entry", "new journal entry", "create new", "create"]:

        entry = input("\nHow would you like to remember this day?\n")

        with open(f"{now.date()}.txt", "w") as journal_entry:

            journal_entry.write(f"{date_time}\n")
            journal_entry.write(f"\n{entry}")

        # journal_entry.close()

    elif menu in ["edit existing journal entry", "edit journal entry", "edit entry", "edit"]:

        entry_name = input("\nWhich day's entry you want to edit? Write only file name without extension)\n")

        with open(f"{entry_name}.txt", "a") as journal_entry:

            edit_entry = input(f"\nWhat would you like to edit in the entry of {entry_name}?\n")
            journal_entry.write(f"\n{edit_entry}")

            print("Entry successfully edited\n")

            # journal_entry.write(f"\n{entry}")

    elif menu in ["delete", "delete journal entry", "remove entry", "remove"]:

        entry_name = input("\nWhich day's entry you want to delete? Write file name with extension\n")

        if os.path.exists(entry_name):
            confirm = input(f"Are you sure you want to delete the entry of {entry_name}, you cannot undo this action.\nEnter the entry file name again to confirm: ")

            if confirm == entry_name:
                os.remove(entry_name)
                print(f"{entry_name} has been deleted")

            else:
                print(f"{confirm} doesn't match with {entry_name}\nTherefore the file has not been deleted")

        else:
            print(f"No such entry of {entry_name} was found.\nPlease re-check the name")

    elif menu in ["Nothing", "nothing", "done", "over"]:

        break

    else:
        print("Invalid choice.")