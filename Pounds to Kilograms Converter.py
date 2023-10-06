#Welcome Message
print("This Program is Used to Convert Pounds (lb) to Kilograms(kg),")
print(" or Kilograms(kg) to Pounds(lb)")
#Option menu
print("Would You Like To Convert Pounds or Kilograms First?")

print("------------------------------------------------------------------------------")
#Give Choice of Pounds or Kilograms conversion
choice = int(input("ENTER 1: For Pounds or ENTER 2 For Kilograms: "))

print("------------------------------------------------------------------------------")
#Equation for Pounds To Kilograms
if choice == 1:
    pounds = int(input("Enter Weight In Pounds: "))
    pounds_2 = (pounds/2.20462)
    print("Your Weight Converted from",pounds,"lbs, to", pounds_2, "kgs")
    
#Equation for Kilograms to Pounds    
if choice == 2:
    kilograms = int(input("Enter Weight In Kilograms: "))
    kilograms_2 = (kilograms*2.20462)
    print("Your Weight Converted from",kilograms, "kgs, to" , kilograms_2, "lbs")
