import unittest

from src.YourBooksApp import YourBooksApp
from tests.TestObjectsFactory import TestObjectsFactory
from tests.ExtendedTestCase import ExtendedTestCase


class YourBooksAppTest(ExtendedTestCase):
    def setUp(self):
        self._factory = TestObjectsFactory()

    def test_cant_create_cart_with_invalid_client_id(self):
        a_clock = self._factory.clock()

        application = YourBooksApp(
            self._factory.client_credentials_authenticator(),
            self._factory.publisher_catalogue(),
            a_clock,
            self._factory.merchant_processor_dummy()
        )
        self.assert_raises(lambda: application.create_cart(self._factory.invalid_client_id(), self._factory.valid_password()),
                           Exception,
                           YourBooksApp.ERROR_INVALID_CREDENTIALS)

    def test_cant_create_cart_with_invalid_password(self):
        application = YourBooksApp(
            lambda client_id, password: client_id != "Valid Client ID" or password != "Valid Password",
            self._factory.publisher_catalogue()
        )

        self.assert_raises(lambda: application.create_cart(self._factory.valid_client_id(), self._factory.invalid_password()),
                           Exception,
                           YourBooksApp.ERROR_INVALID_CREDENTIALS)

    def test_a_new_cart_starts_empty(self):
        application = YourBooksApp(
            self._factory.client_credentials_authenticator(),
            self._factory.publisher_catalogue()
        )

        cart_id = application.create_cart(self._factory.valid_client_id(), self._factory.valid_password())

        self.assertEqual(0, len(application.list_cart(cart_id)))

    def test_another_new_cart_starts_empty(self):
        application = YourBooksApp(
            self._factory.client_credentials_authenticator(),
            self._factory.publisher_catalogue()
        )

        cart_id = application.create_cart(self._factory.another_valid_client_id(), self._factory.another_valid_password())

        self.assertEqual(0, len(application.list_cart(cart_id)))

    def test_cannot_use_cart_after_checking_it_out(self):
        cart_id = self.empty_cart_id()
        self._app.add_to_cart(cart_id, self._factory.valid_book(), 1)

        self._app.checkout_cart(cart_id)

        self.assert_raises(lambda: self._app.list_cart(cart_id),
                           Exception,
                           YourBooksApp)


    # def test_cart_can_not_do_a_list_cart_after_30_minutes(self):
    #     a_clock = self._factory.clock()
    #     an_application = YourBooksApplication(self._factory.client_credentials_authenticator(),
    #                                           self._factory.publisher_catalogue(), a_clock,
    #                                           self._factory.merchant_processor_dummy())
    #     cart_id = an_application.create_cart(self._factory.another_valid_client_id(),
    #                                          self._factory.another_valid_password())
    #     a_clock.advance(timedelta(minutes=31))
    #     try:
    #         an_application.list_cart(cart_id)
    #         self.fail()
    #     except Exception as error:
    #         self.assertEqual(YourBooksApplication.ERROR_EXPIRED_TIME, str(error))
    #
    # def test_cart_cannot_checkout_a_cart_after_30_minutes(self):
    #     a_clock = self._factory.clock()
    #     an_application = YourBooksApplication(self._factory.client_credentials_authenticator(),
    #                                           self._factory.publisher_catalogue(), a_clock,
    #                                           self._factory.merchant_processor_dummy())
    #     cart_id = an_application.create_cart(self._factory.another_valid_client_id(),
    #                                          self._factory.another_valid_password())
    #     a_clock.advance(timedelta(minutes=31))
    #     card_number = 1234432167891234
    #     name = 'Sofia'
    #     expiration_date = MonthYear(11, 2023)
    #     try:
    #         an_application.check_out_cart(cart_id, card_number, name, expiration_date)
    #         self.fail()
    #     except Exception as error:
    #         self.assertEqual(YourBooksApplication.ERROR_EXPIRED_TIME, str(error))
    #
    # def test_cart_cannot_add_book_a_cart_after_30_minutes(self):
    #     a_clock = self._factory.clock()
    #     an_application = YourBooksApplication(self._factory.client_credentials_authenticator(),
    #                                           self._factory.publisher_catalogue(), a_clock,
    #                                           self._factory.merchant_processor_dummy())
    #     cart_id = an_application.create_cart(self._factory.another_valid_client_id(),
    #                                          self._factory.another_valid_password())
    #     a_clock.advance(timedelta(minutes=31))
    #     book_isbn = self._factory.valid_book() # revisar isbn
    #     book_quantity = 2
    #     try:
    #         an_application.add_to_cart(cart_id, book_isbn, book_quantity)
    #         self.fail()
    #     except Exception as error:
    #         self.assertEqual(YourBooksApplication.ERROR_EXPIRED_TIME, str(error))
    #
    # def test_a_client_can_know_its_purchases(self):
    #     a_sales_book = self._factory.empty_sales_book()
    #     a_client_id = self._factory.valid_client_id()
    #     a_cart = self._factory.empty_cart()
    #     a_cart.append_with_quantity(2, self._factory.valid_book())
    #     expected_total = 2 * self._factory.valid_book_price()
    #     a_client_sale = Sale(a_client_id=a_client_id,
    #                          a_date=self._factory.a_valid_date(),
    #                          a_cart=a_cart,
    #                          a_transaction_id=0
    #                          )
    #     another_client_sale = self.sale_made_by(self._factory.another_valid_client_id())
    #     a_sales_book.append(a_client_sale)
    #     a_sales_book.append(another_client_sale)
    #     an_application = YourBooksApplication(self._factory.client_credentials_authenticator(),
    #                                           self._factory.publisher_catalogue(), self._factory.clock(),
    #                                           self._factory.merchant_processor_dummy(), a_sales_book=a_sales_book)
    #     purchased_books, total_amount = an_application.list_purchases(a_client_id, self._factory.valid_password())
    #     self.assertEqual(expected_total, total_amount)
    #     self.assertEqual(2, purchased_books[self._factory.valid_book()])
    #
    # def sale_made_by(self, another_client_id):
    #     another_client_sale = Sale(
    #         a_client_id=another_client_id,
    #         a_date=self._factory.a_valid_date(),
    #         a_cart=self._factory.full_cart(),
    #         a_transaction_id=1
    #     )
    #     return another_client_sale


if __name__ == '__main__':
    unittest.main()
