#This program allows the user to enter any word and then returns the word scrambled

import random

string = input("Enter Text: ")

shuffled_string = "".join(random.sample(string, len(string)))

print(shuffled_string)


    
