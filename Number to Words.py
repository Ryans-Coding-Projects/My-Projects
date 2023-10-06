arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def number_to_word(n):
    if n == 0:
        return ""
    else:
        last_digit = n % 10
        small_ans = arr[last_digit]
        return number_to_word(n // 10) + small_ans + " "

def main():
    n = int(input("Enter a number: "))
    print(number_to_word(n))

if __name__ == "__main__":
    main()


    
