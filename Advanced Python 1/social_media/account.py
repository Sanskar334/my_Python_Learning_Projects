class authentication:
    def login(self):
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")

        # Check if the credentials are correct.
        with open("credentials.txt", "r") as file:
            credentials = file.readlines()

        for line in credentials:
            saved_username, saved_password = line.strip().split(", ")
            saved_username = saved_username.replace("Username: ", "")
            saved_password = saved_password.replace("Password: ", "")

            match (saved_username, saved_password):
                case (u, p) if u == username and p == password:
                    print(f"\nLogin successful!")
                    break
                case (u, p) if u == username:
                    print(f"\nIncorrect password for {username}. Please try again.")
                    return self.login()
                case (u, p) if p == password:
                    print(f"\nIncorrect username. Please try again.")
                    return self.login()
                case _:
                    print(f"\nNo account found with username {username}. Please sign up.")
                    return self.signup()

        print(f"\nWelcome back, {username}!")
        # return username, password

    def signup(self):
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        print(f"Account created successfully for {username}!")
        with open("credentials.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        # return username, password

    def login_or_signup(self, action):
        match action:
            case "login":
                return self.login()
            case "sign up":
                return self.signup()
            case _:
                print("Invalid action. Please try again.")