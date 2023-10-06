#This Program allows the user to enter a number and returns whether or not the input number is prime


def get_num():
    return int(input("Enter a Number: "))

num = get_num()

b= [n for n in range(1, num) if num % n == 0]

if len(b) == 1:
    print("\n" ,num, "Is A Prime Number")
else:
    print("\n", num, "Is Not A Prime Number")

   
        
