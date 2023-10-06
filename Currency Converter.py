#This program is used to convert us dollar to other currencies

def convert_to():
    print("\n|--------------------------|")
    print("| 1. U.S. Dollar           |")
    print("| 2. Euro                  |")
    print("| 3. Japanese Yen          |")
    print("| 4. Great British Pound   |")
    print("| 5. Austrailian Dollar    |")
    print("| 6. Canadian Dollar       |")
    print("| 0. Exit                  |")
    print("|--------------------------|")

while True:
    convert_to()

    amount = int(input("\nEnter U.S Dollar amount to convert: "))

    con_to = input("\nWhat would you like to convert to?: ")

    euro = amount * 0.93

    yen = amount * 131.42

    gbp = amount * 0.83

    aus = amount * 1.45

    can = amount * 1.34

    if con_to == "1":
        print(f"\n{amount} U.S. Dollars is ${amount} U.S. Dollars.")

    elif con_to == "2":
        print(f"\n{amount} U.S. Dollars is {euro} Euro's.")

    elif con_to == "3":
        print(f"\n{amount} U.S. Dollars is {yen} Japanese Yen.")

    elif con_to == "4":
        print(f"\n{amount} U.S. Dollars is {gbp} Great British Pounds.")

    elif con_to == "5":
        print(f"\n{amount} U.S. Dollars is {aus} Austrailian Dollars.")

    elif con_to == "6":
        print(f"\n{amount} U.S. Dollars is {can} Canadian Dollars.")

    elif choice == "0":
        print("Exited")
        break

    else:
        print("\nInvalid input. Please enter a number between 1 and 6.")
    
