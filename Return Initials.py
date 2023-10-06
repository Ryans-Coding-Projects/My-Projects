#This program returns the first letter of a persons first and last names

name = input("Enter a First and Last name: ")

print(str(name.split(" ")[0][0]).upper() + str(name.split(" ")[1][0]).upper())
