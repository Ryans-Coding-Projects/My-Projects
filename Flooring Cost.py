#This program is used to calculate the cost of a new floor

print("\nAnswer a few questions to calculate the total cost a new floor.")

while True:
    print("\n1. Carpet ")
    print("2. Wood ")
    print("3. Vinyl ")
    floor_choice = int(input("\nEnter your choice of new flooring: "))
    if floor_choice == 1:
        floor_choice = 2.50
        floor_type = "carpet"
        break
    elif floor_choice == 2:
        floor_choice = 9
        floor_type = "wood"
        break
    elif floor_choice == 3:
        floor_choice = 6
        floor_type = "vinyl"
        break
    else:
        print("\nInvalid floor choice. Choose a floor type by entering numbers 1, 2, or 3.")
floor_size = int(input("\nEnter the total square footage of floor to be replaced: "))
floor_cost = floor_choice * floor_size
floor_cost = "{:.2f}".format(floor_cost)

print(f"\nThe total cost for the new {floor_type} floor is ${floor_cost}")
