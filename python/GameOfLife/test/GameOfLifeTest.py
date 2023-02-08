import unittest

from src.GameOfLife import GameOfLife


class GameOfLifeTest(unittest.TestCase):

    def test001_cell_is_not_alive_at_position_1_2(self):
        self.assertFalse(GameOfLife({(1, 1), (3, 1)}).is_cell_alive_in_position((1, 2)))

    def test002_cell_is_alive_at_position_1_1(self):
        self.assertTrue(GameOfLife({(1, 1), (3, 1)}).is_cell_alive_in_position((1, 1)))

    def test003_cell_is_alive_at_position_3_1(self):
        self.assertTrue(GameOfLife({(1, 1), (3, 1)}).is_cell_alive_in_position((3, 1)))

    def test004_cell_without_live_neighbours_dies_by_underpopulation(self):
        self.assertTrue(GameOfLife({(1, 1)}).will_cell_die_by_underpopulation((1, 1)))

    def test005_cell_does_not_die_by_underpopulation_because_its_already_dead(self):
        self.assertFalse(GameOfLife({(3, 3)}).will_cell_die_by_underpopulation((1, 3)))

    def test006_cell_with_two_neighbours_does_not_die_by_underpopulation(self):
        self.assertFalse(GameOfLife({(1, 1), (1, 3)}).will_cell_die_by_underpopulation((2, 2)))

    def test007_position_two_two_neighbours(self):
        self.assertEqual([(1, 1), (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3)],
                         GameOfLife({(2, 2)}).get_neighbours((2, 2)))

    def test008_cells_with_two_live_neighbours_survive_on_to_the_next_generation(self):
        self.assertTrue(GameOfLife({(1, 1), (1, 3), (2, 2)}).will_cell_live_on_to_the_next_generation((2, 2)))

    def test009_cells_with_three_live_neighbours_survive_on_to_the_next_generation(self):
        self.assertFalse(GameOfLife({(1, 1), (1, 3), (2, 1), (2, 2), (1,2)}).will_cell_live_on_to_the_next_generation((1, 2)))

    def test010_cells_whit_more_than_three_live_neighbours_die_by_overpopulation(self):
        self.assertTrue(GameOfLife({(1, 1), (1, 3), (2, 1), (2, 2), (1,2)}).will_cell_die_by_overpopulation((1, 2)))

    def test011_cells_with_three_live_neighbours_become_alive(self):
        self.assertTrue(GameOfLife({(1, 1), (1, 3), (2, 1)}).will_cell_become_alive((1, 2)))

    def test012_live_cell_die(self):
        a_game = GameOfLife({(1, 1)})
        a_game.kill_cell((1, 1))
        self.assertEqual(False, a_game.is_cell_alive_in_position((1,1)))

    def test013_dead_cell_become_alive(self):
        a_game = GameOfLife({})
        a_game.generate_cell((1, 1))
        self.assertEqual(True, a_game.is_cell_alive_in_position((1,1)))

    def xtest014_cells_pass_to_the_next_generation(self):
        a_game = GameOfLife({(1,2), (2,2), (2,1)})
        self.assertEqual({(1, 1),(1, 2),(2, 1),(2, 2)},a_game.pass_on_to_next_generation())

if __name__ == '__main__':
    unittest.main()
