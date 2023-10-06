#This program takes a number and returns all possible powers of given number

n = int(input("Enter number: "))
func = [1 << i for i in range(n+1)]
print(func)


