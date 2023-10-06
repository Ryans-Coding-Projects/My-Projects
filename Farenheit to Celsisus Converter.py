#Welcome Message
print("This Program is Used to Convert Farenheit to Celsius, or Celsius to Farenheit.")
#Option menu
print("Would You Like To Convert Farenheit or Celsius First?")

print("------------------------------------------------------------------------------")
#Give Choice of farenheit or celsius conversion
choice = int(input("ENTER 1: For Farenheit or ENTER 2 For Celsius: "))

print("------------------------------------------------------------------------------")
#Equation for Farenheit To Celsius
if choice == 1:
    farenheit = int(input("Enter Temperature In Farenheit: "))
    farenheit = ((farenheit - 32) * .5556)
    print("Your Answer Is",farenheit,"°C")
#Equation for Celsius to farenheit    
if choice == 2:
    celsius = int(input("Enter Temperature In Celius: "))
    celsius = ((celsius * 1.8) + 32)
    print("Your Answer is",celsius,"°F")

