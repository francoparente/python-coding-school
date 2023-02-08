import unittest

from Rover import Rover


class MarsRoverTest(unittest.TestCase):
    def test_forward_when_heading_north_keeps_heading_and_steps_northward(self):
        a_rover = Rover(0, 0, "NORTH")  # setup

        a_rover.process_command_codes("f")  # exercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 1))
        self.assertTrue(a_rover.is_heading("NORTH"))

    def test_backward_when_heading_north_keeps_heading_and_steps_southward(self):
        a_rover = Rover(0, 0, "NORTH")  # setup

        a_rover.process_command_codes("b")  # excercise

        # asserts
        self.assertFalse(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_at(0, -1))
        self.assertTrue(a_rover.is_heading("NORTH"))

    def test_right_when_heading_north_keeps_position_and_heads_east(self):
        a_rover = Rover(0, 0, "NORTH")  # setup

        a_rover.process_command_codes("r")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_heading("EAST"))
        self.assertFalse(a_rover.is_heading("NORTH"))

    def test_left_when_heading_north_keeps_position_and_heads_west(self):
        a_rover = Rover(0, 0, "NORTH")  # setup

        a_rover.process_command_codes("r")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_heading("EAST"))
        self.assertFalse(a_rover.is_heading("NORTH"))

    def test_forward_when_heading_south_keeps_heading_and_steps_southward(self):
        a_rover = Rover(0, 0, "SOUTH")  # setup

        a_rover.process_command_codes("f")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, -1))
        self.assertTrue(a_rover.is_heading("SOUTH"))

    def test_backward_when_heading_south_keeps_heading_and_steps_northward(self):
        a_rover = Rover(0, 0, "NORTH")  # setup

        a_rover.process_command_codes("b")  # excercise

        # asserts
        self.assertFalse(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_at(0, -1))
        self.assertTrue(a_rover.is_heading("NORTH"))

    def test_right_when_heading_south_keeps_position_and_heads_west(self):
        a_rover = Rover(0, 0, "SOUTH")  # setup

        a_rover.process_command_codes("r")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_heading("WEST"))
        self.assertFalse(a_rover.is_heading("SOUTH"))

    def test_left_when_heading_south_keeps_position_and_heads_east(self):
        a_rover = Rover(0, 0, "SOUTH")  # setup

        a_rover.process_command_codes("l")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_heading("EAST"))
        self.assertFalse(a_rover.is_heading("SOUTH"))

    def test_forward_when_heading_east_keeps_heading_and_steps_eastward(self):
        a_rover = Rover(0, 0, "EAST")  # setup

        a_rover.process_command_codes("f")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(1, 0))
        self.assertTrue(a_rover.is_heading("EAST"))

    def test_backward_when_heading_east_keeps_heading_and_steps_westward(self):
        a_rover = Rover(0, 0, "EAST")  # setup

        a_rover.process_command_codes("b")  # excercise

        # asserts
        self.assertFalse(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_at(-1, 0))
        self.assertTrue(a_rover.is_heading("EAST"))

    def test_right_when_heading_east_keeps_position_and_heads_south(self):
        a_rover = Rover(0, 0, "EAST")  # setup

        a_rover.process_command_codes("r")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_heading("SOUTH"))
        self.assertFalse(a_rover.is_heading("EAST"))

    def test_left_when_heading_east_keeps_position_and_heads_north(self):
        a_rover = Rover(0, 0, "EAST")  # setup

        a_rover.process_command_codes("l")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_heading("NORTH"))
        self.assertFalse(a_rover.is_heading("EAST"))

    def test_forward_when_heading_east_keeps_heading_and_steps_westward(self):
        a_rover = Rover(0, 0, "WEST")  # setup

        a_rover.process_command_codes("f")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(-1, 0))
        self.assertTrue(a_rover.is_heading("WEST"))

    def test_backward_when_heading_west_keeps_heading_and_steps_eastward(self):
        a_rover = Rover(0, 0, "WEST")  # setup

        a_rover.process_command_codes("b")  # excercise

        # asserts
        self.assertFalse(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_at(1, 0))
        self.assertTrue(a_rover.is_heading("WEST"))

    def test_right_when_heading_west_keeps_position_and_heads_north(self):
        a_rover = Rover(0, 0, "WEST")  # setup

        a_rover.process_command_codes("r")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_heading("NORTH"))
        self.assertFalse(a_rover.is_heading("WEST"))

    def test_left_when_heading_west_keeps_position_and_heads_south(self):
        a_rover = Rover(0, 0, "WEST")  # setup

        a_rover.process_command_codes("l")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_heading("SOUTH"))
        self.assertFalse(a_rover.is_heading("WEST"))

    def test_step_back_and_then_forward_and_turn_right_twice(self):
        a_rover = Rover(0, 0, "NORTH")  # setup

        a_rover.process_command_codes("fbrr")  # excercise

        # asserts
        self.assertTrue(a_rover.is_at(0, 0))
        self.assertTrue(a_rover.is_heading("SOUTH"))

    # def test_invalid_command_received(self):
    #     a_rover = Rover(0, 0, "NORTH")  # setup
    #
    #    try:
    #        a_rover.process_command_codes("x")
    #        self.fail()
    #    except Exception as error:
    #        self.assertEqual(Rover.ERROR_INVALID_COMMAND, str(error))
    #
    # def test_invalid_heading_received(self):
    #     try:
    #         a_rover = Rover(0, 0, "x")  # setup
    #         self.fail()
    #     except Exception as error:
    #         self.assertEqual(Rover.ERROR_INVALID_HEADING, str(error))

if __name__ == '__main__':
    unittest.main()
