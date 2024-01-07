from django.shortcuts import render
from .puzzle_generator import sudoku_sol, sudoku_puzzle

def sudoku(request):
    return render(request, 'sudoku.html', {'sudoku_grid': sudoku_puzzle, 'completed_sudoku': sudoku_sol})
