#Import time 
import time

#Define the timer and it's function and display results
def timer():
    seconds = int(input("Enter the number of seconds for the timer: "))
    print("Timer started for {} seconds.".format(seconds))
    time.sleep(seconds)
    print("Time's up!")
    
timer()
    
