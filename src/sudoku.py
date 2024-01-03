grid = [["123456789" for _ in range(9)] for _ in range(9)]
easyPuzzle = [[4, 9, 7, 3, 0, 0, 5, 0, 0],
                [1, 0, 0, 9, 0, 8, 0, 3, 7],
                [5, 0, 3, 6, 7, 4, 0, 0, 0],
                [0, 7, 0, 1, 9, 0, 2, 0, 3],
                [0, 0, 1, 2, 4, 0, 0, 6, 0],
                [2, 0, 0, 0, 0, 0, 7, 9, 0],
                [3, 0, 4, 7, 0, 0, 0, 2, 0],
                [7, 6, 0, 0, 3, 9, 0, 0, 0],
                [0, 1, 9, 0, 0, 0, 3, 0, 0]]

def print_grid(grid):
    for row in grid:
        for num in row:
            print(f"| {num} |", end=" ")
        print("|")
        print()
    print("-----------")

# def rowSolver(row):


print_grid(grid=grid)