#This program allows you to think of a number and the computer will try to guess it

import random

nums = list(range(1, 11))
    
guess_amount = 1

print("""Think of a number between 0 and 10
and I will try to guess it.\n""")

while True:
    guess=random.choice(nums)
    print("\nIs your number", guess, "?")
    
    user_input=input("\nEnter Yes if the computer got your number or no if not: ").lower()

    while user_input not in["yes", "no"]:
        print("\nInvalid response. Please enter 'yes' or 'no'.")
        user_input = input("\nEnter Yes if the computer got your number or no if not: ").lower()

    if user_input == "yes":
        print("\nI guessed your number in", guess_amount, "tries!")
        break

    elif user_input == "no":
        guess_amount += 1
        nums.remove(guess)
        print("\nI did not guess your number. Let me try again")
        

   
