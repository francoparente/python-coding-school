class Position:
    def __init__(self, an_x, an_y):
        self._y = an_y
        self._x = an_x

    def __eq__(self, other):
        return self._x == other.x() and self._y == other.y()

    def x(self):
        return self._x

    def y(self):
        return self._y

    def north_position(self):
        return Position(self._x, self._y + 1)

    def south_position(self):
        return Position(self._x, self._y - 1)

    def east_position(self):
        return Position(self._x + 1, self._y)

    def west_position(self):
        return Position(self._x - 1, self._y)
