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

expertPuzzle = [[0, 7, 8, 5, 0, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 7, 8, 0, 0],
                [0, 0, 0, 1, 9, 0, 0, 0, 0],
                [0, 0, 7, 0, 0, 0, 2, 9, 0],
                [0, 9, 0, 0, 6, 1, 0, 4, 0],
                [0, 0, 0, 0, 0, 4, 0, 0, 0],
                [3, 0, 6, 0, 0, 2, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 4],
                [0, 0, 0, 0, 0, 0, 5, 0, 0]]

masterPuzzle = [[0, 0, 3, 0, 0, 0, 0, 0, 2],
                [0, 8, 0, 0, 5, 0, 0, 0, 0],
                [7, 0, 0, 8, 0, 0, 0, 4, 9],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 6, 0, 0, 3, 0, 0, 0],
                [9, 0, 0, 5, 0, 0, 0, 7, 8],
                [0, 0, 9, 0, 6, 0, 0, 1, 4],
                [0, 0, 0, 4, 0, 0, 2, 0, 0],
                [1, 0, 0, 0, 0, 0, 5, 0, 0]]

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

def find_hidden_sets(arr):
    occurrences = {}
    for cell in arr:
        # if len(cell) > 1:
            for value in cell:
                if value in occurrences:
                    occurrences[value].append(cell)
                else:
                    occurrences[value] = [cell]
        
    hidden_sets = {}
    for value, cells in occurrences.items():
        occurrences_count = len(cells)
        if 1 < occurrences_count < 10:
            if occurrences_count not in hidden_sets:
                hidden_sets[occurrences_count] = {}
            if value not in hidden_sets[occurrences_count]:
                hidden_sets[occurrences_count][value] = cells
            
    for occurrences_count, sets in hidden_sets.items():
        if len(sets.values()) == occurrences_count:
            hidden = set(sets.keys())
            resident = []
            match = True
            for val in sets.values():
                if len(resident) == 0:
                    resident = val
                elif resident != val:
                    match = False
            if match:
                for j in range(9):
                    if len(hidden - arr[j]) == 0:
                        arr[j] = hidden
                        print(f"Hidden set of {occurrences_count} with value {hidden} in row {i} at cells: {sets.values()}")

def exclusive_square_row(grid, count):
    for r in range(9):
        for c in range(3):
            square = grid[(r//3)*3: (r//3)*3 + 3, (c)*3: (c)*3 + 3].flatten()
            subsection = np.delete(square, [r%3 * 3, r%3 * 3 + 1, r%3 * 3 + 2])
            row = np.delete(grid[r], [c*3, c*3 + 1, c*3 + 2])
            setSquare = set().union(*subsection)
            setRow = set().union(*row)
            diff = set()
            if len(setSquare - setRow) > 0:
                diff.update(setSquare - setRow)
            elif len(setRow - setSquare) > 0:
                diff.update(setRow - setSquare)
            if len(diff) > 0:
                for c2 in range(9):
                    if c2 != c*3 and c2 != c*3+1 and c2 != c*3+2:
                        grid[r][c2] = grid[r][c2] - diff
                        count += 1
                for r2 in range(3):
                    rowIndex = r//3 * 3 + r2
                    if rowIndex != r:
                        grid[rowIndex][c*3] = grid[rowIndex][c*3] - diff
                        grid[rowIndex][c*3+1] = grid[rowIndex][c*3+1] - diff
                        grid[rowIndex][c*3+2] = grid[rowIndex][c*3+2] - diff
                        count += 3
    return count

def exclusive_square_col(grid, count):
    for c in range(9):
        for r in range(3):
            square = grid[(r)*3: (r)*3 + 3, (c//3)*3: (c//3)*3 + 3].flatten()
            subsection = np.delete(square, [c%3, c%3+3, c%3+6])
            col = grid[:, c].flatten()
            col = np.delete(col, [r*3, r*3 + 1, r*3 + 2])
            setSquare = set().union(*subsection)
            setCol = set().union(*col)
            diff = set()
            if len(setSquare - setCol) > 0:
                diff.update(setSquare - setCol)
            elif len(setCol - setSquare) > 0:
                diff.update(setCol - setSquare)
            if len(diff) > 0:
                for r2 in range(9):
                    if r2 != r*3 and r2 != r*3+1 and r2 != r*3+2:
                        grid[r2][c] = grid[r2][c] - diff
                        count += 1
                for c2 in range(3):
                    colIndex = c//3 * 3 + c2
                    if colIndex != c:
                        grid[r*3][colIndex] = grid[r*3][colIndex] - diff
                        grid[r*3+1][colIndex] = grid[r*3+1][colIndex] - diff
                        grid[r*3+2][colIndex] = grid[r*3+2][colIndex] - diff
                        count += 3
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

def singlesSolver(grid, count, hard):
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
            
            elif len(cell) != 9 and hard:
                if (count_sets(grid[i], cell) == len(cell)):
                    for k in range(9):
                        if (len(grid[i][k] - cell) > 0):
                            count += 1
                            grid[i][k] = grid[i][k] - cell
                if (count_sets(grid[:, j], cell) == len(cell)):
                    for k in range(9):
                        if (len(grid[k][j] - cell) > 0):
                            count += 1
                            grid[k][j] = grid[k][j] - cell
                if (count_sets((grid[(i//3)*3: (i//3)*3 + 3, (j//3)*3: (j//3)*3 + 3]).flatten(), cell) == len(cell)):
                    for r in range(3):
                        for c in range(3):
                            element = grid[i//3*3 + r][j//3*3 + c]
                            if (len(element - cell) > 0):
                                count += 1
                                grid[i//3*3 + r][j//3*3 + c] = grid[i//3*3 + r][j//3*3 + c] - cell
                count += 27
                
            
            if len(cell) > 1:
                col_solver(grid[:, j], cell, i)
                row_solver(grid[i], cell, j)
                square_solver(grid[(i//3)*3: (i//3)*3 + 3, (j//3)*3: (j//3)*3 + 3], cell, i % 3, j % 3)
                count += 24

    return count



fill_in_given_cells(grid=grid, puzzle=expertPuzzle)
print_grid(grid=grid)
iteration = 1
count = 0
hard = True

while (any(len(grid[row][col]) > 1 for row in range(9) for col in range(9))):
    print("Iteration: ", iteration, "\n")
    beforeGrid = np.copy(grid)
    count = singlesSolver(grid=grid, count=count, hard=hard)
    
    if hard:
        for i in range(9):
            find_hidden_sets(grid[i])
            find_hidden_sets(grid[:, i])
        
        for i in range(3):
            for j in range(3):
                square = grid[i*3: i*3 +3, j*3: j*3+3]
                square = square.flatten()
                find_hidden_sets(square)

        count = exclusive_square_row(grid, count)
        count = exclusive_square_col(grid, count)
        
    print_grid(grid=grid)
    print(count)
    if (np.equal(beforeGrid, grid).all()):
        print("IMPOSSIBLE!!\n")
        break
    iteration += 1

print_solution(grid)