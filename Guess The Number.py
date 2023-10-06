#Assign Number for The User to Try To Guess
my_number = 77

#Welcome Message
print("-------------------------------------------")
print("I am Thinking of a Number between 1 and 100,")
print("Try to Guess the Number I am thinking Of")
print("-------------------------------------------")

#Assign User's Guess to an integer
guess = int(input("Enter Your Guess: "))

print("-------------------------------------------")

#While Loop To Allow User To Continue Guessing Until The Guess My number
while guess != my_number:

#If Statement if User's guess Is Higher Than My Number    
    if guess > my_number:
        print("The Number You Guessed Is Too High")
        guess = int(input("Enter Your Guess Again: "))
        print("-------------------------------------------")
#Elif Statement if User's guess Is Lower Than My Number
    elif guess < my_number:
        print("The Number You Guessed Is Too Low")
        guess = int(input("Enter Your Guess Again: "))
        print("-------------------------------------------")
        
#Break the Loop when The User Guesses Correctly and Congratulate Them
    else:
        break
print("CORRECT! - You Guessed My Number Right")



