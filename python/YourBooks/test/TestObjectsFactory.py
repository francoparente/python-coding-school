from src.Card import Card
from tests.ClockSimulator import ManualClock
from src.MerchantProcessor import *
from src.MonthYear import MonthYear
from src.Sale import Sale
from src.ShoppingCart import ShoppingCart
from datetime import datetime


class TestObjectsFactory:
    def empty_cart(self):
        return ShoppingCart(self.publisher_catalogue())

    def valid_book(self):
        return "The Lord of the Rings: The Fellowship of the Ring"

    def another_valid_book(self):
        return "Where's Wally: Lost in Time"

    def invalid_book(self):
        return "Invalid Book"

    def publisher_catalogue(self):
        return {
            self.valid_book(): self.valid_book_price(),
            self.another_valid_book(): self.another_valid_book_price()
        }

    def valid_book_price(self):
        return 10

    def another_valid_book_price(self):
        return 20

    def a_valid_card(self):
        return Card("1234567891234567", "Franco Parente", MonthYear(12, 2023))

    def an_expired_card(self):
        return Card("1234567891234567", "Robert Lewandowsky", MonthYear(12, 2020))

    def an_invalid_card(self):
        return Card("123", "Pibe Valderrama", MonthYear(12, 23))

    def merchant_processor_dummy(self):
        return MerchantProcessorDummy()

    def merchant_processor_success(self):
        return MerchantProcessorSuccess()

    def merchant_processor_insufficient_funds(self):
        return MerchantProcessorInsufficientFunds()

    def sales_book(self):
        return [Sale(1, self.valid_book(), 2, 20)]

    def valid_client_id(self):
        return "Valid Client ID"

    def valid_password(self):
        return "Valid Password"

    def another_valid_client_id(self):
        return "Another Valid Client ID"

    def another_valid_password(self):
        return "Another Valid Password"

    def invalid_client_id(self):
        return "Invalid Client ID"

    def invalid_password(self):
        return "Invalid Password"

    def client_credentials_authenticator(self):
        clients = {
            self.valid_client_id(): self.valid_password(),
            self.another_valid_client_id(): self.another_valid_password(),
        }
        return lambda client_id, password: client_id not in clients or password != clients.get(client_id)

    def clock(self):
        return ManualClock(datetime.today())
