import json
import os

user_data_file = 'user_accounts.json'

#Function to load the user data from json file:
def read_users():
    if os.path.exists(user_data_file):
        with open(user_data_file, 'r') as file:
            return json.load(file)
    else:
        return {}

def sign_upwith_an_email(email):
    return "@" in email and "." in email

def create_password(password):
    return len(password) >= 8

def signup_user():
    print("Create a Foodieyumz Account!")
    
    users = read_users()
    username = input("Username: ")
    
    if username in users:
        print("Username already exists. Please try another one.")
        return None
    
    while True:
        email = input("Email: ")
        if sign_upwith_an_email(email):
            break
        else:
            print("Invalid email format. Please try again.")
    
    while True:
        password = input("Password: ")
        if create_password(password):
            break
        else:
            print("Password must be at least 8 characters long. Please try again.")
    
    user_data = {
        "email": email,
        "password": password
    }
    
    users[username] = user_data
    save_users(users)
    
    print("\nSuccessfully Created An Account!")
    print(f"Welcome, {username}!")
    return username

def save_users(users):
    with open(user_data_file, 'w') as file:
        json.dump(users, file)

def delete_user():
    users = read_users()
    username = input("Enter the username you want to delete: ")
    
    if username in users:
        confirm = input(f"Are you sure you want to delete the user '{username}'? This action cannot be undone. (y/n): ")
        if confirm.lower() == 'y':
            del users[username]
            save_users(users)
            print(f"User '{username}' has been deleted.")
        elif confirm.lower() == 'n':
            print("Deletion cancelled.")
        else:
            print("Invalid action. Please try again.")
    else:
        print("Username not found.")

def login_user():
    users = read_users()
    username = input("Enter your Username: ")
    
    if username not in users:
        print("Username not found. Please sign up first.")
        return None
    
    password = input("Enter your password: ")
    
    if users[username]["password"] == password:
        print(f"Login successful! Welcome back, {username}!")
        return username
    else:
        print("Incorrect password. Please try again.")
        return None

def logout_user():
    print("You have been logged out.")

def change_password(current_user):
    users = read_users()
    
    if current_user is None:
        print("You need to be logged in to change your password.")
        return
    
    old_password = input("Enter your current password: ")
    
    if users[current_user]["password"] == old_password:
        while True:
            new_password = input("Enter your new password: ")
            if create_password(new_password):
                users[current_user]["password"] = new_password
                save_users(users)
                print("Password successfully changed!")
                break
            else:
                print("Password must be at least 8 characters long. Please try again.")
    else:
        print("Incorrect password. Please try again.")
        return None

def main():
    current_user = None
    
    while True:
        print("\n--- Menu ---")
        print("1. Create an Account")
        print("2. Login")
        print("3. Logout")
        print("4. Delete User")
        print("5. Change Password")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            if current_user:
                print("You are already logged in. Please log out first.")
            else:
                current_user = signup_user()
        elif choice == '2':
            if current_user:
                print("You are already logged in.")
            else:
                current_user = login_user()
        elif choice == '3':
            if current_user:
                logout_user()
                current_user = None
            else:
                print("You are not logged in.")
        elif choice == '4':
            if current_user:
                print("You cannot delete an account while logged in. Please log out first.")
            else:
                delete_user()
        elif choice == '5':
            if current_user:
                change_password(current_user)
            else:
                print("You need to log in to change your password.")
        elif choice == '6':
            print("See you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
