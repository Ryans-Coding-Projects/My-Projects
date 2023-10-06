print("Welcome to the birthday dictionary. We know the birthdays of Albert Einstein, Benjamin Franklin, and Ada Lovelace.")

birthday_dictionary = {
    "Albert Einstein" : "03/14/1879",
    "Benjamin Franklin" : "01/06/1706",
    "Ada Lovelace" : "12/10/1815"
    }

choice = input("\nWho's birthday would you like to lookup?: ")

print("\n"+
      choice+"'s birthday is",birthday_dictionary[choice]+".")
