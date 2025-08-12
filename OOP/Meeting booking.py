class Meetings:

    def __init__(self, organiser_name, meeting_subject, duration, date, mode_of_meeting):
        self.organiser_name = organiser_name
        self.meeting_subject = meeting_subject
        self.duration = duration
        self.date = date
        self.mode_of_meeting = mode_of_meeting

    def __str__(self):
        return (f"\nDate: {self.date}\n"
                f"Organised by: {self.organiser_name}\n"
                f"Subject: {self.meeting_subject}\n"
                f"Duration: {self.duration}\n"
                f"Mode: {self.mode_of_meeting}\n")
        
class meeting_manager:
        
        def save_meeting(self, meeting):
            with open("scheduled meeting.txt", "a") as file:
                  file.write(str(meeting) + "\n")
        
        def book_meeting(self):

            organiser = input("\nOrganiser of this meeting: ")
            subject = input("Subject this meeting: ")
            date = input("Date of this meeting: ")
            duration = input("Duration of this meeting: ")
            mode = input("Medium of this meeting: ")

            meeting = Meetings(organiser, subject, duration, date, mode)

            self.save_meeting(meeting)

        def cancel_meeting(self):

                key_date = input("\nEnter the date of this meeting: ")

                with open("scheduled meeting.txt", "r") as file:
                    lines = file.readlines()

                with open("scheduled meeting.txt", "w") as file:
                    for line in lines:
                        if key_date in line:
                                # line = line.rstrip('\n')
                                file.write("\nIMPORTANT NOTE: This meeting got cancelled.")

                        # else:
                        #     print(f"No")

                print("\nYour meeting was successfully cancelled.")

        def reschedule_meeting(self):

                key_date = input("\nEnter the date of this meeting: ")
                new_date = input("\nEnter the new date for reschedule: ")

                with open("scheduled meeting.txt", "r") as file:
                    lines = file.readlines()

                with open("scheduled meeting.txt", "w") as file:
                    for line in lines:
                        if key_date in line:
                                # line = line.rstrip('\n')
                                file.write(f"\nIMPORTANT NOTE: This meeting got reschedule to {new_date}")

                        # else:
                        #     print(f"No such meeting with date {key_date} is scheduled.")

                print("\nYour meeting was successfully rescheduled.")

# HERE STARTS THE ACTUAL SCRIPT.

while True:
    def menu():
            print(f"\nHello, Manager")
            print(f'''\nWelcome to the Meeting booking menu\n
1. Book Meeting.\n2. Cancel Meeting. \n3. Reschedule Meeting''')
            print("\nNote: you can exit by typing \"Exit\".")

    choices = ["book meeting", "book", "cancel meeting", "cancel", "reshedule meeting", "reschedule"]

    menu()
    choice = input("\nWhat would you like to do?\n").lower()

    if choice in choices[0:2]:
        manager = meeting_manager()
        manager.book_meeting()

    elif choice in choices[2:4]:
        manager = meeting_manager()
        manager.cancel_meeting()

    elif choice in choices[4:6]:
        manager = meeting_manager()
        manager.reschedule_meeting()

    else:
        print("Invalid entry! Please enter a valid entry.")
        break