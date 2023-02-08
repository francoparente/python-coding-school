import unittest

from Position import Position
from Tictactoe import Tictactoe


class TictactoeTest(unittest.TestCase):

    def test_board_is_empty_when_game_starts_and_it_is_player_x_turn_and_there_is_no_winner(self):
        a_game = Tictactoe()

        self.assertTrue(a_game.board_is_empty())
        self.assertTrue(a_game.is_turn_of_player_x())
        self.assertFalse(a_game.is_turn_of_player_o())
        self.assertFalse(a_game.has_player_x_won())
        self.assertFalse(a_game.has_player_o_won())

    def test_middle_center_position_is_empty(self):
        a_game = Tictactoe()

        self.assertTrue(a_game.position_is_empty(a_game.MIDDLE_CENTER))

    def test_player_o_cant_start_playing(self):
        a_game = Tictactoe()

        try:
            a_game.o_takes_position(Position(1, 1))
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(a_game.ERROR_WRONG_TURN, str(error))
            self.assertTrue(a_game.position_is_empty(Position(1, 1)))
            self.assertTrue(a_game.is_turn_of_player_x())
            self.assertFalse(a_game.is_turn_of_player_o())

    def test_x_takes_position_2_2_and_then_it_is_player_o_turn(self):
        a_game = Tictactoe()
        a_game.x_takes_position(Position(2, 2))

        self.assertTrue(a_game.is_x_at(Position(2, 2)))
        self.assertTrue(a_game.is_player_o_turn())

    def test_o_takes_position_2_3_and_then_it_is_player_x_turn(self):
        a_game = Tictactoe()
        a_game.x_takes_position(Position(2, 2))
        a_game.o_takes_position(Position(2, 3))

        self.assertTrue(a_game.is_o_at(Position(2, 3)))
        self.assertTrue(a_game.is_player_x_turn())

    def test_player_o_cant_take_a_position_taken_by_player_x(self):
        a_game = Tictactoe()
        a_game.x_takes_position(Position(3, 3))

        try:
            a_game.o_takes_position(Position(3, 3))
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(a_game.ERROR_POSITION_TAKEN, str(error))
            self.assertTrue(a_game.is_x_at(Position(3, 3)))

    def test_player_x_cant_take_a_position_taken_by_player_o(self):
        a_game = Tictactoe()
        a_game.x_takes_position(Position(3, 3))
        a_game.o_takes_position(Position(3, 2))

        try:
            a_game.x_takes_position(Position(3, 2))
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(a_game.ERROR_POSITION_TAKEN, str(error))
            self.assertTrue(a_game.is_x_at(Position(3, 3)))
            self.assertTrue(a_game.is_o_at(Position(3, 2)))
            self.assertFalse(a_game.is_x_at(Position(3, 2)))

    def test_player_x_cant_take_a_position_taken_by_player_x(self):
        a_game = Tictactoe()
        a_game.x_takes_position(Position(3, 3))
        a_game.o_takes_position(Position(3, 2))

        try:
            a_game.x_takes_position(Position(3, 3))
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(a_game.ERROR_POSITION_TAKEN, str(error))
            self.assertTrue(a_game.is_x_at(Position(3, 3)))
            self.assertTrue(a_game.is_o_at(Position(3, 2)))
            self.assertTrue(a_game.is_x_at(Position(3, 3)))

    def test_player_o_cant_take_a_position_taken_by_player_o(self):
        a_game = Tictactoe()
        a_game.x_takes_position(Position(3, 3))
        a_game.o_takes_position(Position(3, 2))
        a_game.x_takes_position(Position(3, 1))

        try:
            a_game.o_takes_position(Position(3, 2))
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(a_game.ERROR_POSITION_TAKEN, str(error))
            self.assertTrue(a_game.is_x_at(Position(3, 3)))
            self.assertTrue(a_game.is_o_at(Position(3, 2)))
            self.assertTrue(a_game.is_x_at(Position(3, 1)))
            self.assertTrue(a_game.is_o_at(Position(3, 2)))

    def test_after_three_turns_board_is_not_empty(self):
        game = Tictactoe()

        game.x_takes_position(Position(2, 2))
        game.o_takes_position(Position(2, 1))
        game.x_takes_position(Position(1, 2))

    def test_player_cant_play_outside_the_board_boundaries_1(self):
        game = Tictactoe()
        try:
            game.x_takes_position(Position(4, 1))
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(game.ERROR_POSITION_OUTSIDE_BOARD, str(error))
            self.assertFalse(game.is_x_at(Position(4, 1)))

    def test_player_cant_play_outside_the_board_boundaries_2(self):
        game = Tictactoe()
        game.x_takes_position(Position(1, 1))
        try:
            game.o_takes_position(Position(0, 2))
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(game.ERROR_POSITION_OUTSIDE_BOARD, str(error))
            self.assertFalse(game.is_x_at(Position(0, 2)))

    def test_player_cant_play_outside_the_board_boundaries_3(self):
        game = Tictactoe()

        try:
            game.x_takes_position(Position(1, 5))
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(game.ERROR_POSITION_OUTSIDE_BOARD, str(error))
            self.assertFalse(game.is_x_at(Position(1, 5)))

    def test_player_cant_play_outside_the_board_boundaries_4(self):
        game = Tictactoe()
        game.x_takes_position(game.UPPER_LEFT)

        try:
            game.o_takes_position(Position(2, -2))
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(game.ERROR_POSITION_OUTSIDE_BOARD, str(error))
            self.assertFalse(game.is_x_at(Position(2, -2)))

    def test_player_x_wins_if_marked_a_winning_combination(self):
        game = Tictactoe()

        game.x_takes_position(game.MIDDLE_CENTER)
        game.o_takes_position(game.UPPER_LEFT)
        game.x_takes_position(game.UPPER_RIGHT)
        game.o_takes_position(game.BOTTOM_LEFT)
        game.x_takes_position(game.MIDDLE_RIGHT)
        game.o_takes_position(game.BOTTOM_RIGHT)
        game.x_takes_position(game.MIDDLE_LEFT)

        self.assertTrue(game.has_player_x_won())
        self.assertFalse(game.has_player_o_won())

    def test_player_o_wins_if_marked_a_winning_combination(self):
        game = Tictactoe()

        game.x_takes_position(game.MIDDLE_CENTER)
        game.o_takes_position(game.UPPER_LEFT)
        game.x_takes_position(game.UPPER_RIGHT)
        game.o_takes_position(game.BOTTOM_LEFT)
        game.x_takes_position(game.MIDDLE_RIGHT)
        game.o_takes_position(game.MIDDLE_LEFT)

        self.assertTrue(game.has_player_o_won())
        self.assertFalse(game.has_player_x_won())

    def test_player_cant_play_if_there_is_a_winner(self):
        game = Tictactoe()

        game.x_takes_position(game.MIDDLE_CENTER)
        game.o_takes_position(game.UPPER_LEFT)
        game.x_takes_position(game.UPPER_RIGHT)
        game.o_takes_position(game.BOTTOM_LEFT)
        game.x_takes_position(game.MIDDLE_RIGHT)
        game.o_takes_position(game.MIDDLE_LEFT)

        try:
            game.x_takes_position(game.BOTTOM_RIGHT)
            self.fail("An exception was expected")
        except Exception as error:
            self.assertEqual(game.ERROR_MATCH_FINISHED, str(error))
            self.assertFalse(game.is_x_at(game.BOTTOM_RIGHT))
            self.assertFalse(game.has_player_x_won())
            self.assertTrue(game.has_player_o_won())

    def test_match_ends_if_board_is_full_and_there_is_no_winner(self):
        game = Tictactoe()

        game.x_takes_position(game.MIDDLE_CENTER)
        game.o_takes_position(game.UPPER_LEFT)
        game.x_takes_position(game.UPPER_RIGHT)
        game.o_takes_position(game.BOTTOM_LEFT)
        game.x_takes_position(game.MIDDLE_LEFT)
        game.o_takes_position(game.BOTTOM_CENTER)
        game.x_takes_position(game.UPPER_CENTER)
        game.o_takes_position(game.MIDDLE_RIGHT)
        game.x_takes_position(game.BOTTOM_RIGHT)

        self.assertTrue(game.board_is_full())
        self.assertFalse(game.has_player_x_won())
        self.assertFalse(game.has_player_o_won())





if __name__ == '__main__':
    unittest.main()
