from abc import ABC, abstractmethod


class StackElement(ABC):

    @abstractmethod
    def deep_size(self):
        pass


class StackTop(StackElement):
    def __init__(self, a_value, a_previous):
        self._value = a_value
        self._previous = a_previous

    def value(self):
        return self._value

    def previous(self):
        return self._previous

    def size(self):
        return 1

    def deep_size(self):
        return self.size() + self._previous.deep_size()


class StackNone(StackElement):
    def size(self):
        return 0

    def deep_size(self):
        return self.size()


class Stack:
    _top_element: StackTop

    def __init__(self):
        self._top_element = None

    def is_empty(self):
        return self._top_element is None

    def push(self, an_object):
        self._top_element = StackTop(an_object, self._top_element)

    def top(self):
        return self._top_element.value()

    def pop(self):
        element_to_pop = self._top_element.value()
        self._top_element = self._top_element.previous()
        return element_to_pop

    def size(self):
        return self._top_element.deep_size()
