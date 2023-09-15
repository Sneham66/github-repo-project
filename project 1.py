class User:
    def __init__(self, username):
        self.username = username
        self.groups = []

class Group:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.files = []

class AdminInterface:
    def __init__(self):
        self.users = []
        self.groups = []

    def add_user(self):
        username = input("Enter the username of the new user: ")
        new_user = User(username)
        self.users.append(new_user)
        print(f"User '{username}' added successfully.")

    def create_group(self):
        group_name = input("Enter the name of the new group: ")
        new_group = Group(group_name)
        self.groups.append(new_group)
        print(f"Group '{group_name}' created successfully.")

    def add_user_to_group(self):
        if not self.users or not self.groups:
            print("No users or groups available.")
            return

        print("Select a group:")
        for index, group in enumerate(self.groups):
            print(f"{index + 1}. {group.name}")

        group_choice = int(input()) - 1
        selected_group = self.groups[group_choice]

        print("Enter usernames of users to add to the group (comma-separated):")
        usernames_input = input()
        usernames = [username.strip() for username in usernames_input.split(",")]

        for username in usernames:
            user = next((user for user in self.users if user.username == username), None)
            if user:
                if user not in selected_group.members:
                    selected_group.members.append(user)
                    user.groups.append(selected_group)
                    print(f"User '{user.username}' added to group '{selected_group.name}' successfully.")
                else:
                    print(f"User '{user.username}' is already in the group '{selected_group.name}'.")
            else:
                print(f"User '{username}' not found.")

    def delete_user(self):
        if not self.users:
            print("No users available.")
            return

        print("Select a user to delete:")
        for index, user in enumerate(self.users):
            print(f"{index + 1}. {user.username}")

        user_choice = int(input()) - 1
        deleted_user = self.users.pop(user_choice)

        for group in deleted_user.groups:
            group.members.remove(deleted_user)
        deleted_user.groups = []

        print(f"User '{deleted_user.username}' deleted successfully.")

    def run(self):
        while True:
            print("\nAdmin Interface Menu:")
            print("1. Add new user")
            print("2. Create new group")
            print("3. Add user to group")
            print("4. Delete user")
            print("5. Show groups")
            print("6. Upload file to group")
            print("7. Show files in group")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.create_group()
            elif choice == "3":
                self.add_user_to_group()
            elif choice == "4":
                self.delete_user()
            elif choice == "5":
                self.show_groups()
            elif choice == "6":
                self.upload_file_to_group()
            elif choice == "7":
                self.show_files_in_group()
            elif choice == "8":
                print("Exiting the admin interface.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def show_groups(self):
        if not self.groups:
            print("No groups available.")
            return

        print("Groups:")
        for index, group in enumerate(self.groups):
            print(f"{index + 1}. {group.name}")

    def upload_file_to_group(self):
        if not self.groups:
            print("No groups available.")
            return

        print("Select a group to upload the file:")
        for index, group in enumerate(self.groups):
            print(f"{index + 1}. {group.name}")

        group_choice = int(input()) - 1
        selected_group = self.groups[group_choice]

        if not selected_group.members:
            print("No members in the selected group to upload the file.")
            return

        print("Select a user to upload the file:")
        for index, user in enumerate(selected_group.members):
            print(f"{index + 1}. {user.username}")

        user_choice = int(input()) - 1
        selected_user = selected_group.members[user_choice]

        file_name = input("Enter the name of the file to upload: ")
        selected_group.files.append(file_name)

        print(f"File '{file_name}' uploaded to group '{selected_group.name}' by user '{selected_user.username}'.")

    def show_files_in_group(self):
        if not self.groups:
            print("No groups available.")
            return

        print("Select a group to show files:")
        for index, group in enumerate(self.groups):
            print(f"{index + 1}. {group.name}")

        group_choice = int(input()) - 1
        selected_group = self.groups[group_choice]

        if not selected_group.files:
            print(f"No files available in group '{selected_group.name}'.")
        else:
            print(f"Files in group '{selected_group.name}':")
            for file_name in selected_group.files:
                print(file_name)

if __name__ == "__main__":
    admin_interface = AdminInterface()
    admin_interface.run()
