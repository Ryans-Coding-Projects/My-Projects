#This program uses an array of numbers and returns the sum of only positive numbers

def positive_sum(arr):
    sum = 0
    for number in arr:
        if number > 0:
            sum += number
    return sum
