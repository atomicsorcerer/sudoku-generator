"""
Sudoku Generator
© Atomic Sorcerer 2022
"""
from lib.utils import generate_board

import sys

arg_iterations = 1000

try:
    arg_iterations = int(sys.argv[1])
except IndexError:
    pass


class ProgressBar:
    def __init__(self, iterations, length=20):
        self.iterations = iterations
        self.length = length
        self.tracker = 0
        self.count = 0

    def progress(self) -> None:
        self.tracker += 1

        if self.tracker % (self.iterations / self.length) == 0:
            self.count += 1

        print("\r", end="")
        print(
            f"{str(self.tracker)}/{str(self.iterations)} - [{'=' * self.count}{'*' * (self.length - self.count)}]",
            end="",
        )


def run_test_series(iterations_to_complete=100) -> tuple[float, int, list[str]]:
    progress_bar = ProgressBar(iterations=iterations_to_complete)
    error_count = 0
    issues = []

    for i in range(iterations_to_complete):
        try:
            generate_board(show_process=False, print_final_result=False)
        except Exception as e:
            error_count += 1
            issues.append(e.__class__.__name__)

        progress_bar.progress()

    return error_count / iterations_to_complete, error_count, issues


error_rate = run_test_series(arg_iterations)

print("\n\n" + "Error Rate: " + str(round(error_rate[0] * 100, 4)) + "%")
print(f"An error was found {error_rate[1]} times.")
print(f"Error(s) found: { list(set(error_rate[2])) }")
