#This program generates a fibonacci sequence.

num = int(input("Enter Number: "))

fib=[0,1]

n1,n2= 0,1

while True:
    n1, n2 = n2, n1 + n2
    fib.append(n1)
    if len(fib) == num:
        break
    
print(*fib)
