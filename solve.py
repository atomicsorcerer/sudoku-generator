"""
Sudoku Generator
© Atomic Sorcerer 2022
"""

from lib.utils import complete_board, print_board
from board.board import Board

import sys


show_build_process = False

do_highlight = False

try:
    if sys.argv.count("--show_process") > 0:
        show_build_process = True
except IndexError:
    pass

try:
    if sys.argv.count("--do_highlight") > 0:
        do_highlight = True
except IndexError:
    pass

indexes_to_collapse = []


def add_a_coord():
    print("---")
    x = int(input("Enter the 'x' coordinate: "))
    y = int(input("Enter the 'y' coordinate: "))
    value = int(input("Enter value to collapse tile to: "))
    coords = (x, y)

    indexes_to_collapse.append((coords, value))

    add_more = input("Do you want to collapse more tiles (y, N): ")

    if add_more == "y":
        add_a_coord()


if __name__ == "__main__":
    add_a_coord()

    board = Board()

    for i in indexes_to_collapse:
        board.collapse_specific_tile(i[0][0], i[0][1], i[1], do_highlight=do_highlight)

    new_board = complete_board(board, show_process=show_build_process)

    print(f"Iteration Amount: {str(new_board[1])}")
    print(f"Attempts to create board: {str(new_board[2])}")
