from random import randint
import time

def Game(Player1, Player2):

    print('Game beginning in...')
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("Go!\n")

    print ("Turn", 1)
    
    #Setting a specific battleship location for testing
    """
    Player2.ship_row = 0
    Player2.ship_col = 0
    Player1.ship_row = 0
    Player1.ship_col = 0
    """

    #Reset player boards
    Player1.ship_row = randint(0, len(Player1.board)-1)
    Player1.ship_col = randint(0, len(Player1.board)-1)

    Player2.ship_row = randint(0, len(Player2.board)-1)
    Player2.ship_col = randint(0, len(Player2.board)-1)
    
    #For automatically incrementing guesses across the board
    """
    row_count = 0
    column_count = 0
    """
    for turn in range(1,26):


        ##For automatically incrementing guesses across the board
        """
        p1_guess_row = row_count
        p1_guess_col = column_count
        p2_guess_row = row_count
        p2_guess_col = column_count
        if turn%5==0: column_count += 1
        if row_count == 4: row_count = 0
        else: row_count += 1
        """

        p1_guess_row = int(input("Player 1 Guess Row: "))
        p1_guess_col = int(input("Player 1 Guess Col: "))

        p2_guess_row = int(input("Player 2 Guess Row: "))
        p2_guess_col = int(input("Player 2 Guess Col: "))

        game_status = 0 #in session
        game_result = 0 #tie
        if p1_guess_row == Player2.ship_row and p1_guess_col == Player2.ship_col:
            print("--------------\nCongratulations! " + Player1.username + " has sunk " + Player2.username + "'s ship!\n")
            Player2.board[p1_guess_row][p1_guess_col]="@"
            game_status = 1 #over
            game_result = 1 #player 1 has won
            Player1.has_hit()
            Player1.has_won()
            Player2.has_lost()

        if p2_guess_row == Player1.ship_row and p2_guess_col == Player1.ship_col:
            print("--------------\nCongratulations! " + Player2.username + " has sunk " + Player1.username + "'s ship!\n")
            Player1.board[p1_guess_row][p1_guess_col]="@"
            game_status = 1 #over
            if game_result == 1: #tie
                game_result = 0
                #backtracking since it's a tie now
                Player2.has_hit()
                Player1.wins -= 1
                Player2.loses -= 1

            else: 
                game_result = 2 #player 2 has won
                Player2.has_hit()
                Player2.has_won()
                Player1.has_lost()

        if game_status == 1:
            print(Player1.username + "'s Board")
            Player1.print_board()
            print("\n")

            print(Player2.username + "'s Board")
            Player2.print_board()
            print("\n")
            break

        else:
            #Player 1 miss cases
            Player1.has_missed()
            if (p1_guess_row < 0 or p1_guess_row > len(Player2.board)-1) or (p1_guess_col < 0 or p1_guess_col > len(Player2.board[0])-1):
                print ("Oops, that's not even in the ocean.")
            elif (Player2.board[p1_guess_row][p1_guess_col]=="X"):
                print ("You guessed that one already.")
            else:
                print ("You missed my battleship!")
                Player2.board[p1_guess_row][p1_guess_col]="X"
            
            #Player 2 miss cases
            Player2.has_missed()
            if (p2_guess_row < 0 or p2_guess_row > len(Player1.board)-1) or (p2_guess_col < 0 or p2_guess_col > len(Player1.board[0])-1):
                print ("Oops, that's not even in the ocean.")
            elif (Player1.board[p2_guess_row][p2_guess_col]=="X"):
                print ("You guessed that one already.")
            else:
                print ("You missed my battleship!")
                Player1.board[p2_guess_row][p2_guess_col]="X"

            if turn == 25:
                print ("Game Over")
                Player1.board[Player1.ship_row][Player1.ship_col]="@"
                Player2.board[Player2.ship_row][Player2.ship_col]="@"
                print ("I can't believe you both couldn't find each others' battleships!")
            else:
                print ("Turn", turn+1)

            print(Player1.username + "'s Board:\n")
            Player1.print_board()
            print("\n")

            print(Player2.username + "'s Board:\n")
            Player2.print_board()
            print("\n")

class Player:

    def __init__(self, username):
        self.reset_board()
        self.username = username

        #Statistics
        self.wins = 0
        self.loses = 0
        self.hits = 0
        self.misses = 0

        self.ship_row = randint(0, len(self.board)-1)
        self.ship_col = randint(0, len(self.board)-1)

    def print_board(self): 
        for row in self.board:
            print (" ".join(row))

    def reset_board(self):
        self.board = []
        for x in range(5):
            self.board.append(["O"]*5)

    def has_won(self):
        self.wins += 1

    def has_lost(self):
        self.loses += 1

    def has_hit(self):
        self.hits += 1

    def has_missed(self):
        self.misses += 1

if __name__ == "__main__":
    print ("Let's play Battleship!")
    
    Player1 = Player(input("Enter Player 1 Username: "))
    Player2 = Player(input("Enter Player 2 Username: "))
    
    #TO-DO: addBattleships(int(input("How many battleships will be present in this game? ")))
    Game(Player1, Player2)
    
    while True:

        print("Statistics: \n--------------\n")
        print("user: " + Player1.username)
        print("wins: " + str(Player1.wins))
        print("loses: " + str(Player1.loses))
        print("hits: " + str(Player1.hits))
        print("misses: " + str(Player1.misses))
        try:
            print("hit %: " + "{:.1f}".format(float(Player1.hits/(Player1.hits+Player1.misses)*100)) + "%\n--------------\n")
        except ZeroDivisionError:
            print("hit %: - \n--------------\n")
        print("user: " + Player2.username)
        print("wins: " + str(Player2.wins))
        print("loses: " + str(Player2.loses))
        print("hits: " + str(Player2.hits))
        print("misses: " + str(Player2.misses))
        try:
            print("hit %: " + "{:.1f}".format(float(Player2.hits/(Player2.hits+Player2.misses))*100) + "%\n--------------\n")
        except ZeroDivisionError:
            print("hit %: - \n--------------\n")
        
        print("\n--------------\n")
        rematch_response = input("Want to play again? ")
        if rematch_response =='y' or rematch_response =='Y':
            Game(Player1, Player2)
        else:
            break

