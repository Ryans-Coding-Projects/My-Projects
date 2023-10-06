#Tic-Tac-Toe game in Python

#Create the board
board = ["-", "-", "-",         "-", "-", "-",         "-", "-", "-"]

#Fucntion to display the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

#Fucntion to play a move
def play_move(player, position):
    board[position] = player

#Fucntion to check if the game is over
def check_game_over():
    #Check rows
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #Check columns
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    #Check diagonals
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    #If any row, column, or diagonal is filled with same player, return True
    if row_1 or row_2 or row_3 or col_1 or col_2 or col_3 or diag_1 or diag_2:
        return True
    #Check if the board is full
    if "-" not in board:
        return True
    #If the game is not over trturn false
    return False

#Function to check who won
def check_winner():
    #Check rows
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] !="-"
    #Check columns
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    #Check diagonals
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    #Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board
    elif row_3:
        return board[6]
    elif col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    elif diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    else:
        return None

# Main game loop
def game():
    print("Welcome to Tic-Tac-Toe!")
    current_player = "X"
    game_over = False
    while not game_over:
        display_board()
        print(f"{current_player}'s turn. Please choose a position (1-9).")
        choice = input()
        try:
            choice = int(choice)
            if choice in range(1, 10) and board[choice - 1] == "-":
                play_move(current_player, choice - 1)
                if check_game_over():
                    game_over = True
                    winner = check_winner()
                    if winner:
                        print(f"{winner} wins!")
                    else:
                        print("It's a tie!")
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid choice. Please choose a valid position.")
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 9.")

# Start the game
game()
