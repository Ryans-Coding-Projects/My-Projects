#Title message
print("\nMonthly Budget Planner\n")

#Program description
print("This Program Is Used To Calculate How Much Money You Will Have Left After\nAll Expenses Are Paid.")
print("-------------------------------------------------------------------------")

#Define users income
income = int(input("\nWhat Is Your Total Take Home Pay Per Month?: \n"))

#Assign yes and no variables
yes = "yes"
no = "no"

#Questions to define users expenses
#Car expenses
choice = input("Do You Own a Car?: \n").lower()
if choice == yes:
    car_insurance = int(input("How Much Do You Pay Per Month For Car insurance?: \n"))
    car_payment = int(input("How Much Do You Pay Per Month For Your Car Payment?: \n"))
    gas = int(input("How Much Do You Pay Per Month For Gas?: \n"))
if choice == no:
        car_insurance = 0
        car_payment = 0
        gas = 0
        
#Home expenses
choice1 = input("Do You Rent or Own a Home?: \n").lower()
if choice1 == yes:
    rent = int(input("How Much Do You Pay Per Month For Rent or Mortgage?: \n"))
    utilities = int(input("How Much Do You Pay Per Month For Utilities?: \n"))
if choice1 == no:
    rent = 0
    utilities = 0
    
#Phone expenses
choice2 = input("Do You Own A Phone?: \n").lower()
if choice2 == yes:
    phone_bill = int(input("How Much Do You Pay Per Month For Your Phone Bill?: \n"))
    choice4 = input("Are You Still Paying off the Phone?: \n").lower()
    if choice4 == yes:
        int(input("How Much Do You Pay Per Month For Your Phone Payment?: \n"))
    if choice4 == no:
        phone_payment = 0       
if choice2 == no:
    phone_bill = 0
    phone_payment = 0
    
#Internet expenses
choice3 = input("Do You Pay For Internet?: \n").lower()
if choice3 == yes:
    internet = int(input("How Much Do You Pay Per Month For Internet?: \n"))
if choice3 == no:
    internet = 0
    
#Food expenses 
food = int(input("How Much Do You Pay Per Month For Food?: \n"))

#Credit card expenses
choice5 = input("Do You Own A Credit Card?: \n").lower()
if choice5 == yes:
    credit_card = int(input("How Much Do You Pay Per Month For Youe Credit Card?: \n"))
if choice5 == no:
    credit_card=0
    
#Subscription expenses                               
monthly_subscriptions = int(input("How Much Do You Pay Per Month For Monthly Subscriptions? i.e.(Netflix, Hulu, Game Pass): \n"))

#Other expenses
other_expenses = int(input("Enter Any Expenses That Were Not Entered Above: \n"))

#Equation to add up all expenses        
total_expenses = rent + food + car_insurance + credit_card + monthly_subscriptions + car_payment + gas + phone_bill + internet + other_expenses + utilities + phone_payment

#Equation for subtrating the total expenses from users income
budget = income - total_expenses
#Display results

if budget < 0:
    print("\n\nYou are overspending. Please revise your Expenses.\n Your Remaining Money Is $" , str(budget)) 
else:
    print("\n\nYour Money Remaining For The Month Is: $" + str(budget))

        
    
    
