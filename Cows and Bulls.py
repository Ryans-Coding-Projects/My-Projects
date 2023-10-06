#This program is used to play cows and bulls.
#Rules: Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”.
#For every digit the user guessed correctly in the wrong place is a “bull.”

#Import
import random

def cows_and_bulls(guess):
    #Generate a random 4-digit number
    target = str(random.randint(1000, 9999))
    guess = str(guess)

    #Initialize cows and bulls count
    cows = 0
    bulls = 0

    #Check for cows and bulls
    for i in range(len(target)):
        if target[i] == guess[i]:
            bulls += 1
        elif guess[i] in target:
            cows += 1

    return(cows, bulls)

while True:
    guess = input("Enter a 4-digit number: ")
    if len(guess) != 4:
        print("Invalid input. Please enter a 4-digit number.")
    else:
        result = cows_and_bulls(guess)
        print("Cows", result[0], "Bulls", result[1])
    


    
                        

    
