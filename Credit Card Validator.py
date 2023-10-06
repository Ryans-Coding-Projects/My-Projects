#This program prompts the user to enter a debit/credit card number and returns whether or not its valid

cc = input("Enter Card Number(no spaces): ")

if len(cc) == 16 and cc[0] == "5":
    print(f"{cc} is a valid Mastercard Number")

elif len(cc) == 16 and cc[0] == "4":
    print(f"{cc} is a Valid Visa Card Number")

elif len(cc) == 16 and cc[0] == "6":
    print(f"{cc} is a Valid Discover Card Number")

elif len(cc) == 15 and cc[0] == "3":
    print(f"{cc} is a Valid American Express Card Number")

else:
    print(f"{cc} is not a valid credit/debit card number")
    
