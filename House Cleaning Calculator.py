ROOM_COST = 50
WINDOW_COST = 10
estimate = 0

def display_menu():
    print("\n|-------------------------|")
    print("|           MENU          |")
    print("|-------------------------|")
    print("| 1. Start Estimate       |")
    print("| 2. View Estimate        |")
    print("| 3. Schedule Services    |")
    print("| 4. View Services        |")
    print("| 5. View Pricing         |")
    print("| 6. Exit                 |")
    print("|-------------------------|")

def get_estimate():
    rooms = int(input("\nHow many rooms need cleaned?: "))
    room_total = (ROOM_COST * rooms)
    windows = int(input("How many windows need cleaned?: "))
    window_total = (WINDOW_COST * windows)
    return window_total + room_total

def view_services():
    print("\nOur Services Include:")
    print("- Room Cleaning")
    print("- Window Cleaning")

def view_pricing():
    print("\nRoom Cleaning: ", ROOM_COST, "dollars per room.")
    print("Window Cleaning: ", WINDOW_COST, "dollars per window.")

while True:
    display_menu()
    choice = input("\nEnter Selection: ")

    if choice == "1":
        estimate = get_estimate()
        print("\nThe estimated cost to clean your home is", estimate, "dollars.")

    elif choice == "2":
        if estimate == 0:
            print("\nYou Have Not Completed An Estimate")
        else:
            print("\nThe estimated cost to clean your home is", estimate, "dollars.")

    elif choice == "3":
        print("\nTo Schedule a Cleaning, Please Call (234)-817-7027")

    elif choice == "4":
        view_services()

    elif choice == "5":
        view_pricing()

    elif choice == "6":
        print("\nThank You For Your Time!")
        break

    else:
        print("\nInvalid Input. Please Enter A Number Between 1 and 6.")


