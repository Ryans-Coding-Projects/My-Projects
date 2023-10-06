def sys_login():
    users = {}
    while True:
        print("|-------------------|")
        print("| 1. Login          |")
        print("|-------------------|")
        print("| 2. Create Account |")
        print("|-------------------|")
        choice=input("Please Login or Create an account to continue: ")
        
        if choice == "1":
            username = input("Enter Username: ")
            if username in users:
                password = input("Enter Password: ")
                if password == users[username]:
                    print(f"{username} Succesfully Logged In")
                    break
                else:
                    print("Invalid Password")
                    print("\nReturning to login screen.....")
            else:
                print(f"User not found with the username {username}")
    
        elif choice == "2":
            created_username = input("\nEnter a new username: ")
            while created_username in users:
                print(f"Username {created_username} already exists. Please choose a different username.")
                created_username = input("\nEnter a new username: ")
            print("Username succesfully created!")
            created_password = input("\nEnter a new Password: ")
            while len(created_password) < 6:
                print("Please Enter more than 6 digits")
                created_password = input("\nEnter a new Password: ")
                print("Password succesfully created!")
                print("\nAccount succesfully created!")
                users[created_username] = created_password
                print("\nReturning to login screen.....")
                break
        else:
            print("Invalid input. Please Login or Create an Account to continue.")
    

sys_login()





    
