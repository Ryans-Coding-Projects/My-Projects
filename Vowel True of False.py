def is_vowel(char):
    all_vowels = "aeiou"
    return char in all_vowels
w = input("Enter a letter: ")
print(is_vowel(w))
