#import random to receive a random response each time 
import random

#User input for question to be asked
input("Ask the Magic 8 Ball a Question: ")

#All responses the Magic 8 Ball can give the user
responses = [

    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
    ]

#Display Magic 8 Ball's Answer
print(random.choice(responses))

        
