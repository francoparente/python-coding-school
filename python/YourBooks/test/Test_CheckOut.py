import unittest

from src.MerchantProcessor import *
from src.Cashier import Cashier
from tests.TestObjectsFactory import TestObjectsFactory


class CheckOutTest(unittest.TestCase):
    def setUp(self):
        self._factory = TestObjectsFactory()

    def test_cant_checkout_empty_cart(self):
        a_cart = self._factory.empty_cart()
        a_card = self._factory.a_valid_card()
        a_cashier = Cashier(a_cart, a_card, self._factory.merchant_processor_dummy(), self._factory.sales_book())

        try:
            a_cashier.checkout()
            self.fail()
        except Exception as error:
            self.assertEqual(Cashier.ERROR_EMPTY_CART, str(error))

    def test_total_amount_returns_total_price_of_cart_1(self):
        a_cart = self._factory.empty_cart()
        a_card = self._factory.a_valid_card()
        a_cart.append(TestObjectsFactory().valid_book())
        a_cashier = Cashier(a_cart, a_card, self._factory.merchant_processor_dummy(), self._factory.sales_book())

        self.assertEqual(10, a_cashier.total_amount())

    def test_total_amount_returns_total_price_of_cart_2(self):
        a_cart = self._factory.empty_cart()
        a_card = self._factory.a_valid_card()
        a_cart.append_with_quantity(2, TestObjectsFactory().valid_book())
        a_cart.append_with_quantity(3, TestObjectsFactory().another_valid_book())
        a_cashier = Cashier(a_cart, a_card, self._factory.merchant_processor_dummy(), self._factory.sales_book())

        self.assertEqual(80, a_cashier.total_amount())

    def test_cannot_checkout_with_expired_card(self):
        a_cart = self._factory.empty_cart()
        a_card = self._factory.an_expired_card()
        a_cart.append_with_quantity(2, TestObjectsFactory().valid_book())
        a_cashier = Cashier(a_cart, a_card, self._factory.merchant_processor_dummy(), self._factory.sales_book())

        try:
            a_cashier.checkout()
            self.fail()
        except Exception as error:
            self.assertEqual(Cashier.ERROR_EXPIRED_CARD, str(error))

    def test_cannot_process_payment_with_insufficient_funds(self):
        a_cart = self._factory.empty_cart()
        a_cart.append_with_quantity(2, TestObjectsFactory().valid_book())
        a_card = self._factory.a_valid_card()
        a_cashier = Cashier(a_cart, a_card, self._factory.merchant_processor_insufficient_funds(), self._factory.sales_book())

        try:
            a_cashier.checkout()
            self.fail()
        except Exception as error:
            self.assertEqual(MerchantProcessor.ERROR_INSUFFICIENT_FUNDS, str(error))

    def test_process_payment_successfully(self):
        a_cart = self._factory.empty_cart()
        a_cart.append_with_quantity(2, TestObjectsFactory().valid_book())
        a_card = self._factory.a_valid_card()
        sales_book = self._factory.sales_book()
        a_cashier = Cashier(a_cart, a_card, self._factory.merchant_processor_success(), sales_book)

        checkout = a_cashier.checkout()

        self.assertEqual(1, sales_book[0].transaction_id())



if __name__ == '__main__':
    unittest.main()
