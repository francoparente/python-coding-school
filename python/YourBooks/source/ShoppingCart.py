# from src.Item import Item


class ShoppingCart:
    ERROR_INVALID_PURCHASE = 'Cannot Add zero o less books to the cart'
    ERROR_INVALID_BOOK = "Cannot Add Invalid Book"

    def __init__(self, catalogue):
        self._catalogue = catalogue
        self._books_in_the_cart = []

    def is_empty(self):
        return len(self._books_in_the_cart) == 0

    def append_with_quantity(self, number_of_copies, a_book):
        if number_of_copies <= 0:
            raise Exception(ShoppingCart.ERROR_INVALID_PURCHASE)
        for i in range(number_of_copies):
            self.append(a_book)

    def contains(self, a_book):
        return self._books_in_the_cart[self._books_in_the_cart.index(a_book)]

    def number_of_items(self):
        return len(self._books_in_the_cart)

    def count(self, a_book):
        return self._books_in_the_cart.count(a_book)

    def append(self, a_book):
        self.assert_book_belongs_to_publisher(a_book)
        self._books_in_the_cart.append(a_book)

    # def append(self, a_book):
    #     self.assert_book_belongs_to_publisher(a_book)
    #     self._books_in_the_cart.append(a_book)

    def assert_book_belongs_to_publisher(self, a_book):
        if a_book not in self._catalogue:
            raise Exception(ShoppingCart.ERROR_INVALID_BOOK)

    def total_amount(self):
        # opción 1: comprehension list
        return sum([self.price_of(book) for book in self._books_in_the_cart])

        # opción 2: mapeo
        # return sum(map(lambda book: self.price_of(book), self._books_in_the_cart))

        # opción 3: procedural
        # total_amount = 0
        # for book in self._books_in_the_cart:
        #     total_amount += self.price_of(book)
        #
        # return total_amount

    def price_of(self, book):
        return self._catalogue.get(book)

    # def for_each_book(self, param):
    #     pass

    def list_items(self):
        return self._books_in_the_cart

    def create_dictionary(self):
        dictionary = {}
        books = set()
        for book in self._books_in_the_cart:
            books.add(book)
        for book in books:
            dictionary[book] = self.count(book)
        return dictionary

    # def append_item(self, book_name, quantity):
    #     self.append(Item(book_name, quantity))

