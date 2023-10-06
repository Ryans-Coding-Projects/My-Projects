#Import random 
import random

#Welcome message.
print("RANDOM PASSWORD GENERATOR")
print("-------------------------")

#Ask user how long they'd like their password to be.
length = int(input("How many characters would you like your password to be?: "))

#List characters that can be used.
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"

#Ask for user input to generate password
input("\nPress ENTER to generate a random password: ")

#Function to join a random combination of charcaters based upon length of password selected by user.
password = " ".join(random.sample(chars,length))

#Display results.    
print("\nYour new password is: ", password)
