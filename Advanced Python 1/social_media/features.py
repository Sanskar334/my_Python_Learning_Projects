class main_features():
    def create_post(self):
        post_content = input("\nEnter your post content.\n")
        with open("myposts.txt", "a") as file:
            file.write(f"post 1:\n\n{post_content}\n") # use loop here to increment post number or just use post i + 1, and use i = 0

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