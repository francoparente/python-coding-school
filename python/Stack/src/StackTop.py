from abc import ABCMeta, abstractmethod

import src.Stack as stack


class StackTop(metaclass=ABCMeta):
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def deep_size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def map_on(self, mapped_stack, a_lambda):
        pass


class StackElement(StackTop):
    def __init__(self, value, previous_element):
        self._value = value
        self._previous_element = previous_element

    def value(self):
        return self._value

    def previous(self):
        return self._previous_element

    def deep_size(self):
        return self.size() + self._previous_element.deep_size()

    def size(self):
        return 1

    def is_empty(self):
        return False

    def map_on(self, mapped_stack, a_lambda):
        self._previous_element.map_on(mapped_stack, a_lambda)
        mapped_stack.push(a_lambda(self._value))



class NoStackElement(StackTop):
    def deep_size(self):
        return self.size()

    def size(self):
        return 0

    def value(self):
        raise Exception(stack.Stack.ERROR_EMPTY_STACK)

    def is_empty(self):
        return True

    def map_on(self, mapped_stack, a_lambda):
        pass
