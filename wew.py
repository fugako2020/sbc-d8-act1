registered_users = {}  

def register():
    with open("username-password.txt", "w") as file:
        new_username = input("Choose a new username: ")
        new_password = input("Choose a password: ")
        registered_users[new_username] = new_password  
        file.write(f"{new_username}:{new_password}\n")
        print(f"User '{new_username}' registered successfully.")

def login():
    with open("username-password.txt", "r") as file:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in registered_users and registered_users[username] == password:
            print("Successfully logged in.")
        else:
            print("Login failed. Please try again.")

while True:
    choice = input("Enter 'l' to login or 'r' to register: ")

    if choice == 'r':
        register()
    
    elif choice == 'l':
        login()
    
    else:
        print("Invalid choice. Please enter 'l' or 'r'.")

    continue_choice = input("Do you want to continue? (yes/no): ").lower()
    if continue_choice != 'yes':
        break


