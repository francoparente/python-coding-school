import unittest

from src.Pila import Stack


class Pilatest(unittest.TestCase):
    def test_when_the_stack_is_empty(self):
        stack = Stack()
        self.assertEqual(True, stack.is_empty())

    def test_when_the_stack_add_an_object(self):
        stack = Stack()
        stack.push("A")
        self.assertEqual("A", stack.top())
        self.assertFalse(stack.is_empty())

    def test_when_the_stack_add_two_elements_and_then_pop(self):
        stack = Stack()
        stack.push("A")
        stack.push("B")
        x = stack.pop()
        self.assertEqual("B", x)
        self.assertEqual("A", stack.top())
        self.assertFalse(stack.is_empty())

    def test_when_the_stack_add_three_elements_and_then_pop(self):
        stack = Stack()
        stack.push("A")
        stack.push("B")
        stack.push("A")
        stack.pop()
        self.assertEqual("B", stack.top())
        self.assertFalse(stack.is_empty())

    def test_when_the_stack_add_three_elements_and_then_pop2(self):
        stack = Stack()
        stack.push("A")
        stack.push("B")
        stack.push("C")
        stack.push("D")
        stack.push("B")
        stack.push("A")
        x = stack.pop()
        self.assertEqual("A", x)
        self.assertEqual("B", stack.top())
        self.assertFalse(stack.is_empty())
        self.assertEqual(5, stack.size())

    def test_the_stack_can_not_pop_when_is_empty(self):
        stack = Stack()
        try:
            stack.pop()
            self.fail('An exception was expected')
        except Exception as exception:
            self.assertEquals(Stack.ERROR_STACK_IS_EMPTY, str(exception))
            self.assertTrue(stack.is_empty())

    def test_the_stack_can_not_top_when_is_empty(self):
        stack = Stack()
        try:
            stack.top()
            self.fail('An exception was expected')
        except Exception as exception:
            self.assertEquals(Stack.ERROR_STACK_IS_EMPTY, str(exception))
            self.assertTrue(stack.is_empty())


if __name__ == '__main__':
    unittest.main()
