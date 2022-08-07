"""
Sudoku Generator
© Atomic Sorcerer 2022
"""

from exceptions import ZeroEntropyError

import random


class Tile:
    def __init__(self, x_coord, y_coord, length=9):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.length = length
        self.highlighted = False

        # "value" is the same as superposition,
        # and it is generally assumed that anything can have multiple values
        self.value = [i + 1 for i in range(length)]

    def __repr__(self) -> str:
        if len(self.value) == self.length:
            return "Full"
        elif len(self.value) == 1:
            return f"{'|' if self.highlighted else ''}{self.value[0]}{'|' if self.highlighted else ''}"
        else:
            return f"({self.value})"

    def get_entropy(self) -> int:
        if len(self.value) < 1:
            raise ZeroEntropyError("Entropy Can't Be 0")

        return len(self.value)

    def random_collapse(self, amount=1) -> list[int]:
        for _ in range(amount):
            if self.get_entropy() <= 1:
                break

            collapse_position = random.randint(0, self.get_entropy() - 1)

            self.value.pop(collapse_position)

        return self.value

    def random_collapse_full(self) -> list[int]:
        self.random_collapse(amount=self.length)

        return self.value

    def collapse_option(self, *args) -> list[int]:
        for i in args:
            try:
                self.value.remove(i)
            except:
                pass

        return self.value

    def change_value(self, new_value) -> list[int]:
        if isinstance(new_value, list) and len(new_value) <= self.length:
            self.value = new_value

        return self.value
