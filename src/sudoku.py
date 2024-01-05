import numpy as np

grid = [[set([1, 2, 3, 4, 5, 6, 7, 8, 9]) for _ in range(9)] for _ in range(9)]
grid = np.array(grid)
easyPuzzle = [[4, 9, 7, 3, 0, 0, 5, 0, 0],
                [1, 0, 0, 9, 0, 8, 0, 3, 7],
                [5, 0, 3, 6, 7, 4, 0, 0, 0],
                [0, 7, 0, 1, 9, 0, 2, 0, 3],
                [0, 0, 1, 2, 4, 0, 0, 6, 0],
                [2, 0, 0, 0, 0, 0, 7, 9, 0],
                [3, 0, 4, 7, 0, 0, 0, 2, 0],
                [7, 6, 0, 0, 3, 9, 0, 0, 0],
                [0, 1, 9, 0, 0, 0, 3, 0, 0]]

hardPuzzle = [[0, 0, 0, 0, 0, 0, 8, 0, 0],
                [2, 1, 0, 3, 0, 0, 0, 0, 0],
                [7, 0, 3, 2, 4, 0, 0, 0, 0],
                [0, 6, 0, 4, 5, 0, 0, 0, 8],
                [0, 8, 5, 0, 0, 6, 0, 0, 9],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 2, 0, 0, 0, 4],
                [6, 0, 0, 0, 0, 3, 0, 5, 0],
                [0, 0, 0, 0, 0, 0, 6, 1, 0]]

def print_grid(grid):
    horizontal_line = '+-------+-------+-------+'

    for i in range(9):
        if i % 3 == 0:
            print(horizontal_line)

        for j in range(9):
            print('|', end=' ')

            cell = grid[i][j]
            for val in range(1, 10):
                if val in cell:
                    print(val, end='')
                else:
                    print(' ', end='')

            if j == 8:
                print('|')

    print(horizontal_line)

def print_solution(grid):
    horizontal_line = '+---+---+---+'

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print(horizontal_line)

        for j in range(9):
            if j % 3 == 0:
                print('|', end=' ')

            cell = grid[i][j]
            if len(cell) == 1:
                print(list(cell)[0], end=' ')
            else:
                print('.', end=' ')

            if j == 8:
                print('|')

    print(horizontal_line)

def fill_in_given_cells(grid, puzzle):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (puzzle[i][j] != 0):
                grid[i][j] = set([puzzle[i][j]])

def count_sets(arr, set):
    count = 0
    for cell in arr:
        if (len(cell - set) == 0):
            count += 1
    return count

def row_solver(row, cell, index):
    tmp = cell
    for j in range(9):
        if j != index:
            tmp = tmp - row[j]
    if len(tmp) == 1:
        row[index] = tmp

def col_solver(col, cell, index):
    tmp = cell
    for j in range(9):
        if j != index:
            tmp = tmp - col[j]
    if len(tmp) == 1:
        col[index] = tmp

def square_solver(square, cell, i, j):
    tmp = cell
    for r in range(3):
        for c in range(3):
            if r != i or c != j:
                tmp = tmp - square[r][c]
    
    if len(tmp) == 1:
        square[i][j] = tmp

def singlesSolver(grid, count):
    for i in range(9):
        for j in range(9):
            cell = grid[i][j]
            count += 1

            if (len(cell) == 1):
                # print("Found value ", cell, " in row ", i+1)
                for k in range(9):
                    if k != j:
                        count += 1
                        grid[i][k] = grid[i][k] - cell

                for k in range(9):
                    if k != i:
                        count += 1
                        grid[k][j] = grid[k][j] - cell
                
                square = grid[(i//3)*3: (i//3)*3 + 3, (j//3)*3: (j//3)*3 + 3]
                for r in range(3):
                    for c in range(3):
                        if square[r][c] != cell:
                            count += 1
                            square[r][c] = square[r][c] - cell
            
            elif len(cell) != 9:
                if (count_sets(grid[i], cell) == len(cell)):
                    print(i, j)
                    for k in range(9):
                        if (len(grid[i][k] - cell) > 0):
                            grid[i][k] = grid[i][k] - cell
                if (count_sets(grid[:, j], cell) == len(cell)):
                    print(i, j)
                    for k in range(9):
                        if (len(grid[k][j] - cell) > 0):
                            grid[k][j] = grid[k][j] - cell
                if (count_sets(grid[(i//3)*3: (i//3)*3 + 3, (j//3)*3: (j//3)*3 + 3], cell) == len(cell)):
                    for element in grid[(i//3)*3: (i//3)*3 + 3, (j//3)*3: (j//3)*3 + 3]:
                        if (len(element - cell) > 0):
                            element = element - cell
            
            if len(cell) > 1:
                col_solver(grid[:, j], cell, i)
                row_solver(grid[i], cell, j)
                square_solver(grid[(i//3)*3: (i//3)*3 + 3, (j//3)*3: (j//3)*3 + 3], cell, i % 3, j % 3)

    return count


fill_in_given_cells(grid=grid, puzzle=hardPuzzle)
print_grid(grid=grid)
iteration = 1
count = 0

while (any(len(grid[row][col]) > 1 for row in range(9) for col in range(9))):
    print("Iteration: ", iteration, "\n")
    beforeGrid = np.copy(grid)
    count = singlesSolver(grid=grid, count=count)

    print_grid(grid=grid)
    print(count)
    if (np.equal(beforeGrid, grid).all()):
        print("IMPOSSIBLE!!\n")
        break
    iteration += 1

print_solution(grid)