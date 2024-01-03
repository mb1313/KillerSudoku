import numpy as np

grid = [[str(123456789) for _ in range(9)] for _ in range(9)]
grid = np.array(grid)
easyPuzzle = [['4', '9', '7', '3', '0', '0', '5', '0', '0'],
                ['1', '0', '0', '9', '0', '8', '0', '3', '7'],
                ['5', '0', '3', '6', '7', '4', '0', '0', '0'],
                ['0', '7', '0', '1', '9', '0', '2', '0', '3'],
                ['0', '0', '1', '2', '4', '0', '0', '6', '0'],
                ['2', '0', '0', '0', '0', '0', '7', '9', '0'],
                ['3', '0', '4', '7', '0', '0', '0', '2', '0'],
                ['7', '6', '0', '0', '3', '9', '0', '0', '0'],
                ['0', '1', '9', '0', '0', '0', '3', '0', '0']]

def print_grid(grid):
    for row in grid:
        for num in row:
            print(f"| {num} |", end=" ")
        print("|")
        print()
    print("-----------")

def fill_in_given_cells(grid, puzzle):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (puzzle[i][j] != '0'):
                grid[i][j] = puzzle[i][j]

def rowSolver(grid):
    for i in range(9):
        for j in range(9):
            cell = grid[i][j]
            if (len(cell) == 1):
                value = cell[0]
                print("Found value ", value, " in row ", i+1)
                for k in range(9):
                    if k != j:
                        grid[i][k] = grid[i][k].replace(value, "")

def colSolver(grid):
    for j in range(9):
        for i in range(9):
            cell = grid[i][j]
            if (len(cell) == 1):
                value = cell[0]
                for k in range(9):
                    if k != i:
                        grid[k][j] = grid[k][j].replace(value, "")

def squareSolver(grid):
    for row in range(3):
        for col in range(3):
            square = grid[row*3 : (row*3)+3, col*3 : (col*3)+3]
            
            for r in range(3):
                for c in range(3):
                    cell = square[r][c]
                    if (len(cell) == 1):
                        value = cell[0]
                        for r2 in range(3):
                            for c2 in range(3):
                                if r2 != r or c2 != c:
                                    square[r2][c2] = square[r2][c2].replace(value, "")

fill_in_given_cells(grid=grid, puzzle=easyPuzzle)
print_grid(grid=grid)
iteration = 1
while (any(len(grid[row][col]) > 1 for row in range(9) for col in range(9))):
    print("Iteration: ", iteration, "\n")
    rowSolver(grid=grid)
    colSolver(grid=grid)
    squareSolver(grid=grid)
    print_grid(grid=grid)
    iteration += 1