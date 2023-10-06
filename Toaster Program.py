#Name of Item To Program
print("Toaster")

print("-------")
#Variables for Toaster Options
a = "on"

b = "off"
#Option To Turn/Keep Toaster Off or Turn Toaster On
power = input("Toaster Power [ON] or [OFF]: ").lower()

1 == "toast"
#Function for power on
if power == "on":
    print("Toaster Power: ON")
    toast = int(input("Enter Time to Toast in Minutes MINIMUM[1 Minute] MAXIMUM[5 MINUTES]: "))
#While Loop - When Time is Entered Outside of Toaster Limit it Will Not Work
    while toast > 5 or toast < 1:
         print("Invalid Time")
         toast = int(input("Enter Time to Toast in Minutes MINIMUM[1 Minute] MAXIMUM[5 MINUTES]: "))
 #If statements to simulate toasting times in minutes and ask to power off after use   
    if toast == 1:
        print("Toasting For [1] Minute")
        print("......................")
        print("Toasting Complete")
        power = input("Toaster Power [ON] or [OFF]: ").lower()

    if toast == 2: 
        print("Toasting For [2] Minutes")
        print("......................")
        print("Toasting Complete")
        power = input("Toaster Power [ON] or [OFF]: ").lower()

    if toast == 3:
         print("Toasting For [3] Minutes")
         print("......................")
         print("Toasting Complete")
         power = input("Toaster Power [ON] or [OFF]: ").lower()

    if toast == 4:
        print("Toasting For [4] Minutes")
        print("......................")
        print("Toasting Complete")
        power = input("Toaster Power [ON] or [OFF]: ").lower()

    if toast == 5:
        print("Toasting For [5] Minutes")
        print("......................")
        print("Toasting Complete")
        power = input("Toaster Power [ON] or [OFF]: ").lower()
#Function to power off toaster
if power == "off":
    "toast" == 0
    print("Toaster Power: Off")
#Error Statement given if improper input is entered   
else:
    print("ERROR")

    

