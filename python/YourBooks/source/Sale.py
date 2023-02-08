from src.ShoppingCart import ShoppingCart


class Sale:
    def __init__(self, a_date, a_transaction_id, a_cart: ShoppingCart, a_client_id):
        self._date = a_date
        self._transaction_id = a_transaction_id
        self._cart = a_cart
        self._client = a_client_id

    def transaction_id(self):
        return self._transaction_id

    def total_amount(self):
        return self._cart.total_amount()

    def client(self):
        return self._client

    def purchased_books(self):
        return self._cart.create_dictionary()
