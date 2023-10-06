print("Vending Machine - 1.4.135")

print("-------------------------")

money = int(input("Enter Money in Dollars: "))

while money >10:
    print("This Machine Does Not Accept Bills Larger Then 10")
    print("-------------------------")
    money = int(input("Enter Money in Dollars: "))

i=0    

balance = 0 + money

    
while i != 50:
    print(" ")

    print("BALANCE: $" , balance)

    print(" ")
   
    print("-------------------------")
    print("----------MENU-----------")
    print("-------------------------")
    print("ENTER 101:Monster Energy Drink")
    
    print(" ")

    print("ENTER 102:Bang Energy Drink")

    print(" ")

    print("ENTER 103:Reign Energy Drink")

    print(" ")

    print("ENTER 104:Coca-Cola ")

    print(" ")

    print("ENTER 105:Coca-Cola Cherry")

    print(" ")

    print("ENTER 106:Mountain Dew")

    print(" ")

    print("ENTER 107:Diet Mountain Dew")

    print(" ")

    print("ENTER 108:Dr. Pepper")

    print(" ")

    print("ENTER 109:Orange Juice")

    print(" ")

    print("ENTER 110:Dasani Water")

    print(" ")

    print("ENTER 0:REFUND")

    print(" ")

    print("-------------------------")

    selection = int(input("Selection:"))

    if selection==101 and balance>4.50:
        balance=balance-4.50
        print("Vending......Thank You")
        
    if selection==102 and balance>4.50:
        balance=balance-4.50
        print("Vending......Thank You")
        print("-------------------------")

    if selection==103 and balance>4.50:
        balance=balance-4.50
        print("Vending......Thank You")
        print("-------------------------")

    if selection==104 and balance>2.50:
        balance=balance-2.50
        print("Vending......Thank You")
        print("-------------------------")

    if selection==105 and balance>2.50:
        balance=balance-2.50
        print("Vending......Thank You")
        print("-------------------------")

    if selection==106 and balance>2.50:
        balance=balance-2.50
        print("Vending......Thank You")
        print("-------------------------")

    if selection==107 and balance>2.50:
        balance=balance-2.50
        print("Vending......Thank You")

    if selection==108 and balance>2.50:
        balance=balance-2.50
        print("Vending......Thank You")
        print("-------------------------")

    if selection==109 and balance>2.00:
        balance=balance-2.00
        print("Vending......Thank You")
        print("-------------------------")

    if selection==110 and balance>1.50:
        balance=balance-1.50
        print("Vending......Thank You")
        
    if selection == 0:  
        print("Thank You. Balance: $" , balance , "Returned")
        break
    
    if balance < 1.50:
        print("-------------------------")
        print("Not Enough Money To Complete This Transaction")
        break

    

  
 

        
