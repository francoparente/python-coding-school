from datetime import timedelta
from uuid import uuid4

from src.Card import Card
from src.Cashier import Cashier
from src.ShoppingCart import ShoppingCart


class YourBooksApp:
    ERROR_INVALID_CREDENTIALS = "Invalid Credentials"
    ERROR_INVALID_CART_ID = "Invalid Cart ID"
    ERROR_EXPIRED_TIME = 'Time has expired'


def __init__(self, client_credentials_authenticator, catalogue, a_clock, merchant_processor, a_sales_book=None):
    if a_sales_book is None:
        a_sales_book = []

    self._are_invalid_credentials = client_credentials_authenticator
    self._catalogue = catalogue
    self._carts = {}
    self._clock = a_clock
    self._merchant_processor = merchant_processor
    self._last_use = a_clock.today()
    self._sales_book = a_sales_book


def create_cart(self, a_client_id, a_password):
    self.assert_valid_credentials(a_client_id, a_password)
    cart_id = uuid4()
    new_shopping_cart = ShoppingCart(self._catalogue)
    self._carts[cart_id] = new_shopping_cart
    self._last_use = self._clock.today()

    return cart_id


def assert_valid_credentials(self, a_client_id, a_password):
    if self._are_invalid_credentials(a_client_id, a_password):
        raise Exception(YourBooksApp.ERROR_INVALID_CREDENTIALS)


def assert_valid_cart_id(self, a_cart_id):
    if a_cart_id not in self._carts:
        raise Exception(YourBooksApp.ERROR_INVALID_CART_ID)


def assert_cart_session_not_expired(self):
    if self.expired_time():
        raise Exception(YourBooksApp.ERROR_EXPIRED_TIME)


def expired_time(self):
    return self._clock.today() - self._last_use >= timedelta(minutes=30)

def disable_cart(self):
    del self._cart[a_cart_id]
    del self._last_time_used_by_cart[a_cart_id]

def check_out_cart(self, a_cart_id, a_card_number, a_name, expiration_date):
    self.assert_cart_session_not_expired()
    a_card = Card(a_card_number, a_name, expiration_date)
    a_cart: ShoppingCart = self._carts.get(a_cart_id)
    cashier = Cashier(a_cart, a_card, self._merchant_processor, self._sales_book)
    self._last_use = self._clock.today()

    return cashier.checkout()

    # result = self.with_cart_do(a_cart_id, lambda cart: None)
    #
    # del self._carts[a_cart_id]
    #
    # return result


def add_to_cart(self, a_cart_id, book_isbn, book_quantity):
    self.with_cart_do(a_cart_id, lambda cart: cart.keep_copies(book_isbn, book_quantity))
    self.assert_cart_session_not_expired()

    shopping_cart: ShoppingCart = self._carts.get(a_cart_id)
    self._last_use = self._clock.today()

    return shopping_cart.append_with_quantity(book_isbn, book_quantity)


def list_purchases(self, a_client_id, a_password):
    self.assert_valid_credentials(a_client_id, a_password)
    self.assert_cart_session_not_expired()
    client_purchases = [sale for sale in self._sales_book if sale.client() == a_client_id]

    return client_purchases[0].purchased_books(), client_purchases[0].total_amount()


def list_cart(self, a_cart_id):
    self.assert_valid_cart_id(a_cart_id)
    self.assert_cart_session_not_expired()

    a_cart: ShoppingCart = self._carts.get(a_cart_id)
    self._last_use = self._clock.today()

    return a_cart.create_dictionary()


# def list_cart2(self, a_cart_id):
#     result = self.with_cart_do(a_cart_id, lambda cart: cart.books_with_quantities())
#     return result


def with_cart_do(self, a_cart_id, action_to_do):
    self.assert_valid_cart_id(a_cart_id)
    self.assert_cart_session_not_expired(a_cart_id)

    result = action_to_do(self._carts[a_cart_id])

    self.reset_last_time_used(a_cart_id)
    return result
