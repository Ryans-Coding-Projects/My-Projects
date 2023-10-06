#This program allows user to input strings and returns the total count of vowels

vowel_counter = input("Enter String: ")

count = len([char for char in vowel_counter if char in "aeiouAEIOU"])

print("Number of Vowels: :", count)
