#This program takes user input and determiones whether or not it is a palindrone.
#A palindrone is a word that reads the same forwards andf backwards 

a = input("Enter phrase: ")

b = a[::-1]

if a == b:
    print(f"{a} is a Palindrone")

else:
    print(f"{a} is Not a Palindrone")
