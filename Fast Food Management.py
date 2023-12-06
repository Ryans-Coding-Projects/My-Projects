import hashlib

users = {}

def login():
    while True:
        print("|-------------------|")
        print("| 1. Login          |")
        print("|-------------------|")
        print("| 2. Create Account |")
        print("|-------------------|")
        choice = input("\nPlease Login or Create an account to continue: ")

        if choice == "1":
            username = input("Enter Username: ")
            if username in users:
                password = input("Enter Password: ")
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if hashed_password == users[username]:
                    print(f"{username} Successfully Logged In")
                    return username
                else:
                    print("Invalid Password")
            else:
                print(f"User not found with the username {username}")

        elif choice == "2":
            created_username = input("\nEnter a new username: ")
            while created_username in users:
                print(f"Username {created_username} already exists. Please choose a different username.")
                created_username = input("\nEnter a new username: ")

            created_password = input("\nEnter a new Password: ")
            while len(created_password) < 6:
                print("Please Enter more than 6 digits")
                created_password = input("\nEnter a new Password: ")

            hashed_password = hashlib.sha256(created_password.encode()).hexdigest()
            users[created_username] = hashed_password
            print("\nAccount successfully created!")
            return created_username

        else:
            print("Invalid input. Please Login or Create an Account to continue.")


logged_in_username = login()
print("Welcome, ", logged_in_username)

employees = {}


def search_employees(search_name):
    if search_name in employees:
        print(f"Employee found: \nName: {search_name} \nPhone: {employees[search_name]}")
    else:
        print(f"No Employees found with the name {search_name}")


def add_employee():
    name = input("\nEnter employee name: ")
    phone = input("\nEnter employee phone number: ")
    employees[name.title()] = phone
    print(f"Employee {name} added successfully with phone number {phone}")


def remove_employee():
    name = input("Enter employee name to remove: ")
    if name in employees:
        del employees[name]
        print(f"\nEmployee {name} removed successfully")
    else:
        print(f"\nNo employee found with the name {name}")


def show_menu():
    print("|-----------------------|")
    print("|          MENU         |")
    print("|-----------------------|")
    print("| 1. Search Employee    |")
    print("| 2. Add Employee       |")
    print("| 3. Remove Employee    |")
    print("| 4. Place Order        |")
    print("| 5. View Order         |")
    print("| 6. Promote Restaurant |")
    print("| 7. Schedule Meeting   |")
    print("| 8. Mass Text          |")
    print("| 9. Exit               |")
    print("|-----------------------|")


# Functions for managing orders, promotions, meetings, and mass text can be added similarly


while True:
    show_menu()
    choice = input("\nEnter Selection: ")

    if choice == "1":
        search_name = input("\nEnter employee name to search: ")
        search_employees(search_name.title())

    elif choice == "2":
        add_employee()

    elif choice == "3":
        remove_employee()

    def place_order():
    order_item = input("Enter the item to order: ")
    order_amount = input("Enter the quantity: ")
    order = {"Item": order_item, "Quantity": order_amount}
    return order

def view_order(order):
    if order:
        print("Current Order:")
        print(f"Item: {order['Item']}")
        print(f"Quantity: {order['Quantity']}")
    else:
        print("No order placed yet.")

    elif choice == "4":
        order = place_order()

    elif choice == "5":
        view_order(order)

    elif choice == "6":
        promote()
        promote_choice = input("\nEnter Selection: ")
        if promote_choice == "1":
            print("\nLaunching Youtube Ad Campaign")
        elif promote_choice == "2":
            print("\nRequesting Billboard at nearest available location") 
        elif promote_choice == "3":
            outdoor_sign_choice = input("\nWould you like to change the outdoor sign?: ")
            if outdoor_sign_choice == "Yes":
                outdoor_message = input("\nWhat would you like the utdoor sign to say?: ")
                print(f"\nThe outdoor sign now reads: {outdoor_message}")
            else:
                print("\nThe outdoor sign will not be changed at this time")
                
        elif promote_choice == "4":
            print("\nReturning to Main Menu")
        else:
            print("\nInvalid Input")
        

    elif choice == "7":
        meeting_time = input("Meeting Time: ")
        meeting_place =input("Meeting Place: ")
        print("\nMeeting sending to all employee phone numbers")
        print("\nMeeting sucessfully sent!")
        print(f"\nMeeting succesfully scheduled for {meeting_time} at {meeting_place}")

    elif choice == "8":
        mass_text = input("Enter Message: ")
        print(f"Message sent to all employees, {mass_text}")

    elif choice == "9":
        print("\nSuccesfully Exited")
        break

    else:
        print("\nInvalid Input. Please enter a number between 1 and 9")

    


