#This program takes an ordered list of numbers then decides whether or
#not the given number is inside the list and returns (then prints) an appropriate boolean.

a = [1, 3, 5, 30, 42, 43, 500]


while True:
    num = int(input("Enter a number: "))

    if num in a:
        print("True")
        break

    else:
        print("False")
