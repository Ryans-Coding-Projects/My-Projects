#This program can be used to find the perimeter or area of a square


while True:
    print("\n1. Area")
    print("2. Perimeter")
    print("3. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        length = int(input("Enter length of a side: "))
        area = length ** 2
        print(area)

    elif choice == 2:
        length = int(input("Enter length of a side: "))
        perm = length * 4
        print(perm)      

    elif choice == 3:
        ("\nSuccesfully Exited")
        break

    else:
        print("\nInvalid input. Please enter a number between 1 and 3.")

