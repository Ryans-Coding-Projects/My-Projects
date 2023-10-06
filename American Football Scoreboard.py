team1_name = input("Enter The Name Of Team 1: ")

team2_name = input("Enter The name Of team_2: ")

team1_score_total = int(input("ENTER Team 1's Current Score: "))

team2_score_total = int(input("ENTER Team 2's Current Score: "))

while True:

    print("------------------------------------------")
    print(team1_name , "Score Is:" , team1_score_total)
    print(team2_name , "Score Is:" , team2_score_total)
    print("------------------------------------------")
    choice = int(input("[ENTER: 1] to Update Team 1 Score Or [ENTER: 2] to Update Team 2 Score: "))

    if choice == 1:
        print("--------------------------------------------------")
        print("Score Update for" , team1_name)
        print("--------------------------------------------------")
        print("[ENTER 1] To Add Touchdown W/ No Additional Points")
        print("[ENTER 2] To Add Touchdown + Fieldgoal")
        print("[ENTER 3] To Add Touchdown + 2/Point Conversion")
        print("[ENTER 4] To Add 3-Point Fieldgoal")
        print("[ENTER 5] To Make Defined Changes To Current Score")
        print("[ENTER 6] To Return")
        print("--------------------------------------------------")
        team1choice = int(input("ENTER CHOICE: "))

        if team1choice == 1:
            team1_score_total = team1_score_total + 6
            print(" ")
            print("Succesfully Updated Score")
            print("Returning.......")
            print(" ")

        if team1choice == 2:
            team1_score_total = team1_score_total + 7
            print(" ")
            print("Succesfully Updated Score")
            print("Returning.......")
            print(" ")

        if team1choice == 3:
            team1_score_total = team1_score_total +8
            print(" ")
            print("Succesfully Updated Score")
            print("Returning.......")
            print(" ")

        if team1choice == 4:
            team1_score_total = team1_score_total + 3
            print(" ")
            print("Succesfully Updated Score")
            print("Returning.......")
            print(" ")

        if team1choice == 5:
            team1_score_total = int(input("Enter New Score For Team 1: "))

        if team1choice == 6:
            print(" ")
            print("Returning......... ")
            print(" ")
        

    if choice == 2:                           
        print("--------------------------------------------------")
        print("Score Update for" , team2_name)
        print("--------------------------------------------------")
        print("[ENTER 1] To Add Touchdown W/ No Additional Points")
        print("[ENTER 2] To Add Touchdown + Fieldgoal")
        print("[ENTER 3] To Add Touchdown + 2/Point Conversion")
        print("[ENTER 4] To Add 3-Point Fieldgoal")
        print("[ENTER 5] To Make Defined Changes To Current Score")
        print("[ENTER 6] To Return")
        print("--------------------------------------------------")
        team2choice = int(input("ENTER CHOICE: "))

        if team2choice == 1:
            team2_score_total = team2_score_total + 6
            print(" ")
            print("Succesfully Updated Score")
            print("Returning.......")
            print(" ")

        if team2choice == 2:
            team2_score_total = team2_score_total + 7
            print(" ")
            print("Succesfully Updated Score")
            print("Returning.......")
            print(" ")

        if team2choice == 3:
            team2_score_total = team2_score_total + 8
            print(" ")
            print("Succesfully Updated Score")
            print("Returning.......")
            print(" ")

        if team2choice == 4:
            team2_score_total = team2_score_total + 3
            print(" ")
            print("Succesfully Updated Score")
            print("Returning.......")
            print(" ")

        if team2choice == 5:
            team2_score_total = int(input("Enter New Score For Team 2: "))

        if team2choice == 6:
            print(" ")
            print("Returning......... ")
            print(" ") 

        else:
            print("")
            
        




