from random import randint
#importing the randint function from the random module

board = [] #Generating our board - 5x5 grid of all 'O's for ocean.

for x in range(5): #This for loop creates 5 columns with 5 rows each
    board.append(["O"]*5)

def print_board(board): #This function prints out the board evenly like a grid
    for row in board:
            print " ".join(row) #gets rid of the quotation marks and commas

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board)-1) #Returns a random variable anywhere from 0 to 4

def random_col(board):
    return randint(0, len(board[0])-1)

ship_row = random_row(board)
ship_col = random_col(board)


print "Turn", 1
for turn in range(1,6):
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        board[guess_row][guess_col]="@"
        break #Note: Use the break command to get out of a for loop
    else:
        if (guess_row < 0 or guess_row > len(board)-1) or (guess_col < 0 or guess_col > len(board[0])-1):
            print "Oops, that's not even in the ocean."
        elif (board[guess_row][guess_col]=="X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col]="X"

        if turn == 5:
            print "Game Over"
            board[ship_row][ship_col]="@"
        else:
            print "Turn", turn+1

        print_board(board)
