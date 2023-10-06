print("---------------------------")
print("        Calculator         ")
print("---------------------------")

print("Enter 1: For Addition")              
print("Enter 2: For Subtraction")
print("Enter 3: For Multiplication")
print("Enter 4: For Division")

print("---------------------------")

try:
    choice = int(input("Enter Your Choice: "))
    if choice not in (1, 2, 3, 4):
        raise ValueError
except ValueError:
    print("Invalid choice. Please enter a number between 1 and 4.")
else:
    print("---------------------------")
    if choice == 1:
        print("You've Selected Addition")
        print("---------------------------")
        print(" ")
        try:
            number_1 = int(input("Enter the First Number: "))
            number_2 = int(input("Enter the Second Number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            answer = number_1 + number_2
            print(" ")
            print(number_1, "+", number_2, "=", answer)
    elif choice == 2:
        print("You've Selected Subtraction")
        print("---------------------------")
        print(" ")
        try:
            number_1 = int(input("Enter the First Number: "))
            number_2 = int(input("Enter the Second Number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            answer = number_1 - number_2
            print(" ")
            print(number_1, "-", number_2, "=", answer)
    elif choice == 3:
        print("You've Selected Multiplication")
        print("---------------------------")
        print(" ")
        try:
            number_1 = int(input("Enter the First Number: "))
            number_2 = int(input("Enter the Second Number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        else:
            answer = number_1 * number_2
            print(" ")
            print(number_1, "*", number_2, "=", answer)
    elif choice == 4:
        print("You've Selected Division")
        print("---------------------------")
        print(" ")
        try:
            number_1 = int(input("Enter the First Number: "))
            number_2 = int(input("Enter the Second Number: "))
            if number_2 == 0:
                raise ZeroDivisionError
        except ValueError:
            print("Invalid input. Please enter a number.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        else:
            answer = number_1 / number_2
            print(" ")
            print(number_1, "/", number_2, "=", answer)
