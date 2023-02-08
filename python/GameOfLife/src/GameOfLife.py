# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

VIVA = True
MUERTA = False


class GameOfLife:

    def __init__(self, alive_cells_positions):
        grid = self.create_empty_grid()

        for (x, y) in alive_cells_positions:
            grid[x - 1][y - 1] = VIVA

        self._grid = grid

    def create_empty_grid(self):
        grid = []
        for row_index in range(5):
            column = []
            for column_index in range(5):
                column.append(MUERTA)
            grid.append(column)
        return grid

    def get_row(self, row):
        return self._grid[row - 1]

    def is_cell_alive_in_position(self, position):
        row = self.get_row(position[0])
        return row[position[1] - 1]

    def count_live_neighbours(self,position):
        live_neighbours = 0
        neighbours_list = self.get_neighbours(position)

        for neighbour in neighbours_list:
            if self.is_cell_alive_in_position(neighbour):
                live_neighbours += 1

        return live_neighbours

    def will_cell_die_by_underpopulation(self, position):
        if self.is_cell_alive_in_position(position):
            if self.count_live_neighbours(position) < 2:
                return True
            return False

    def will_cell_live_on_to_the_next_generation(self, position):
        if 2 <= self.count_live_neighbours(position) <= 3:
            return True
        return False

    def will_cell_die_by_overpopulation(self, position):
        if self.count_live_neighbours(position) > 3:
            return True
        return False

    def will_cell_become_alive(self, position):
        if not self.is_cell_alive_in_position(position):
            if self.count_live_neighbours(position) == 3:
                return True
            return False

    def get_neighbours(self, position):
        list_of_neighbours_positions = []

        (row_number, column_number) = position
        number_of_rows = range(row_number - 1, row_number + 2)
        number_of_columns = range(column_number - 1, column_number + 2)
        for row in number_of_rows:
            for column in number_of_columns:
                if (row, column) != position:
                    list_of_neighbours_positions.append((row,column))

        return list_of_neighbours_positions

    def kill_cell(self, position):
        if self.is_cell_alive_in_position(position):
            self._grid[position[0]-1][position[1]-1]=MUERTA
        return

    def generate_cell(self, position):
        if not self.is_cell_alive_in_position(position):
            self._grid[position[0]-1][position[1]-1]=VIVA
        return

    # def pass_on_to_next_generation(self):
    #     next_generation = set()
    #
    #     for position in self.
    #     if self.will_cell_die_by_underpopulation()
    #     return next_generation
    #

class Position:
    def __init__(self, ):
        pass


class Cell:
    def __init__(self, position_row, position_column):
        self._position_row = position_row
        self._position_column = position_column
