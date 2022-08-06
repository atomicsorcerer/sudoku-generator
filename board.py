"""
Sudoku Generator
© Atomic Sorcerer 2022
"""

import random

from tile import Tile


class Board:
    def __init__(self, rows=9, columns=9):
        self.rows = rows
        self.columns = columns
        self.tiles = []
        self.completed = False
        self.counter = 0

        # a list of all tiles that have been collapsed to 0 entropy
        # and have effected tiles in its area
        self.collapsed_tiles = []

        for y in range(rows):
            new_row = []
            for x in range(columns):
                new_row.append(Tile(x, y))

            self.tiles.append(new_row)

    def find_new_tile(self) -> tuple[int, int]:
        lowest_entropy_value = 9

        for i in self.tiles:
            for z in i:
                if z.get_entropy() < lowest_entropy_value and z.get_entropy() != 1:
                    lowest_entropy_value = z.get_entropy()

        coords_of_potential_tiles = []

        for i in self.tiles:
            for z in i:
                if z.get_entropy() == lowest_entropy_value:
                    coords_of_potential_tiles.append((z.x_coord, z.y_coord))

        new_tile = coords_of_potential_tiles[
            random.randint(0, len(coords_of_potential_tiles) - 1)
        ]

        return new_tile

    # find a random tile position that has not been used yet
    def find_new_random_tile(self) -> tuple[int, int]:
        new_x_coord = random.randint(0, self.columns - 1)
        new_y_coord = random.randint(0, self.rows - 1)

        for i in self.collapsed_tiles:
            if i == (new_x_coord, new_y_coord):
                return self.find_new_random_tile()

        return new_x_coord, new_y_coord

    # check if a tile has already been fully collapsed and added to the used list
    def tile_already_added_to_used_list(self, x, y) -> bool:
        for i in self.collapsed_tiles:
            if (x, y) == i:
                return True

        return False

    def collapse_rows(self, x, y, new_value) -> None:
        to_collapse_later = []

        for i in self.tiles[y]:
            if i.x_coord == x:
                continue

            new_collapsed_value = self.tiles[y][i.x_coord].collapse_option(new_value)[0]

            if self.tiles[y][i.x_coord].get_entropy() == 1:
                if not self.tile_already_added_to_used_list(i.x_coord, y):
                    self.collapsed_tiles.append((i.x_coord, y))
                    to_collapse_later.append((i.x_coord, y, new_collapsed_value))

        for i in to_collapse_later:
            self.collapse_columns(i[0], i[1], i[2])
            self.collapse_rows(i[0], i[1], i[2])
            self.collapse_groups(i[0], i[1], i[2])

    def collapse_columns(self, x, y, new_value) -> None:
        to_collapse_later = []

        for z, _ in enumerate(self.tiles):
            if z == y:
                continue

            new_collapsed_value = self.tiles[z][x].collapse_option(new_value)[0]

            if self.tiles[z][x].get_entropy() == 1:
                if not self.tile_already_added_to_used_list(x, z):
                    self.collapsed_tiles.append((x, z))
                    to_collapse_later.append((x, z, new_collapsed_value))

        for i in to_collapse_later:
            self.collapse_columns(i[0], i[1], i[2])
            self.collapse_rows(i[0], i[1], i[2])
            self.collapse_groups(i[0], i[1], i[2])

    def collapse_groups(self, x, y, new_value) -> None:
        to_collapse_later = []

        x_start = 0
        y_start = 0

        if x < 3:
            pass
        elif x < 6:
            x_start = 3
        elif x < 9:
            x_start = 6

        if y < 3:
            pass
        elif y < 6:
            y_start = 3
        elif y < 9:
            y_start = 6

        # first row
        for i in range(2):
            new_collapsed_value = self.tiles[y][(x + i + 1) % 3].collapse_option(
                new_value
            )[0]

            current_y_coord = y
            current_x_coord = (x + i + 1) % 3

            if self.tiles[current_y_coord][current_x_coord].get_entropy() == 1:
                if not self.tile_already_added_to_used_list(
                    current_x_coord, current_y_coord
                ):
                    self.collapsed_tiles.append((current_x_coord, current_y_coord))
                    to_collapse_later.append(
                        (current_x_coord, current_y_coord, new_collapsed_value)
                    )

        # second row
        for i in range(3):
            new_collapsed_value = self.tiles[((y + 1) % 3 + y_start)][
                i + x_start
            ].collapse_option(new_value)[0]

            current_y_coord = (y + 1) % 3 + y_start
            current_x_coord = i + x_start

            if self.tiles[current_y_coord][current_x_coord].get_entropy() == 1:
                if not self.tile_already_added_to_used_list(
                    current_x_coord, current_y_coord
                ):
                    self.collapsed_tiles.append((current_x_coord, current_y_coord))
                    to_collapse_later.append(
                        (current_x_coord, current_y_coord, new_collapsed_value)
                    )

        # third row
        for i in range(3):
            new_collapsed_value = self.tiles[((y + 2) % 3 + y_start)][
                i + x_start
            ].collapse_option(new_value)[0]

            current_y_coord = (y + 2) % 3 + y_start
            current_x_coord = i + x_start

            if self.tiles[current_y_coord][current_x_coord].get_entropy() == 1:
                if not self.tile_already_added_to_used_list(
                    current_x_coord, current_y_coord
                ):
                    self.collapsed_tiles.append((current_x_coord, current_y_coord))
                    to_collapse_later.append(
                        (current_x_coord, current_y_coord, new_collapsed_value)
                    )

        for i in to_collapse_later:
            self.collapse_columns(i[0], i[1], i[2])
            self.collapse_rows(i[0], i[1], i[2])
            self.collapse_groups(i[0], i[1], i[2])

    def collapse_random_tile(self) -> tuple[int, int] | None:
        # make sure that there are still tiles to collapse
        if len(self.collapsed_tiles) >= self.rows * self.columns:
            self.completed = True
            return

        rand_x_coord, rand_y_coord = self.find_new_tile()

        # add the used tile coordinates to the list of already used tiles
        self.collapsed_tiles.append((rand_x_coord, rand_y_coord))

        # collapse the given tile to its lowest position
        new_value = self.tiles[rand_y_coord][rand_x_coord].random_collapse_full()[0]

        # collapse all rows
        self.collapse_rows(rand_x_coord, rand_y_coord, new_value)

        # collapse columns
        self.collapse_columns(rand_x_coord, rand_y_coord, new_value)

        # collapse groups
        self.collapse_groups(rand_x_coord, rand_y_coord, new_value)

        return rand_x_coord, rand_y_coord
