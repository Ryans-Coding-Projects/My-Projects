import random

#Welcome Message
print("Welcome to the Coin Flipping Simulator!")
print("--------------------------------------")

#Prompt for User Input
num_flips = int(input("Enter the number of time you want to flip the coin: "))
input("Press ENTER to flip a coin: \n\n")


#Function for Displaying either Heads or Tails
def cointoss():
    return random.choice([ "Heads" , "Tails" ])

#Initialize count for heads and tails
heads_count = 0
tails_count = 0

#Loop to flip the coin multiple times
for i in range(num_flips):
    print("Flip", i+1, ":", cointoss())
    if cointoss() == "Heads":
        heads_count += 1
    else:
        tails_count += 1

#Display Results
print("\nNumber of Heads: ", heads_count)
print("Number of Tails: "
      , tails_count)



