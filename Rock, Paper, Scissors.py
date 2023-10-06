import random

print("------------------------------------------------")

while True:

    print("Play Rock, Paper, Scissors against the Computer!")

    print("------------------------------------------------")

    user_choice = input("Enter [Rock], [Paper], or [Scissors] to Begin: ")

    print("------------------------------------------------")

    possible_choices = ["rock" , "paper" , "scissors"]

    computer_choice = random.choice(possible_choices)

    print("Your Choice Is:" , {user_choice} , "And the Computers Choice Is:" , {computer_choice})

    if user_choice == computer_choice:
        print("It's a Tie")
        print("------------------------------------------------")
    
    elif user_choice == "rock" :
        if computer_choice=="scissors" :
            print("YOU WIN! - Rock Beats Scissors")
            print("------------------------------------------------")
        else:
            print("YOU LOSE! - Paper Beats Rock")
            print("------------------------------------------------")
        
    elif user_choice == "paper" :
        if computer_choice=="rock" :
            print("YOU WIN! - Paper Beats Rock")
            print("------------------------------------------------")
        else:
            print("YOU LOSE! - Scissors Beats Paper")
            print("------------------------------------------------")
        
    elif user_choice == "scissors" :
        if computer_choice=="paper" :
            print("YOU WIN! - Scissors Beats Paper")
            print("------------------------------------------------")
        else:
           print("YOU LOSE! - Rock Beats Scissors ")
           print("------------------------------------------------")

    
    play_again = input("Would You Like to Play Again? [yes] or [no]): ")
    if play_again.lower() != "yes":
        print(" ")
        print("Thanks For Playing!")
        break


        
    

   
