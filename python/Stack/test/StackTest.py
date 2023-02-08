import unittest

from src.Stack import Stack


class StackTest(unittest.TestCase):
    def test_a_stack_is_initially_empty(self):
        a_stack = Stack()

        self.assertTrue(a_stack.is_empty())
        self.assertEqual(0, a_stack.size())

    def test_push_adds_an_element_to_the_stack(self):
        a_stack = Stack()

        a_stack.push(self.an_element())

        self.assertFalse(a_stack.is_empty())
        self.assertEqual(1, a_stack.size())
        self.assertEqual(self.an_element(), a_stack.top())

    def test_pop_removes_the_top_element_of_the_stack(self):
        a_stack = Stack()
        a_stack.push(self.an_element())

        a_stack.pop()

        self.assertTrue(a_stack.is_empty())

    def test_pop_returns_the_top_element_of_the_stack(self):
        a_stack = Stack()
        a_stack.push(self.an_element())

        popped_element = a_stack.pop()

        self.assertEqual(self.an_element(), popped_element)

    def test_top_does_not_remove_the_top_element_of_the_stack(self):
        a_stack = Stack()
        a_stack.push(self.an_element())

        a_stack.top()

        self.assertFalse(a_stack.is_empty())
        self.assertEqual(1, a_stack.size())

    def test_after_popping_an_element_the_previous_elements_remain_on_the_stack(self):
        a_stack = Stack()
        a_stack.push(self.an_element())
        a_stack.push(self.another_element())
        a_stack.push(self.yet_another_element())

        a_stack.pop()

        self.assertEqual(self.another_element(), a_stack.top())
        self.assertFalse(a_stack.is_empty())

    def test_a_stack_behaves_lifo(self):
        a_stack = Stack()
        a_stack.push(self.an_element())
        a_stack.push(self.another_element())
        a_stack.push(self.yet_another_element())

        self.assertEqual(3, a_stack.size())
        self.assertEqual(self.yet_another_element(), a_stack.pop())
        self.assertEqual(self.another_element(), a_stack.pop())
        self.assertEqual(self.an_element(), a_stack.pop())
        self.assertEqual(0, a_stack.size())
        self.assertTrue(a_stack.is_empty())

    def test_cannot_pop_empty_stack(self):
        a_stack = Stack()

        try:
            a_stack.pop()
            self.fail()
        except Exception as exception:
            self.assertEqual(Stack.ERROR_EMPTY_STACK, str(exception))
            self.assertTrue(a_stack.is_empty())
            self.assertEqual(0, a_stack.size())

    def test_cannot_ask_for_top_of_empty_stack(self):
        a_stack = Stack()

        try:
            a_stack.top()
            self.fail()
        except Exception as exception:
            self.assertEqual(Stack.ERROR_EMPTY_STACK, str(exception))
            self.assertTrue(a_stack.is_empty())
            self.assertEqual(0, a_stack.size())

    # TODO: Ponerle buenos nombres a estos tests (del map)
    def test01(self):
        a_stack = Stack()

        mapped_stack = a_stack.map(lambda elemento: None)

        self.assertTrue(mapped_stack.is_empty())

    def test02(self):
        a_stack = Stack()
        a_stack.push(2)

        mapped_stack = a_stack.map(lambda elemento: elemento + 1)

        self.assertEqual(1, mapped_stack.size())
        self.assertEqual(3, mapped_stack.top())

    def test03(self):
        a_stack = Stack()
        a_stack.push(1)
        a_stack.push(2)
        a_stack.push(3)

        mapped_stack = a_stack.map(lambda elemento: str(elemento + 1))

        self.assertEqual(3, mapped_stack.size())
        self.assertEqual("4", mapped_stack.pop())
        self.assertEqual("3", mapped_stack.pop())
        self.assertEqual("2", mapped_stack.pop())


    def an_element(self):
        return "un elemento"

    def another_element(self):
        return "otro elemento"

    def yet_another_element(self):
        return "otro elemento más"


if __name__ == '__main__':
    unittest.main()
