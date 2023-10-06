#This program can be used to convert many different types of units.

#Main Menu
#While loop to allow the user to continue performing conversions
while True:
    print("\n")
    print("|-------------------------|")
    print("|          MENU           |")
    print("|-------------------------|")
    print("| 1. Cm to Inches         |")
    print("| 2. Inches to Cm         |")
    print("| 3. Kg to Lbs            |")
    print("| 4. Lbs to Kg            |")
    print("| 5. Celsius to Farenheit |")
    print("| 6. Farenheit to Celsius |")
    print("| 7. Mph to Kph           |")
    print("| 8. Kph to Mph           |")
    print("| 9. Grams to Ounces      |")
    print("| 0. Exit                 |")
    print("|-------------------------|")

    #User choice function
    choice = int(input("\n\nWhich unit would you like to convert?: "))

    #Formulas for each of the conversions
    if choice == 1:
        cm_number = int(input("\nEnter measurement in centimeters: "))
        total_1 = cm_number / 2.54 
        print(cm_number, "centimeters is equal to", total_1, "inches." )

    elif choice == 2:
        inch_number = int(input("\nEnter measurement in inches: "))
        total_2 = inch_number * 2.54 
        print(inch_number, "inches is equal to", total_2, "centimeters." )
            
    elif choice == 3:
        kg_number = int(input("\nEnter weight in kilograms: "))
        total_3 = kg_number * 2.204 
        print(kg_number, "kilograms is equal to", total_3, "pounds." )

    elif choice == 4:
        pound_number = int(input("\nEnter weight in pounds: "))
        total_4 = pound_number * 0.453 
        print(pound_number, "pounds is equal to", total_4, "kilograms." )

    elif choice == 5:
        celsius_number = int(input("\nEnter temperature in celsius: "))
        total_5 = (celsius_number * 1.8) + 32 
        print(celsius_number, "degrees celsius is equal to", total_5, "degrees farenheit." )

    elif choice == 6:
        farenheit_number = int(input("\nEnter temperature in farenheit: "))
        total_6 = (farenheit_number - 32) * 0.555  
        print(farenheit_number, "degrees farenheit is equal to", total_6, "degrees celsius." )

    elif choice == 7:
        mph_number = int(input("\nEnter speed in mph: "))
        total_7 = mph_number * 1.609 
        print(mph_number, "MPH is equal to", total_7, "KPH." )

    elif choice == 8:
        kph_number = int(input("\nEnter speed in kph: "))
        total_8 = kph_number / 1.609 
        print(kph_number, "KPH is equal to", total_8, "MPH." )

    elif choice == 9:
        grams_number = int(input("\nEnter weight in grams: "))
        total_9 = grams_number *  0.035274 
        print(grams_number, "grams is equal to", total_9, "ounces." )

    #Allows user to exit when finished
    elif choice == 0:
        print("\nSuccesfully Exited")
        break

    #Tells user when invalid input is entered
    else:
        print("\nInvalid choice. Please enter a number between 0 and 9.")
    
        
