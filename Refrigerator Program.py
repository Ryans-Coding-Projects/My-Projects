print("Refrigerator")

print("------------")

y="open"

z="closed"

i=10

while i>5:
    door = input("Open Fridge Door?: ")

    if door == "yes":
        print("Refrigerator Light On")
        temperature = int(input("Set Refrigerator Temperature: [30-40] Degrees F"))
        while temperature>40 or temperature<30:
            print("Invalid Temperature")
            temperature = int(input("Set Refrigerator Temperature: [30-40] Degrees F"))
        print("Temperature set to, " , temperature , "degrees F")
        close_door = input("Close Fridge Door?: ")

    if door == "no" or close_door=="yes":
        print("Rerigerator Light Off")
        break
        
    
    






