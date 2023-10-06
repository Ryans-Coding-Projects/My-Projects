#This program is used to set a 4 digit pin number on a door.

MAX_GUESSES = 3

while True:
    pin = int(input("\nSet 4-Digit PIN: "))
    if pin < 1000 or pin >= 10000:
              print("\nPIN must be 4 digits: ")
    else:
        break

while True:
    pin_confirmation = int(input("\nConfirm 4 Digit PIN: "))
    if pin_confirmation == pin:
        print(f"\nPIN Set to {pin_confirmation}")
        break
    else:
        print("\nPINS do not match")

guesses = MAX_GUESSES      

while guesses > 0:
    pin_input = input("\nEnter PIN: ")
    if len(pin_input) != 4:
        print("\nInvalid PIN")
        continue
    pin_guess = int(pin_input)
    if pin_guess == pin:
        print("\nDoor Unlocked")
        break
    else:
        guesses -= 1
        print(f"\nWrong PIN. {guesses} attempts left")

else:
    print("\nToo many incorrect attempts. Locked out")
        

    
        
