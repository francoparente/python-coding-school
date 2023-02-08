from abc import ABCMeta, abstractmethod


class RoverHeadings(metaclass=ABCMeta):
    @abstractmethod
    def step_forward(self, a_rover):
        pass

    @abstractmethod
    def step_backward(self, a_rover):
        pass

    @abstractmethod
    def turn_right(self, a_rover):
        pass

    @abstractmethod
    def turn_left(self, a_rover):
        pass


class RoverSouthHeading:
    def step_forward(self, a_rover):
        a_rover.step_southward()

    def step_backward(self, a_rover):
        a_rover.step_northward()

    def turn_right(self, a_rover):
        a_rover.head_to("WEST")

    def turn_left(self, a_rover):
        a_rover.head_to("EAST")


class RoverNorthHeading:
    def step_forward(self, a_rover):
        a_rover.step_northward()

    def step_backward(self, a_rover):
        a_rover.step_southward()

    def turn_right(self, a_rover):
        a_rover.head_to("EAST")

    def turn_left(self, a_rover):
        a_rover.head_to("WEST")


class RoverEastHeading:
    def step_forward(self, a_rover):
        a_rover.step_eastward()

    def step_backward(self, a_rover):
        a_rover.step_westward()

    def turn_right(self, a_rover):
        a_rover.head_to("SOUTH")

    def turn_left(self, a_rover):
        a_rover.head_to("NORTH")


class RoverWestHeading:
    def step_forward(self, a_rover):
        a_rover.step_westward()

    def step_backward(self, a_rover):
        a_rover.step_eastward()

    def turn_right(self, a_rover):
        a_rover.head_to("NORTH")

    def turn_left(self, a_rover):
        a_rover.head_to("SOUTH")
