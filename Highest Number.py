#This program allows the user to enter a desired amount of numbers then adds them to a list and displays the highest number from the list

num = []

n = int(input("How many numbers would you like to enter?: "))

print("\nEnter numbers 1 by 1")

for i in range(0, n):
    ele = int(input("\nEnter number: "))
    num.append(ele)

print(max(num))
