# n-queens problem
import random
import sys


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
    initialized_board = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        col_order = generate_random_column_order(size)
        print(f"Column order for row {i}: {col_order}")
        row_success = False
        for col in col_order:
            print(f"Trying Col: {col} on row: {i}")
            if is_safe(initialized_board, i, col):
                print(f"Col: {col} on row: {i} is safe")
                initialized_board[i][col] = 1
                row_success = True
                break
        if not row_success:
            return False, initialized_board
    return True, initialized_board

def nQueensBacktracking(size:int) -> tuple[bool, list[list[int]]]:
    board = [[0 for _ in range(size)] for _ in range(size)]
    
    def place_queen(current_board, row) :
        # This is the base case, when this is true, it means every
        # queen has been successfully placed.
        if row == size:
            return True
        
        # Attempt to place a queen in each column
        for column in range(size):
            if is_safe(current_board, row, column):
                # If it's safe, place a queen in this position
                current_board[row][column] = 1
                
                # If the next queen is placed, we recursively move to the next rows.
                if place_queen(current_board, row + 1) :
                    return True
                
                # If not, we need to backtrack.
                current_board[row][column] = 0
            
        return False
     
    queens_placed_successfully = place_queen(board, 0)
    
    return queens_placed_successfully, board




approach = input("Select an approach (1 -> Las Vegas, 2 -> Backtracking) or 3 -> Exit: ")
while not approach == "1" and not approach == "2" and not approach == "3":
    approach = input("Select a valid approach (1 -> Las Vegas, 2 -> Backtracking) or 3 -> Exit: ")
    
# Exit early if the user has selected to do so.
if approach == "3":
    print("You've selected to exit. Exiting...")
    sys.exit(0)

# Need to ask the user to input the board size (it's a square board)
board_size = input("Enter board size: ")
while not board_size.isnumeric() or int(board_size) <= 3:
    # Input validation, ensure it's a number
    board_size = input("Enter a valid (number > 3) board size: ")
    
if approach == "1":
    success, board = nQueensLasVegas(int(board_size))
    print(f"Success: {success}")
    printBoard(board)
elif approach == "2":
    success, board = nQueensBacktracking(int(board_size))
    print(f"Success: {success}")
    printBoard(board)



def nQueensBacktrackingVersion2(size: int, startingPosition: tuple[int, int]) -> tuple[bool, list[list[int]]]:
 initialized_board = [[0 for _ in range(size)] for _ in range(size)]
 completed_row, completed_col = startingPosition
 
 # Validate that the starting position is valid (within the board)
 if not (0 <= completed_row < size and 0 <= completed_col < size):
     print("Invalid starting position, you've placed the queen outside the board.")
     return False, initialized_board
 
 initialized_board[completed_row][completed_col] = 1
 
 def place_queen(current_board, row):
     # This is the base case, when this is true, it means every
     # queen has been successfully placed.
     if row == size:
         return True
     
     # We want to skip the row where a queen has already been placed (by the user).
     if row == completed_row:
         return place_queen(current_board, row + 1)
     
     # Attempt to place a queen in each column
     for column in range(size):
         if is_safe(current_board, row, column):
             # If it's safe, place a queen in this position
             current_board[row][column] = 1
             
             # If the next queen is placed, we recursively move to the next rows.
             if place_queen(current_board, row + 1):
                 return True
             
             # If not, we need to backtrack.
             current_board[row][column] = 0
     
     return False
 queens_placed_successfully = place_queen(initialized_board, 0)
 
 return queens_placed_successfully, initialized_board


# success, board = nQueensBacktrackingVersion2(6, (7,3))
# printBoard(board)

def calculate_success_rate(times: int):
    successful_tries_las_vegas, successful_tries_backtracking = 0, 0
    for i in range(times):
        successful_try_las_vegas, _ = nQueensLasVegas(5)
        successful_try_backtracking, _ = nQueensBacktracking(5)
        if successful_try_las_vegas:
            successful_tries_las_vegas += 1
        if successful_try_backtracking:
            successful_tries_backtracking += 1
    
    print(
        f"Successful tries for the Las Vegas approach, after {times} iterations: {successful_tries_las_vegas / times}")
    print(
        f"Successful tries for the Backtracking approach, after {times} iterations: {successful_tries_backtracking / times}")

