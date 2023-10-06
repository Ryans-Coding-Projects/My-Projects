def display_options():
    options = {1: 6, 2: 7, 3: 8, 4: 3}
    print("--------------------------------------------------")
    print("[ENTER 1] To Add Touchdown W/ No Additional Points")
    print("[ENTER 2] To Add Touchdown + Fieldgoal")
    print("[ENTER 3] To Add Touchdown + 2/Point Conversion")
    print("[ENTER 4] To Add 3-Point Fieldgoal")
    print("[ENTER 5] To Make Defined Changes To Current Score")
    print("[ENTER 6] To Return")
    print("--------------------------------------------------")
    return options

def handle_choice(options, team_score_total):
    choice = int(input("ENTER CHOICE: "))
    if choice == 5:
        team_score_total = int(input("Enter New Score: "))
    elif choice in options:
        team_score_total += options[choice]
    return team_score_total

def update_score(team_name, team_score_total):
    print("--------------------------------------------------")
    print("Score Update for", team_name)
    print("--------------------------------------------------")
    options = display_options()
    team_score_total = handle_choice(options, team_score_total)
    return team_score_total

team1_name = input("Enter The Name Of Team 1: ")
team2_name = input("Enter The Name Of Team 2: ")
team1_score_total = int(input("Enter Team 1's Current Score: "))
team2_score_total = int(input("Enter Team 2's Current Score: "))

while True:
    print("------------------------------------------")
    print(team1_name, "Score Is:", team1_score_total)
    print(team2_name, "Score Is:", team2_score_total)
    print("------------------------------------------")
    choice = int(input("[ENTER 1] to Update Team 1 Score Or [ENTER 2] to Update Team 2 Score: "))

    if choice == 1:
        team1_score_total = update_score(team1_name, team1_score_total)
    elif choice == 2:
        team2_score_total = update_score(team2_name, team2_score_total)
    elif choice == 6:
       

       

                
    
