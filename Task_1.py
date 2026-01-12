# n-queens problem
import random


def is_safe(board, row, col):
    size = len(board)
    
    # Checking the same column above the current row (starting at the current row)
    # No need to check below, since we're placing queens 1 row at a time.
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonals
    i = row - 1  # Moving upwards
    j = col - 1  # Moving to the left
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
    
    # Check upper right diagonals
    i = row - 1  # Moving upwards
    j = col + 1  # Moving to the right here
    while i >= 0 and j < size:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
    
    # No need to check below the current row, since again, we're placing queens 1 row at a time.
    # At this point, we've ensured that the queen is safe in this position.
    return True

# Visualize the board.
def printBoard(board):
    for row in board:
        print(row)

# Generate a random order of the columns for a given row.
# This is where the randomness is applied in my implementation.
# The order in which I'm attempting to place a queen is random for every row.
def generate_random_column_order(no_of_cols):
    return random.sample(range(no_of_cols), no_of_cols)

def nQueensLasVegas(size: int) -> tuple[bool, list[list[int]]]:
    board = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        col_order = generate_random_column_order(size)
        print(f"Column order for row {i}: {col_order}")
        row_success = False
        for col in col_order:
            print(f"Trying Col: {col} on row: {i}")
            if is_safe(board, i, col):
                print(f"Col: {col} on row: {i} is safe")
                board[i][col] = 1
                row_success = True
                break
        if not row_success:
            return False, board
    return True, board

# Need to ask the user to input the board size (it's a square board)
board_size = input("Enter board size: ")
while not board_size.isnumeric() or int(board_size) <= 3:
    # Input validation, ensure it's a number
    board_size = input("Enter a valid (number > 3) board size: ")
approach = input("Select an approach (1 -> Las Vegas, 2 -> Backtracking): ")
while not approach == "1" and not approach == "2":
    approach = input("Select a valid approach (1 -> Las Vegas, 2 -> Backtracking): ")

success, board = nQueensLasVegas(int(board_size))

print(f"Success: {success}")
printBoard(board)


def calculate_success_rate(times:int) -> float:
    successful_tries = 0
    for i in range(times):
        successful_tries, _ = nQueensLasVegas(5)
        if successful_tries:
            successful_tries += 1
    
    return successful_tries / times

print(calculate_success_rate(10000))