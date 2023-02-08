from datetime import date

from src.MonthYear import MonthYear


class Card:
    ERROR_INVALID_CARD = 'Cannot checkout with invalid card'

    def __init__(self, number, name, expire_date):
        self.card_number_validation(number)
        self._number = number
        self._name = name
        self._expire_date = expire_date

    def card_number_validation(self, number):
        if self.is_invalid(number):
            raise Exception(self.ERROR_INVALID_CARD)

    def is_expired(self):
        return self._expire_date < MonthYear.new_from(date.today())

    def is_invalid(self, number):
        return len(number) != 16
