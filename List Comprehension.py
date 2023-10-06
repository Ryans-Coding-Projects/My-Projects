#This program takes a list and only displays the even numbers in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even = [a for a in a if a % 2 ==0]

print(even)
