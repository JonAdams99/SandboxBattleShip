# Jon Adams
10/19/24

# single player game - AI Perplexity
# 5 X 5 print_board
# single ship
# input row and then the column
# Game over 
#     print message
#     print final board



import random

def create_board():
    return [['O' for _ in range(5)] for _ in range(5)]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def place_ship(board):
    # Randomly decide if the ship is horizontal or vertical
    is_horizontal = random.choice([True, False])
    
    if is_horizontal:
        row = random.randint(0, 4)
        col = random.randint(0, 2)
        for i in range(3):
            board[row][col + i] = 'S'
    else:
        row = random.randint(0, 2)
        col = random.randint(0, 4)
        for i in range(3):
            board[row + i][col] = 'S'

def get_guess():
    while True:
        try:
            row = int(input("Enter row (0-4): "))
            col = int(input("Enter column (0-4): "))
            if 0 <= row <= 4 and 0 <= col <= 4:
                return row, col
            else:
                print("Invalid input. Please enter numbers between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def play_game():
    print("Welcome to Battleship!")
    player_board = create_board()
    computer_board = create_board()
    place_ship(computer_board)
    
    turns = 0
    hits = 0
    
    while hits < 3:
        print("\nYour board:")
        print_board(player_board)
        
        row, col = get_guess()
        
        if computer_board[row][col] == 'S':
            print("Hit!")
            player_board[row][col] = 'X'
            hits += 1
        else:
            print("Miss!")
            player_board[row][col] = '-'
        
        turns += 1
    
    print("\nCongratulations! You sank the battleship!")
    print(f"It took you {turns} turns.")
    print("\nFinal board:")
    print_board(player_board)

if __name__ == "__main__":
    play_game()