import datetime

current_year = datetime.datetime.now().year

name = input("Enter your name: ")

age = int(input("\nHow old are you?: "))

print(f"\n{name}, you will be 100 years old in {current_year - age + 100}.")
