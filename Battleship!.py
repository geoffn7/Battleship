from random import randint
import time

def Game(Player1, Player2):

    #Set up ships and boards
    player1_progress_board = []
    for x in range(5):
        player1_progress_board.append(["O"]*5)

    player2_progress_board = []
    for x in range(5):
        player2_progress_board.append(["O"]*5)

    ships = int(input("How many battleships will be present in this game? "))
    if ships > 25:
        print("There's more ships than the ocean can handle! 7 ships seems reasonable.")
        ships = 7

    player1_ships = []
    player2_ships = []
    while len(player1_ships) < ships:
        player1_ship_row = randint(0, len(player1_progress_board)-1)
        player1_ship_col = randint(0, len(player1_progress_board[0])-1)

        if [player1_ship_row, player1_ship_col] not in player1_ships:
            player1_ships.append([player1_ship_row, player1_ship_col])

    while len(player2_ships) < ships:
        player2_ship_row = randint(0, len(player2_progress_board)-1)
        player2_ship_col = randint(0, len(player2_progress_board[0])-1)

        if [player2_ship_row, player2_ship_col] not in player2_ships:
            player2_ships.append([player2_ship_row, player2_ship_col])
    
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
    
    for turn in range(1,26):

        player1_hit_ship = False
        player2_hit_ship = False

        p1_guess_row = int(input("Player 1 Guess Row? "))
        p1_guess_col = int(input("Player 1 Guess Col? "))

        p2_guess_row = int(input("\nPlayer 2 Guess Row? "))
        p2_guess_col = int(input("Player 2 Guess Col? "))

        for ship in player2_ships:
            if p1_guess_row == ship[0] and p1_guess_col == ship[1]:
                print("--------------\n" + Player1.username + " has sunk " + Player2.username + "'s ship!\n")
                player2_progress_board[p1_guess_row][p1_guess_col]="@"
                Player1.has_hit()
                player2_ships.remove([p1_guess_row, p1_guess_col])
                player1_hit_ship = True

        for ship in player1_ships:
            if p2_guess_row == ship[0] and p2_guess_col == ship[1]:
                print("--------------\n" + Player2.username + " has sunk " + Player1.username + "'s ship!\n")
                player1_progress_board[p1_guess_row][p1_guess_col]="@"
                Player2.has_hit()
                player1_ships.remove([p2_guess_row, p2_guess_col])
                player2_hit_ship = True

        if player1_hit_ship == False:
            #Player 1 miss cases
            Player1.has_missed()
            if (p1_guess_row < 0 or p1_guess_row > len(player2_progress_board)-1) or (p1_guess_col < 0 or p1_guess_col > len(player2_progress_board[0])-1):
                print ("--------------\n@" + Player1.username + " Oops, that's not even in the ocean.")
            elif (player2_progress_board[p1_guess_row][p1_guess_col]=="X"):
                print ("--------------\n@" + Player1.username + " You guessed that one already.")
            else:
                print ("--------------\n@" + Player1.username + " You missed!")
                player2_progress_board[p1_guess_row][p1_guess_col]="X"
            
        if player2_hit_ship == False:
            #Player 2 miss cases
            Player2.has_missed()
            if (p2_guess_row < 0 or p2_guess_row > len(player1_progress_board)-1) or (p2_guess_col < 0 or p2_guess_col > len(player1_progress_board[0])-1):
                print ("--------------\n@" + Player2.username + " Oops, that's not even in the ocean.")
            elif (player1_progress_board[p2_guess_row][p2_guess_col]=="X"):
                print ("--------------\n@" + Player2.username + " You guessed that one already.")
            else:
                print ("--------------\n@" + Player2.username + " You missed!")
                player1_progress_board[p2_guess_row][p2_guess_col]="X"

        #Checking if a player has won
        if len(player2_ships) == 0 or len(player1_ships) == 0:
            if len(player2_ships) == 0 and len(player1_ships) == 0:
                Player1.has_won()
                Player2.has_won()
                print ("Both sides have been completely wiped out.")
            elif len(player2_ships) == 0:
                print (Player2.username + "'s fleet has been destroyed.")
                Player1.has_won()
                Player2.has_lost()
            else:
                print (Player1.username + "'s fleet has been destroyed.")
                Player2.has_won()
                Player1.has_lost()
            for ship in player1_ships:
                player1_progress_board[ship[0]][ship[1]] = "@"
            for ship in player2_ships:
                player2_progress_board[ship[0]][ship[1]] = "@"     

        elif turn == 25:
            print ("Game Over")
            for ship in player1_ships:
                player1_progress_board[ship[0]][ship[1]] = "@"
            for ship in player2_ships:
                player2_progress_board[ship[0]][ship[1]] = "@"            
            print ("I can't believe you both couldn't find each others' battleships!")
        else:
            print ("--------------\nTurn", turn+1)

        print("--------------\n" + Player1.username + "'s Board")
        for row in player1_progress_board:
            print (" ".join(row))
        print("\n")

        print("--------------\n" + Player2.username + "'s Board")
        for row in player2_progress_board:
            print (" ".join(row))
        print("\n")

        if len(player2_ships) == 0 or len(player1_ships) == 0 or turn == 25:
            break
        
class Player:

    def __init__(self, username):
        self.username = username

        #Statistics
        self.wins = 0
        self.loses = 0
        self.hits = 0
        self.misses = 0

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