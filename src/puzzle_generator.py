import random
import numpy as np
from sudoku import solve_puzzle
def is_valid(grid, row, col, num):
    # Check if the current number is already in the row
    if num in grid[row]:
        return False
    
    # Check if the current number is already in the column
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # Check if the current number is already in the 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def solve_sudoku(grid, values):
    rows = range(9)
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                random.shuffle(values)
                for val in values:
                    if is_valid(grid, row, col, val):
                        grid[row][col] = val
                        if solve_sudoku(grid, values):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_sudoku():
    # Create an empty grid
    grid = [[0 for _ in range(9)] for _ in range(9)]
    vals = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    nums = list(range(1, 10))
    random.shuffle(nums)
    solve_sudoku(grid, vals)
    grid = np.array(grid)
    for i in range(9):
        grid[grid == vals[i]] = nums[i]
    return grid

def rid_cells(grid, difficulty):
    missing = 45
    print(difficulty)
    if (difficulty == 'easy'):
        missing = missing + (int(random.random() - 0.5 * 10))
    if (difficulty == 'med'):
        missing = missing + 5 + int(random.random() / 2 * 10)
    if (difficulty == 'hard'):
        missing = missing + 7 + int(random.random() / 2 * 10)
    if (difficulty == 'expert'):
        missing = missing + 12 + int(random.random() / 2 * 10)
    k = 0
    print("missing", missing)
    while k < missing:
        i = int(round(random.random() * 8))
        j = int(round(random.random() * 8))
        if (grid[i][j] == 0):
            k -= 1
        grid[i][j] = 0
        k += 1

grid = generate_sudoku()
print(grid)
subs = np.copy(grid)
diffs = ['easy', 'med', 'hard', 'expert']
index = 2
print("diff", diffs[index])
rid_cells(subs, diffs[index])
tries = 1
hard = index > 1
while (not solve_puzzle(subs, hard)[0]):
    print(subs)
    subs = np.copy(grid)
    rid_cells(subs, diffs[index])
    tries += 1
print(subs)
print("Puzzles tried: ", tries)
print(np.count_nonzero(subs))