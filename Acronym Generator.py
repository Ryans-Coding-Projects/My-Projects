#This program creates an acronym from the user's input of strings

acronym = input("Enter a String: ")

phrase = acronym.replace("of","").split()


a = ""

for word in phrase:
    a = a + word[0].upper()

print(f"The acronym for {acronym} is {a}")
