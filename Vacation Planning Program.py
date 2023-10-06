
each=8

city=9

nature=10

couple=11

friend=12

family=13

print("Let's Plan Your Next Vacation!")

print(" ")

vacation_type = int(input("What Type Of Vacation Do You Want? ENTER: 1-[beach] or 2-[nature] or 3-[city] "))

while vacation_type > 3 or vacation_type < 1:   
        print("[INVALID ENTRY: TRY AGAIN]")
        vacation_type = int(input("What Type Of Vacation Do You Want? ENTER: 1-[beach] or 2-[nature] or 3-[city] "))
        
print(" ") 

vacation_budget =int(input("Whats Your Budget?: $"))

while vacation_budget < 500:
    print("You Can Not Afford a Vacation With That Amount")
    vacation_budget = int(input("Enter A New Budget?: $"))

print(" ")

vacation_group = int(input("Who's Going On This Vacation? ENTER: 4-[couple] or 5-[friends] or 6-[family] "))

while vacation_group > 6 or vacation_group < 4:
        print("[INVALID ENTRY: TRY AGAIN]")
        vacation_group = int(input("Who's Going On This Vacation? ENTER: 4-[couple] or 5-[friends] or 6-[family] "))
        
print(" ")

if vacation_type == 1 and vacation_budget > 5000 and vacation_group == 4:
    print("Bora Bora - Would Be A Great Destination!")
    
if vacation_type == 1 and vacation_budget < 5000 and vacation_group == 5:
    print("Miami. Florida - Would Be A Great Destination!")

if vacation_type == 1 and vacation_budget > 5000 and vacation_group == 6:
    print("Honolulu, Hawaii - Would Be A Great Destination!")

if vacation_type == 2 and vacation_budget > 5000 and vacation_group == 4:
    print("Iceland - Would Be A Great Destination!")

if vacation_type == 2 and vacation_budget > 5000 and vacation_group == 5:
    print("Denver, Colorado - Would Be A Great Destination!")

if vacation_type == 2 and vacation_budget < 5000 and vacation_group == 6:
    print("Yosemite National Park - Would Be A Great Destination!")

if vacation_type == 3 and vacation_budget > 5000 and vacation_group == 4:
    print("Paris, France - Would Be A Great Destination!")

if vacation_type == 3 and vacation_budget < 5000 and vacation_group == 5:
    print("Las Vegas, Nevada - Would Be A Great Destination!")

if vacation_type == 3 and vacation_budget > 5000 and vacation_group == 6:
    print("New York City, New york - Would Be A Great Destination!")


  



