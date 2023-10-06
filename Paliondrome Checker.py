#This program prompts the user the enter a word and displays whether or not it is a palindrome.

word = input("Enter a Word: ").lower()


if word[::-1] == word:
    print("That word IS a paliondrome! ")

else:
    print("That word IS NOT a palindrome! ")
