from Position import Position


class Tictactoe:
    ERROR_WRONG_TURN = "It is not your turn!"
    ERROR_POSITION_TAKEN = "Position is already taken"
    ERROR_POSITION_OUTSIDE_BOARD = "Choose a position between (1,1) and (3,3)"
    ERROR_MATCH_FINISHED = "This match has finished"

    # Positions
    NUMBER_OF_AVAILABLE_POSITIONS = 9
    UPPER_LEFT = Position(1, 1)
    UPPER_CENTER = Position(1, 2)
    UPPER_RIGHT = Position(1, 3)
    MIDDLE_LEFT = Position(2, 1)
    MIDDLE_CENTER = Position(2, 2)
    MIDDLE_RIGHT = Position(2, 3)
    BOTTOM_LEFT = Position(3, 1)
    BOTTOM_CENTER = Position(3, 2)
    BOTTOM_RIGHT = Position(3, 3)

    def __init__(self):
        self._player_x_taken_positions = set()
        self._player_o_taken_positions = set()
        self._winning_position_combinations = [{self.UPPER_LEFT, self.UPPER_CENTER, self.UPPER_RIGHT},
                                               {self.MIDDLE_LEFT, self.MIDDLE_CENTER, self.MIDDLE_RIGHT},
                                               {self.BOTTOM_LEFT, self.BOTTOM_CENTER, self.BOTTOM_RIGHT},
                                               {self.UPPER_LEFT, self.MIDDLE_LEFT, self.BOTTOM_LEFT},
                                               {self.UPPER_CENTER, self.MIDDLE_CENTER, self.BOTTOM_CENTER},
                                               {self.UPPER_RIGHT, self.MIDDLE_RIGHT, self.BOTTOM_RIGHT},
                                               {self.UPPER_LEFT, self.MIDDLE_CENTER, self.BOTTOM_RIGHT},
                                               {self.UPPER_RIGHT, self.MIDDLE_CENTER, self.BOTTOM_LEFT}]
        self._player_x_turn = True

    def board_is_empty(self):
        return len(self._player_x_taken_positions) == 0

    def board_is_full(self):
        return len(self._player_x_taken_positions) + len(
            self._player_o_taken_positions) == Tictactoe.NUMBER_OF_AVAILABLE_POSITIONS

    def position_is_empty(self, position):
        return (position not in self._player_x_taken_positions) and (position not in self._player_o_taken_positions)

    def is_x_at(self, position):
        return self.is_player_at(position, self.player_x())

    def is_o_at(self, position):
        return self.is_player_at(position, self.player_o())

    def is_player_at(self, position, a_player):
        return position in self.positions_marked_by(a_player)

    def x_takes_position(self, position):
        self.player_takes_position(position, self.player_x())

    def o_takes_position(self, position):
        self.player_takes_position(position, self.player_o())

    def player_takes_position(self, position, a_player):
        self.assert_is_turn_of(a_player)
        self.assert_position_is_not_taken(position)
        self.assert_position_is_on_board(position)
        self.assert_is_not_over()

        self.positions_marked_by(a_player).add(position)
        self.switch_turn()

    def assert_position_is_not_taken(self, position):
        if not self.position_is_empty(position):
            raise Exception(self.ERROR_POSITION_TAKEN)

    def assert_position_is_on_board(self, position):
        if self.is_invalid_position(position):
            raise Exception(self.ERROR_POSITION_OUTSIDE_BOARD)

    def assert_is_not_over(self):
        if self.is_over():
            raise Exception(self.ERROR_MATCH_FINISHED)

    def is_over(self):
        return self.has_player_x_won() or self.has_player_o_won() or self.is_tied()

    def is_tied(self):
        return self.board_is_full() and not (self.has_player_x_won() or self.has_player_o_won())

    def assert_is_turn_of(self, a_player):
        if not self.is_turn_of_player(a_player):
            raise Exception(self.ERROR_WRONG_TURN)

    def is_invalid_position(self, position):
        return not ((1 <= position.row() <= 3) and (1 <= position.column() <= 3))

    def is_turn_of_player_x(self):
        return self.is_turn_of_player(self.player_x())

    def is_turn_of_player_o(self):
        return self.is_turn_of_player(self.player_o())

    def is_turn_of_player(self, a_player):
        if a_player == self.player_x():
            return self.is_player_x_turn()
        return self.is_player_o_turn()

    def is_player_x_turn(self):
        return self._player_x_turn

    def is_player_o_turn(self):
        return not self.is_player_x_turn()

    def switch_turn(self):
        self._player_x_turn = not self.is_player_x_turn()

    def has_player_x_won(self):
        return self.has_player_won(self.player_x())

    def has_player_o_won(self):
        return self.has_player_won(self.player_o())

    def has_player_won(self, a_player):
        for combination in self._winning_position_combinations:
            if combination.issubset(self.positions_marked_by(a_player)):
                return True
        return False

    def positions_marked_by(self, a_player):
        if a_player == self.player_x():
            return self._player_x_taken_positions
        return self._player_o_taken_positions

    def player_x(self):
        return "X"

    def player_o(self):
        return "O"
