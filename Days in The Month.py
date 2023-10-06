#This program allows the user to enter a month and displays the amount of days in that month

while True:
    choice = input("\nEnter Month(or leave blank to exit): ").lower()

    if choice == "january":
        print("\nThere are 31 days in January.")

    elif choice == "february":
        print("\nThere are 28 days in February.")

    elif choice == "march":
        print("\nThere are 31 days in March.")

    elif choice == "april":
        print("\nThere are 30 days in April.")

    elif choice == "may":
        print("\nThere are 31 days in May.")

    elif choice == "june":
        print("\nThere are 30 days in June.")

    elif choice == "july":
        print("\nThere are 31 days in July.")

    elif choice == "august":
        print("\nThere are 31 days in August.")

    elif choice == "september":
        print("\nThere are 30 days in September.")

    elif choice == "october":
        print("\nThere are 31 days in October.")

    elif choice == "november":
        print("\nThere are 30 days in November.")

    elif choice == "december":
        print("\nThere are 31 days in December.")

    elif choice == "":
        break

    else:
        print(f"\n{choice} is not a valid month.")
