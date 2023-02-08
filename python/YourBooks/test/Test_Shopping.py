import unittest

from src.Item import Item
from src.ShoppingCart import ShoppingCart
from tests.TestObjectsFactory import TestObjectsFactory


class ShoppingTest(unittest.TestCase):
    def setUp(self):
        self._test_objects = TestObjectsFactory()

    # tests
    def test_the_cart_is_empty(self):
        a_shopping_cart = ShoppingCart(self._test_objects.publisher_catalogue())

        self.assertTrue(a_shopping_cart.is_empty())

    def test_when_a_book_is_added_the_cart_is_not_empty(self):
        a_shopping_cart = ShoppingCart(self._test_objects.publisher_catalogue())
        a_shopping_cart.append(self._test_objects.valid_book())

        self.assertFalse(a_shopping_cart.is_empty())
        self.assertTrue(a_shopping_cart.contains(self._test_objects.valid_book()))

    def test_when_you_add_more_than_one_book_the_cart_is_not_empty(self):
        a_shopping_cart = ShoppingCart(self._test_objects.publisher_catalogue())
        a_shopping_cart.append_with_quantity(1, self._test_objects.valid_book())
        a_shopping_cart.append_with_quantity(1, self._test_objects.another_valid_book())

        self.assertFalse(a_shopping_cart.is_empty())
        self.assertEqual(self._test_objects.valid_book(), a_shopping_cart.contains(self._test_objects.valid_book()))
        self.assertEqual(self._test_objects.another_valid_book(), a_shopping_cart.contains(
            self._test_objects.another_valid_book()))

    def test_add_more_than_one_of_the_same_book(self):
        a_shopping_cart = ShoppingCart(self._test_objects.publisher_catalogue())
        a_shopping_cart.append_with_quantity(2, self._test_objects.valid_book())

        self.assertFalse(a_shopping_cart.is_empty())
        self.assertEqual(2, a_shopping_cart.count(self._test_objects.valid_book()))

    def test_cannot_add_book_not_belonging_to_the_publisher(self):
        a_shopping_cart = ShoppingCart(self._test_objects.publisher_catalogue())

        try:
            a_shopping_cart.append(self._test_objects.invalid_book())
            self.fail()
        except Exception as error:
            self.assertTrue(a_shopping_cart.is_empty())
            self.assertEqual(ShoppingCart.ERROR_INVALID_BOOK, str(error))

    def test_cannot_add_zero_or_less_than_one_book(self):
        a_shopping_cart = ShoppingCart(self._test_objects.publisher_catalogue())

        try:
            a_shopping_cart.append_with_quantity(0, self._test_objects.valid_book())
            self.fail()
        except Exception as error:
            self.assertTrue(a_shopping_cart.is_empty())
            self.assertEqual(ShoppingCart.ERROR_INVALID_PURCHASE, str(error))

    def test_count_returns_the_amount_of_each_book(self):
        a_shopping_cart = ShoppingCart(self._test_objects.publisher_catalogue())
        book = self._test_objects.valid_book()
        another_book = self._test_objects.another_valid_book()
        a_shopping_cart.append_with_quantity(2, book)
        a_shopping_cart.append_with_quantity(3, another_book)

        self.assertFalse(a_shopping_cart.is_empty())
        self.assertTrue(5, a_shopping_cart.number_of_items())
        self.assertTrue(2, a_shopping_cart.count(book))
        self.assertTrue(3, a_shopping_cart.count(another_book))

    def x_test_list_returns_all_items_in_the_cart_with_their_quantity(self):
        a_shopping_cart = ShoppingCart(self._test_objects.publisher_catalogue())
        book = self._test_objects.valid_book()
        another_book = self._test_objects.another_valid_book()
        a_shopping_cart.append_item(book, 2)
        a_shopping_cart.append_item(another_book, 3)

        self.assertFalse(a_shopping_cart.is_empty())
        self.assertTrue([Item("The Lord of the Rings: The Fellowship of the Ring", 2), Item("Where's Wally: Lost in Time", 3)], a_shopping_cart.list_items())
