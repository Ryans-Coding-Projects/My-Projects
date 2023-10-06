print("This program allows you to enter a number and returns whether it's even or odd.\n ")

num = int(input("Enter a number: "))

mod = num % 2


if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")
