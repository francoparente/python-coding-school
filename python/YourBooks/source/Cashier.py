class Cashier:
    ERROR_EMPTY_CART = 'Cannot checkout an empty cart'
    ERROR_EXPIRED_CARD = 'Cannot checkout with expired card'

    def __init__(self, a_cart, a_card, a_merchant_processor, a_sales_book):
        self._sales_book = a_sales_book
        self._merchant_processor = a_merchant_processor
        self._cart = a_cart
        self._card = a_card
        self._transaction_id = 0
        # self._catalogue

    def checkout(self):
        if self._cart.is_empty():
            raise Exception(Cashier.ERROR_EMPTY_CART)

        if self._card.is_expired():
            raise Exception(Cashier.ERROR_EXPIRED_CARD)

        # self._transaction_id = self._merchant_processor.debit()
        transaction_id = self._merchant_processor.debit()
        # self.register_transaction()

        return self.total_amount()

        # total = 0
        # return self._cart.for_each_book(lambda book: total = total + self._catalogue.get(book))

    def total_amount(self):
        return self._cart.total_amount()

