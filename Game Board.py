#This program ask for user input and creates a gameboard defined by it

def board(n):
    for i in range(n):
        print((" "+"-"*n)*n+" ")
        print(("|"+n*" ")*n+"|")

    print((" "+"-"*n)*n+" ")

g = int(input("Enter the size of the game board: "))
board(g)




    
   

