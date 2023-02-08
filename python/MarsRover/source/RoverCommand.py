from abc import ABCMeta, abstractmethod
# import source.Rover as rover


class RoverCommand(metaclass=ABCMeta):
    @abstractmethod
    def execute_for(self, a_rover):
        pass


# ForwardCommand().execute_for(self)
class ForwardCommand(RoverCommand):
    def execute_for(self, a_rover):
        a_rover.step_forward()  # double dispatch


# BackwardCommand().execute_for(self)
class BackwardCommand(RoverCommand):
    def execute_for(self, a_rover):
        a_rover.step_backward()  # double dispatch


# LeftCommand().execute_for(self)
class LeftCommand(RoverCommand):
    def execute_for(self, a_rover):
        a_rover.turn_left()  # double dispatch


# RightCommand().execute_for(self)
class RightCommand(RoverCommand):
    def execute_for(self, a_rover):
        a_rover.turn_right()  # double dispatch

# class UndefinedCommand(RoverCommand):
#     def execute_for(self, a_rover):
#         raise Exception(rover.Rover.ERROR_INVALID_COMMAND)
