#This program can be used to see how many days for hours or hours for days

while True:
    print("\n1. For hours to days")
    print("2. For days to hours")

    choice = int(input("\nEnter choice: "))

    if choice == 1:
        hours = int(input("\nEnter hours: "))
        hours_to_days = hours / 24
        print(hours, "hours equals", int(hours_to_days), "days")

    elif choice == 2:
        days = int(input("\nEnter days: "))
        days_to_hours = days * 24
        print(days, "days equals",days_to_hours, "hours")

    elif choice == 3:
        print("\nSuccesfully Exited")
        break

    else:
        print("\nInvalid input. Please enter number 1, 2, or 3.")
