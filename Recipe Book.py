recipes = {}

while True:
    print("\nCOOKBOOK")
    print("--------")
    print("1. To Add A New Recipe")
    print("2. To View A Recipe")
    print("3. To Remove A Recipe")
    print("4. To Exit")
    choice = int(input())

    if choice == 1:
        name = input("Enter the name for this recipe: ")
        recipe = input("Enter the full recipe: ")
        recipes[name.lower()] = recipe
        print("Recipe added succesfully!")

    if choice == 2:
        recipe_name = input("Which recipe would you like to view?: ").lower()
        if recipe_name in recipes:
            print(recipes[recipe_name])
        else:
            print("Sorry, that recipe is not in the cookbook. ")

    elif choice == 3:
        input("Which recipe would you like to remove?: ").lower()
        recipe_name = input("Which recipe would you like to remove?").lower()
        if recipe_name in recipes:
            del recipes[recipe_name]
            print("Recipe removed succesfully. ")
        else:
            print("Sorry, that recipe is not in the cookbook. ")

    elif choice == 4:
        input("Exiting Recipe Book....")
        break

    else:
        print("Invalid choice. Please enter as number between 1 and 4.\n")

        


             
