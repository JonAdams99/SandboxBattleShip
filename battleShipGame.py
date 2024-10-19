# Jon Adams
10/19/24

# single player game - AI Perplexity
# 5 X 5 print_board
# single ship
# input row and then the column
# Game over 
#     print message
#     print final board

# Change AI to the Real game



import random

def create_board():
    # each player has a board
    return [['-' for _ in range(10)] for _ in range(10)]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def create_ship(board):
    fleet = create_fleet()
    ship = ""
    length = 0
    for i,j in fleet.items():
        ship = i
        length = j
        place_ship(board, ship, length)



def create_fleet():
    fleet = {} #Dictionary for all ships {shipName:[shipLetter, length]}
    # carrier = 5
    # battleship = 4
    # destroyer = 3
    # submarine = 3
    # patrol = 2
    # for i in range(5):
    #OOP Fleet has a # of ships, Each ships has designation and langth
    fleet = {"C":5, "B":4, "D":3, "S":3, "P":2}

    return fleet

def ship_overlap_horz(board, row, col, length):
    flag = True
    for i in range(length):
        if board[row][col + i] != "-":
            flag = False
            break
    return flag

def ship_overlap_vert(board, row, col, length):
    flag = True
    for i in range(length):
        if board[row +i][col] != "-":
            flag = False
            break
    return flag

def place_ship(board, shipLetter, shipLength):
    length = shipLength
    letter = shipLetter
    row = 0
    col = 0
    flag = bool
    count = 0
    # Randomly decide if the ship is horizontal or vertical
    is_horizontal = random.choice([True, False])
    
    if is_horizontal:

        row = random.randint(0, 9)
        col = random.randint(0, 9-length)
        flag = ship_overlap_horz(board, row, col, length)
        if flag == True:
            for i in range(length):
                board[row][col + i] = letter
        else:
            place_ship(board, shipLetter, shipLength)
            
    else:        
        row = random.randint(0, 9-length)
        col = random.randint(0, 9)
        ship_overlap_vert(board, row, col, length)
        if flag == True:
            for i in range(length):
                board[row + i][col] = letter
        else:
            place_ship(board, shipLetter, shipLength)
        

def get_guess():
    while True:
        try:
            row = int(input("Enter row (0-9): " ))
            col = int(input("Enter column (0-9): "))
            if 0 <= row <= 9 and 0 <= col <= 9:
                return row, col
            else:
                print("Invalid input. Please enter numbers between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def play_game():
    print("Welcome to Battleship!")
    player_board = create_board()
    computer_board = create_board()
    create_ship(computer_board)
    
    turns = 0
    hits = 0
    
    while hits < 17:
        print("\nYour board:")
        print_board(player_board)
        print_board(computer_board)
        
        row, col = get_guess()
        letter = computer_board[row][col]
        
        if letter !='-':
            print("Hit!")
            player_board[row][col] = letter
            hits += 1
            
        else:
            print("Miss!")
            player_board[row][col] = 'O'
        
        turns += 1
    
    print("\nCongratulations! You sank the battleship!")
    print(f"It took you {turns} turns.")
    print("\nFinal board:")
    print_board(player_board)

if __name__ == "__main__":
    play_game()