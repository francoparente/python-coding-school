from abc import ABCMeta, abstractmethod


class StackState(metaclass=ABCMeta):
    @abstractmethod
    def top_for(self, a_stack):
        pass

    @classmethod
    def state_for(cls, a_stack):
        subclasses = cls.__subclasses__()
        return list(filter(lambda each_subclass: each_subclass.can_handle(a_stack), subclasses))[0]()

    @classmethod
    @abstractmethod
    def can_handle(cls, a_stack):
        pass


class NotEmptyStackState(StackState):
    @classmethod
    def can_handle(cls, a_stack):
        return not a_stack.is_empty()

    def top_for(self, a_stack):
        return a_stack.top_when_not_empty()


class EmptyStackState(StackState):
    @classmethod
    def can_handle(cls, a_stack):
        return a_stack.is_empty()

    def top_for(self, a_stack):
        return a_stack.top_when_empty()


class Stack:
    ERROR_STACK_IS_EMPTY = 'Cannot top/pop an empty list'

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, object):
        self.elements.append(object)

    def top(self):
        return self.state().top_for(self)

    def top_when_not_empty(self):
        return self.elements[self.top_index()]

    def top_when_empty(self):
        raise Exception(Stack.ERROR_STACK_IS_EMPTY)

    def top_index(self):
        return len(self.elements) - 1

    def pop(self):
        
        element_to_pop = self.top()
        del self.elements[self.top_index()]
        return element_to_pop

    def size(self):
        return len(self.elements)

    def state(self):
        return StackState.state_for(self)
