from random import randint

board = []

#Creating the 5*5 board
for x in range(5):
    board.append(["O"] * 5)

#Function for printing the board in a clean way, so that we eliminate the commas
def print_board(board):
    for row in board:
        print " ".join(row)

#Begin the game
print "Let's play Battleship!"

#View the board
print_board(board)

#GEnearter random row and col using Python to place the ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#The coordinates of the random numbers are as follows
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

for turn in range(0,4):
    guess_row = input("Guess Row:")
    guess_col = input("Guess Col:")

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
            
    # Print (turn + 1) here!
    print "That was turn ", turn+1
    print_board(board)
    