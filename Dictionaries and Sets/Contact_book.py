contacts = {
    "sanskar": ["(+91) 0123456789"],
    "jacob": ["(+1) 9820567810"],
    "charles": ["(+1) 4728450681"],
    "rohan": ["(+91) 4200065820"],
    "william": ["(+44) 8265710268"],
}

while True:

    contact_searching = input("\nWhose phone number are you searching for?\n").lower()

    if (contact_searching in contacts):
        print(contacts[contact_searching])

    elif (contact_searching != contacts):
        add_new_contact = input("\nContact not found. Do you want to add it as a new contact? - Yes/No: ").lower()

        if (add_new_contact == "yes"):
            name = input("Enter the name: ").lower()
            number = input("Enter the number: ").lower()

        else:
            print("\nRestart to find or add new contacts.")
            break

        contacts.update({name: [number]})
        print("\nContact added successfully.")

        print(contacts)