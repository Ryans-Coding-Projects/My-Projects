#This program is used to store customer data

customers = {}

def search_customer(search_name):
    if search_name in customers:
        print(f"\nCustomer found: \nName: {search_name} \nPhone: {customers[search_name]}")
    else:
        print(f"\nNo customer found with the name {search_name}")

def add_customer(name, phone):
    customers[name.title()] = phone
    print(f"\nCustomer {name} added successfully with phone number {phone}")

def remove_customer(name):
    if name in customers:
        del customers[name]
        print(f"\nCustomer {name} removed successfully")
    else:
        print(f"\nNo customer found with the name {name}")

def show_menu():
    print("\n|--------------------|")
    print("|        MENU        |")
    print("|--------------------|")
    print("| 1. SEARCH CUSTOMER |")
    print("| 2. ADD CUSTOMER    |")
    print("| 3. REMOVE CUSTOMER |")
    print("| 0. EXIT            |")
    print("|--------------------|")

while True:
    show_menu()
    choice = input("\nEnter Selection: ")

    if choice == "1":
        search_name = input("\nEnter customer name to search: ")
        search_customer(search_name.title())
    elif choice == "2":
        name = input("\nEnter customer name: ")
        phone = input("\nEnter customer phone number: ")
        add_customer(name, phone)
    elif choice == "3":
        name = input("\nEnter customer name to remove: ")
        remove_customer(name.title())
    elif choice == "0":
        print("\nExiting.......")
        break
    else:
        print("\nInvalid input. Please enter a number between 0 and 3.")


