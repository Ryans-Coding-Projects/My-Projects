import datetime

try:
    # Get user input
    username = input("Enter Your Name: ")
    today_year = int(input("Enter The Current Year: "))
    birth_month = int(input("Enter The Month You Were Born (MM): "))
    birth_day = int(input("Enter The Day You Were Born (DD): "))
    birth_year = int(input("Enter The Year You Were Born (YYYY): "))

    # Check if the date is valid
    birth_date = datetime.datetime(birth_year, birth_month, birth_day)

    print("--------------------------------------------------")

    # Calculate the user's birthday and age
    today = datetime.datetime.now()
    age = today.year - birth_year
    if (today.month, today.day) < (birth_month, birth_day):
        age -= 1

    # Calculate time alive in various units
    alive_seconds = int((today - birth_date).total_seconds())
    alive_minutes = alive_seconds // 60
    alive_hours = alive_minutes // 60
    alive_days = alive_hours // 24
    alive_months = alive_days // 30.44  # average number of days in a month
    alive_years = alive_days // 365.2425

    # Print the information
    print(f"{username},\n")
    print("Your Birthday Is:", birth_date.strftime("%B %d, %Y"))
    print("Your Age Is:", age)
    print("You've Been Alive For", alive_seconds, "Seconds")
    print("You've Been Alive For", alive_minutes, "Minutes")
    print("You've Been Alive For", alive_hours, "Hours")
    print("You've Been Alive For", alive_days, "Days")
    print("You've Been Alive For", int(alive_months), "Months")
    print("You've Been Alive For", int(alive_years), "Years")
    print("--------------------------------------------------")

    # Wait for user input to exit the program
    input("Press Enter to exit...")

except ValueError:
    print("Invalid date, please enter a valid date.")





