from src.StackTop import StackTop, StackElement, NoStackElement


class Stack:
    ERROR_EMPTY_STACK = "Stack is empty"

    _top: StackTop

    def __init__(self):
        self._top = NoStackElement()

    def is_empty(self):
        return self._top.is_empty()

    def size(self):
        return self._top.deep_size()

    def push(self, an_object):
        self._top = StackElement(an_object, self._top)

    def top(self):
        return self._top.value()

    def pop(self):
        object_to_pop = self.top()
        self._top = self._top.previous()
        return object_to_pop

    def map(self, a_lambda):
        mapped_stack = Stack()

        self._top.map_on(mapped_stack, a_lambda)

        return mapped_stack
