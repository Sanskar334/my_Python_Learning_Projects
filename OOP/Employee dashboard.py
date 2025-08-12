class employee:

    def __init__(self, experience, name, skills, salary, location):
        self.experience = experience
        self.name = name
        self.skills = skills
        self.salary = salary
        self.location = location

    def __str__(self):
        return (f'''\nexperience: {self.experience}
name: {self.name}\nskills: {self.skills}\nsalary: {self.salary}\nlocation: {self.location}\n''')
    
class manage():

    def save_employee(self, details):
        with open("all employees.txt", "a") as file:
            file.write(f"{details}\n")


    def add_emloyee(self):
        self.experience = float(input("\nExperience of this employee (in number): "))
        self.name = input("Name of this employee: ")
        self.skills = input("Skills of this employee: ")
        self.salary = input("Salary of this employee: ")
        self.location = input("Location of this employee: ")

        details = employee(self.experience, self.name, self.skills, self.salary, self.location)

        self.save_employee(details)

    def edit_employeee_details(self):
        # details = ["experience", "name", "skills", "salary", "location"]
        self.identify = input("\nWhose details you want to edit: ")
        self.edit_details = input(f"What do you want to edit in {self.identify}'s details: ")
        self.edit = input(f"\nEnter {self.identify}'s new {self.edit_details}: ")

        self.target = self.edit_details

        with open("all employees.txt", "r") as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            # if self.target in line:
            if line.startswith(f"{self.edit_details}:"):
                lines[i] = (f"{self.edit_details}: {self.edit}\n")
                # file.write(f"{edit_details}: {edit}")

        with open("all employees.txt", "w") as file:
            file.writelines(lines)

        print(f"{self.identify}'s details edited successfully.")

    def delete_employee(self):
        self.identify = input("\nWhose details you want to delete: ")

        with open("all employees.txt", "r") as file:
            lines = file.readlines()

        with open("all employees.txt", "w") as file:
            for line in lines:
                if self.identify in line:
                    # file.write("\nIMPORTANT NOTE: Details of this employees was deleted.")
                    file.write("")

            print(f"{self.identify}'s details deleted successfully.")

    def current_employees(self):
        with open("all employees.txt", "r") as file:
            # lines = file.readlines()
            print(file.read())

        # print(lines)

    def menu():
            print(f"\nHello, Manager")
            print(f'''\nWelcome to employee dashboard\n
    1. See Current Employees Details.\n2. Add New Employee Details. \n3. Edit Employee Details. \n4. Delete Employee Details.''')
            print("\nNote: you can exit by typing \"Exit\".")

choices = ["add employee", "add", "edit employee details", "edit employee", "edit", "delete employee details", "delete employee", "delete", "see current employee", "current employee", "current"]

while True:
    manager = manage()
    manager.menu()
    choice = input("\nWhat would you like to do?\n").lower()

    if choice in choices[0:2]:
        manager.add_emloyee()

    elif choice in choices[2:5]:
        # manager = manage()
        manager.edit_employeee_details()

    elif choice in choices[5:8]:
        # manager = manage()
        manager.delete_employee()

    elif choice in choices[8:11]:
        # manager = manage()
        manager.current_employees()

    else:
        print("Invalid entry! Please enter a valid entry.")
        break