a = "gallons"

b = "weight"

i=10

while i==10:

    choice = input("Would You Like To Convert Weight or Gallons?: ").lower()

    if choice == "weight":
        weight = int(input("Enter The Weight Of The Liquid In Pounds: "))
        weight_to_gallons = weight / 8.34 
        print("There Are" , weight_to_gallons , "Gallons In" , weight , "Pound(s)")
        break
       


    if choice == "gallons":
        gallons = int(input("Enter How Many Gallons Of Liquid: "))
        gallons_to_pounds = gallons * 8.34
        print("There Are" , gallons_to_pounds , "Pounds In" , gallons , "Gallon(s)")
        break
        


    if choice != "gallons" or "weight":
        print("INVALID CHOICE - Please Enter [WEIGHT] or [GALLONS]")
        
        
