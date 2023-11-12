#This program is used to estimate the total cost of a landscaping job

print("Welcome to CCE Landscaping. Use our short survey to estimate your total cost!")

yard_size = int(input("\nFirst, Please enter the estimated size of your front yard + back yard in square feet: "))

# Cost based on choices
grass_cost_choice = input("\nWould you like your grass mowed? Enter Yes or No: ").lower()
tree_pruning_choice = input("\nWould you like your trees pruned? Enter Yes or No: ").lower()
mulching_cost_choice = input("\nWould you like your yard mulched? Enter Yes or No: ").lower()
hedge_trimming_choice = input("\nWould you like your hedges trimmed? Enter Yes or No: ").lower()
snow_removal_choice = input("\nWould you like snow removed? Enter Yes or No: ").lower()
leaf_removal_choice = input("\nWould you like leaves removed? Enter Yes or No: ").lower()
sidewalk_cleaning_choice = input("\nWould you like your sidewalks cleaned? Enter Yes or No: ").lower()
flower_bed_choice = input("\nWould you like a new flower bed installed? Enter Yes or No: ").lower()
new_pathway_choice = input("\nWould you like a new pathway installed? Enter Yes or No: ").lower()

# Numerical cost values
grass_cost = yard_size * 0.25 if grass_cost_choice == "yes" else 0
tree_pruning_cost = int(input("How many trees need pruning: ")) * 15 if tree_pruning_choice == "yes" else 0
mulching_cost = 100 if mulching_cost_choice == "yes" else 0
hedge_trimming_cost = int(input("Enter number of hedges that need trimmed: ")) * 35 if hedge_trimming_choice == "yes" else 0
snow_removal_cost = yard_size * 0.50 if snow_removal_choice == "yes" else 0
leaf_removal_cost = yard_size * 0.75 if leaf_removal_choice == "yes" else 0
sidewalk_cleaning_cost = 40 if sidewalk_cleaning_choice == "yes" else 0
flower_bed_cost = 150 if flower_bed_choice == "yes" else 0
new_pathway_cost = 250 if new_pathway_choice == "yes" else 0

# Calculate total cost
total_cost = grass_cost + tree_pruning_cost + mulching_cost + hedge_trimming_cost + snow_removal_cost + leaf_removal_cost + sidewalk_cleaning_cost + flower_bed_cost + new_pathway_cost

print(f"\nThe estimated total cost for your services is ${total_cost}")

print("\nThank you for taking the time to complete our survey!")
