"""
Sudoku Generator
© Atomic Sorcerer 2022
"""

from lib import generate_board

import sys


show_build_process = False

try:
    if sys.argv[1] == "show_process":
        show_build_process = True
except IndexError:
    pass

if __name__ == "__main__":
    finished_board = generate_board(show_process=show_build_process)

    print(f"Iteration Amount: {str(finished_board[1])}")
    print(f"Attempts to create board: {str(finished_board[2])}")
