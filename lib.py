"""
Sudoku Generator
© Atomic Sorcerer 2022
"""

from board import Board
from exceptions import InvalidBoardError


def check_if_duplicates(list_of_elems) -> tuple[bool, list]:
    duplicates_indexes = []
    for z, elem in enumerate(list_of_elems):
        if list_of_elems.count(elem) == 2:
            duplicates_indexes.append(z)
        if elem.get_entropy() != 1:
            duplicates_indexes.append(z)

    if len(duplicates_indexes) > 0:
        return True, duplicates_indexes

    return False, []


def check_if_board_is_valid(board) -> bool:
    valid_list = []

    for x in range(board.rows):
        valid_list.append(check_if_duplicates(board.tiles[x])[0])

    for x in range(board.columns):
        valid_list.append(check_if_duplicates([z[x] for z in board.tiles])[0])

    for x in valid_list:
        if x:
            return False

    return True


def print_board(board, add_border=False) -> None:
    if add_border:
        print("--------------------")

    for x in board.tiles:
        print(x)

    if add_border:
        print("--------------------")


def generate_board(
    show_process=False, print_final_result=True, generation_attempt_current_iteration=1
) -> tuple[Board, int, int]:
    board = Board()

    for i in range(board.rows * board.columns):
        if board.completed:
            if not check_if_board_is_valid(board):
                raise InvalidBoardError("Board is not valid.")

            if print_final_result:
                print_board(board)

            return board, i - 1, generation_attempt_current_iteration

        if show_process:
            print(f"{i} ---")
            print_board(board)
            print(f"{i} ---")

        try:
            board.collapse_random_tile()
        except IndexError:
            return generate_board(
                show_process=show_process,
                print_final_result=print_final_result,
                generation_attempt_current_iteration=generation_attempt_current_iteration
                + 1,
            )
