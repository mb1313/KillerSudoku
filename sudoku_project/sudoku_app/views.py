from django.shortcuts import render
from .puzzle_generator import sudoku_sol, sudoku_puzzle
import json

def sudoku(request):
    solution = json.dumps(sudoku_sol.tolist())
    return render(request, 'sudoku.html', {'sudoku_grid': sudoku_puzzle, 'completed_sudoku': solution})
