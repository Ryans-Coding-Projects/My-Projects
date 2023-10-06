print("Welcome to American Banking")

print(" ")

username=input("Enter Your Username: ")

pin=int(input("Enter Your 4-Digit PIN Number: "))

while pin > 9999 or len(pin) != 4:
        print("Invalid Pin Number. Try Again")
        pin = input("Enter Your 4-Digit PIN Number: ")
        
              
print("-----------------------------------")

print(" ")

print("Hello," , username,)

print(" ")

balance = 0
    
while True:

    print("MENU")

    print("-----------------------------------")

    print("ENTER 1: To Display Account Balance")

    print("ENTER 2: To Make a Withdrawl")

    print("ENTER 3: To Make a Cash Deposit")

    print("ENTER 4: To Change Account Pin")

    print("ENTER 5: To Exit")

    print("-----------------------------------")

    choice = int(input("What Would You Like To Do?: "))

    print(" ")

    if choice == 1:
     
        print("Your Account Balance is: $" , balance)

        print("-----------------------------------")

        print(" ")

        print("Returning To Main Menu")

        print(" ")
    
    elif choice == 2:

        withdraw = int(input("How Much Would You Like To Withdraw?: "))

        print(" ")

        if withdraw < balance:
            
            print("Succesfully Withdrew: $" , withdraw)

            print(" ")

            print("Returning To Main Menu")

            print(" ")

            balance = balance-withdraw

        else:
            print("You Do Not Have Enough Money In Your Account")

            print("-----------------------------------")

            print(" ")

            print("Returning To Main Menu")

            print(" ")

    elif choice == 3:
        
        deposit = int(input("How much would you like to deposit?: "))

        print(" ")
        
        print("Succesfully Deposited: $" , deposit)

        print("-----------------------------------")

        print(" ")

        print("Returning To Main Menu")

        print(" ")

        balance = balance+deposit

    elif choice == 4:
         pin = input("Enter Your New Account Pin: ")
         print("Your New Pin Is: " , pin)

         print("-----------------------------------")

         print(" ")

         print("Returning To Main Menu")

         print(" ")

    else:
        if choice == 5:
            print("-----------------------------------")
            print("Thank You For Banking With American Banks")
            print("We Hope to See You Again, " , username)
            break

    
    
