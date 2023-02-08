class Item:
    def __init__(self, book_name, quantity):
        self._book_name = book_name
        self._quantity = quantity

    def book_name(self):
        return self._book_name

    def quantity(self):
        return self._quantity
