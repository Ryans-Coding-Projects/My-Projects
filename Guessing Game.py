#This program prompts the user to try and guess my number.

import random

print("I'm thinking of a number between 1 and 100, try to guess my number!")

guess_count = 0

number = random.randint(1, 100)

while True:
    guess = int(input("\nEnter Guess: ",))
    guess_count += 1
        
    if guess == number:
        print("\nCorrect!", number, "is my number. It took you" , guess_count , "guesses!")
        break

    if guess > number:
        print("\nThat guess is too high! Try again!")
        guess_count + 1

    if guess < number:
        print("\nThat guess is too low! Try again!")
        guess_count + 1

    

        
