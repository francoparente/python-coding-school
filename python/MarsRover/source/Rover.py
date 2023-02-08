from Position import Position
from RoverCommand import ForwardCommand, BackwardCommand, LeftCommand, RightCommand
from RoverHeading import RoverSouthHeading, RoverNorthHeading, RoverEastHeading, RoverWestHeading


class Rover:
    # ERROR_INVALID_COMMAND = "Invalid error"
    # ERROR_INVALID_HEADING = "Invalid heading"

    def __init__(self, an_x, an_y, a_heading_code):
        self._commands = {'f': ForwardCommand(),
                          'b': BackwardCommand(),
                          'l': LeftCommand(),
                          'r': RightCommand()}

        self._headings = {'NORTH': RoverNorthHeading(),
                          'SOUTH': RoverSouthHeading(),
                          'EAST': RoverEastHeading(),
                          'WEST': RoverWestHeading()}

        # if self._headings.get(a_heading_code) is None:
        #     raise Exception(Rover.ERROR_INVALID_HEADING)

        self._position = Position(an_x, an_y)
        self._heading_code = a_heading_code
        self._heading = self._headings.get(a_heading_code)

    def is_at(self, an_x, an_y):
        return self._position == Position(an_x, an_y)

    def heading(self):
        return self._headings.get(self._heading_code)

    def is_heading(self, a_heading_code):
        return self._heading_code == a_heading_code

    def process_command_codes(self, command_code):
        for command in command_code:
            self._commands.get(command).execute_for(self)

    def step_forward(self):
        self._headings.get(self._heading_code).step_forward(self)

    def step_backward(self):
        self._headings.get(self._heading_code).step_backward(self)

    def turn_right(self):
        self._headings.get(self._heading_code).turn_right(self)

    def turn_left(self):
        self._headings.get(self._heading_code).turn_left(self)

    def step_southward(self):
        self._position = self._position.south_position()

    def step_northward(self):
        self._position = self._position.north_position()

    def step_eastward(self):
        self._position = self._position.east_position()

    def step_westward(self):
        self._position = self._position.west_position()

    def head_to(self, a_heading_code):
        self._heading_code = a_heading_code
