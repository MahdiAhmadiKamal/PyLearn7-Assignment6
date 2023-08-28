import pyfiglet

def show_game_board():
    for row in game_board:
        for cell in row:
            print (cell, end=" ")
        print ()
    print ()
      
def check_game():
    if game_board[row][0]==game_board[row][1]==game_board[row][2]!="_" or game_board[0][col]==game_board[1][col]==game_board[2][col]!="_":
        print (player, "won.")
        exit()
    elif game_board[0][0]==game_board[1][1]==game_board[2][2]!="_" or game_board[0][2]==game_board[1][1]==game_board[2][0]!="_":
        print (player, "won.")
        exit()
    elif sum(row.count("_") for row in game_board) == 0:  #Draw condition
        print ("Draw")
        exit()



title = pyfiglet.figlet_format ("Tic Tac Toe", font="slant")
print (title)

game_board = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]]

show_game_board()

while True:

    print ("Player 1")
    while True:
        row = int (input("row: "))
        col = int (input("col: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board [row][col] == "_":
                game_board [row][col] = "X"
                break
            else:
                print ("This cell is filled.")
        else:
            print ("The input number must be between 0 and 2.")

    show_game_board()
    player = "Player 1"
    check_game()

    print ("Player 2")
    while True:
        row = int (input("row: "))
        col = int (input("col: "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board [row][col] == "_":
                game_board [row][col] = "O"
                break
            else:
                print ("This cell is filled.")
        else:
            print ("The input number must be between 0 and 2.")
    show_game_board()
    player = "Player 2"
    check_game()