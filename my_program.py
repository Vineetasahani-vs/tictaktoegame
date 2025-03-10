# Initialize board
board = [[" " for _ in range(3)] for _ in range(3)]

# Function to print the board
def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check for a winner
def check_winner(player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if board is full (draw)
def is_draw():
    return all(cell != " " for row in board for cell in row)

# Main game loop
def tic_tac_toe():
    player = "X"
    while True:
        print_board()
        try:
            row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(player):
                    print_board()
                    print(f"Player {player} wins!")
                    break
                if is_draw():
                    print_board()
                    print("It's a draw!")
                    break
                player = "O" if player == "X" else "X"
            else:
                print("Cell already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column between 0-2.")

# Start the game
tic_tac_toe()
