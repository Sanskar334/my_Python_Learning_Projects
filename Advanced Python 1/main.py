from social_media import account
from social_media import features
if __name__ == "__main__":
    print("\nWelcome to the Social Media App!")
    auth = account.authentication()
    action = str(input("Write \"login\" or \"sign up\": ")).lower()
    auth.login_or_signup(action)
# ----------------------------------------------------------------------

# Main menu for the social media app
    while True:
        print('''1. Create a post
2. View posts\n3. Edit a post\n4. Delete a post''')
        choice = input("\nWhat would you like to do: ").lower()
        main = features.main_features()
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