import unittest

from src.StackSinListas import Stack


class Pilatest(unittest.TestCase):
    def test_when_the_stack_is_empty(self):
        stack = Stack()

        self.assertEqual(True, stack.is_empty())
#
    def test_when_the_stack_add_an_object(self):
        stack = Stack()
        stack.push("A")

        self.assertEqual("A", stack.top())
        self.assertFalse(stack.is_empty())
#
    def test_pop_removes_top_element_and_returns_it(self):
        stack = Stack()
        stack.push("A")
        stack.push("B")

        popped_element = stack.pop()
        self.assertEqual("B", popped_element)
        self.assertEqual("A", stack.top())
        self.assertFalse(stack.is_empty())


    def test_after_popping_element_from_a_size_3_stack_new_size_is_2(self):
        stack = Stack()
        stack.push("A")
        stack.push("B")
        stack.push("C")

        popped_element = stack.pop()
        self.assertEqual("C", popped_element)
        self.assertEqual("B", stack.top())
        self.assertFalse(stack.is_empty())
        self.assertEqual(2, stack.size())
#
#     def test_the_stack_can_not_pop_when_is_empty(self):
#         stack = Stack()
#         try:
#             stack.pop()
#             self.fail('An exception was expected')
#         except Exception as exception:
#             self.assertEquals(Stack.ERROR_STACK_IS_EMPTY, str(exception))
#             self.assertTrue(stack.is_empty())
#
#     def test_the_stack_can_not_top_when_is_empty(self):
#         stack = Stack()
#         try:
#             stack.top()
#             self.fail('An exception was expected')
#         except Exception as exception:
#             self.assertEquals(Stack.ERROR_STACK_IS_EMPTY, str(exception))
#             self.assertTrue(stack.is_empty())
#
#
if __name__ == '__main__':
    unittest.main()
