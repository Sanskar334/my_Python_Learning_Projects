# from random import choice

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

class main_features():
    def create_post(self):
        post_content = input("\nEnter your post content.\n")
        with open("myposts.txt", "a") as file:
            file.write(f"post 1:\n\n{post_content}\n")

    def view_posts(self):
        try:
            with open("myposts.txt", "r") as file:
                posts = file.read()
                if posts:
                    print("\nYour posts:\n")
                    print(posts)
                else:
                    print("\nNo posts found.")
        except FileNotFoundError:
            print("\nNo posts found. Please create a post first.")

    def edit_post(self):
        identify_post = input("\nEnter the post number you want to edit (e.g., Post 1): ").lower()
        try:
            with open("myposts.txt", "r") as file:
                posts = file.readlines()
            
            for i, post in enumerate(posts):
                if identify_post in post:
                    new_content = input("\nEnter the new content for your post:\n")
                    if i + 2 < len(posts):
                        posts[i] = f"{identify_post}:\n\n{new_content}\n"
                        posts[i+1] = "\n"
                        posts[i+2] = "" 
                    else:
                        print("\nPost format seems incorrect.\n")
                        return
                    posts[i] = f"{identify_post}:\n\n{new_content}\n"
                    with open("myposts.txt", "w") as file:
                        file.writelines(posts)
                    print("\nPost updated successfully.\n")
                    break
            else:
                print("\nPost not found.\n")

        except FileNotFoundError:
            print("\nNo posts found. Please create a post first.\n")

    def delete_post(self):
        identify_post = input("\nEnter the post number you want to edit (e.g., Post 1): ").lower()
        try:
            with open("myposts.txt", "r") as file:
                posts = file.readlines()
            
            # post_found = False
            for i, post in enumerate(posts):
                if identify_post in post:
                    # post_found = True
                    print(f"\nDeleting {identify_post}...")
                    # del posts[i]
                    posts[i] = f"{identify_post}"
                    posts[i+1] = "\n"
                    posts[i+2] = ""
                    with open("myposts.txt", "w") as file:
                        file.writelines(posts)
                    print("\nPost deleted successfully.\n")
                    break
            else:
                print("\nPost not found.\n")

        except FileNotFoundError:
            print("\nNo posts found. Please create a post first.\n")

# write here if __name__ == "__main__": when doing modular programming so that this only runs in this file and copy this to main.py
if __name__ == "__main__":
    print("\nWelcome to the Social Media App!")
    auth = authentication()
    action = str(input("Write \"login\" or \"sign up\": ")).lower()
    auth.login_or_signup(action)
# ----------------------------------------------------------------------

# Main menu for the social media app
    while True:
        print('''1. Create a post
2. View posts\n3. Edit a post\n4. Delete a post''')
        choice = input("\nWhat would you like to do: ").lower()
        main = main_features()
        match choice:
            case "create" | "create a post" | "post" | "1":
                main.create_post()
            case "view" | "view post" | "view posts" | "2":
                main.view_posts()
            case "edit" | "edit a post" | "edit previous post" | "3":
                main.edit_post()
            case "delete" | "delete a post" | "remove" | "4":
                main.delete_post()
            case _:
                print("Invalid choice. Please try again.")
                break