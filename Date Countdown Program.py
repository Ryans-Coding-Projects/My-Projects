#Import the date/time
from datetime import datetime

#Function to get user input and calculate the time between two dates
def days_between():
    while True:
        try:
            date1 = input("Enter the First Date in the Format YYYY-MM-DD: ")
            date2 = input("\nEnter the Second Date in the Format YYYY-MM-DD: ")
            date1 = datetime.strptime(date1, "%Y-%m-%d")
            date2 = datetime.strptime(date2, "%Y-%m-%d")
            delta = date2 - date1
            return delta.days
        except ValueError:
            print("Invalid date format. Please Enter the date in the Format YYYY-MM-DD.\n")

#Display results
print("\nThe Number of Days between the Two Dates is: ", days_between())
