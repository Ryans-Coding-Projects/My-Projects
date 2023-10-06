#Hangman game
#Create a list of words to be used in the game.

words = ["python", "programming", "computer", "science"]

#Choose a random word from the list for the player to guess
import random
word = random.choice(words)

#Create a variable to store the number of users lives
lives = 6

#Create a variable to store the letter that the user has already guessed
guessed_letters = []

#Create a variablle to store the letter the user has not guessed yet
display_word = ""
for letter in word:
    if letter in guessed_letters:
        display_word += letter
    else:
        display_word += "_"

#Use the while loop to keep the game running as long as the player has lives
while lives > 0 and "_" in display_word:
    guess = input("Guess a letter: ")


#Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)

#Check if the letter is in the word
    if guess in word:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print("Correct! The word is now:", display_word)
    else:
        lives -= 1
        print("Incorrect. You have", lives, "lives left.")

#Check if the player has won or lost
if "_" not in display_word:
    print("You win! The word was", word + ".")
else:
    print("You lose! The word was", word + ".")
