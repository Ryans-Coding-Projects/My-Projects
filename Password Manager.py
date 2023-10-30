#This Program is used to store and manage users password

passwords = {}

while True:
    print("\n1. View a Password")
    print("2. Enter a New Password")
    print("3. Delete a Password")
    print("4. Exit")
    
    choice = input("\nEnter Choice: ")

    if choice == "1":
        name = input("\nEnter name of password to view: ")
        if name in passwords:
            print(f"\nPassword for {name}: {passwords[name]})")
        else:
            print(f"\nPassword for {name} not found.")
        

    elif choice == "2":
        name = input("\nEnter name of password to create: ")
        password = input("\nEnter the password: ")
        passwords[name] = password
        print(f"\nPassword for {name} created")

    elif choice == "3":
        name = input("\nEnter name of password to delete: ")
        if name in passwords:
            del passwords[name]
            print(f"\nPassword for {name} deleted.")
        else:
            print(f"\nPassword for {name} not found.")

    elif choice == "4":
        print("\nSuccefully Exited")
        break

    else:
        print("\nInvalid Input. Please Enter a number between 1 and 4.")
