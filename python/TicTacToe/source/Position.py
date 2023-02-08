class Position:
    def __init__(self, a_row, a_column):
        self._row = a_row
        self._column = a_column

    def __eq__(self, other):
        return other.row() == self._row and other.column() == self._column

    def __hash__(self):
        return hash((self._row, self._column))

    def row(self):
        return self._row

    def column(self):
        return self._column
