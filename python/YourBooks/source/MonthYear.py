from datetime import date


class MonthYear:
    @classmethod
    def new_from(cls, a_date: date):
        return cls(a_date.month, a_date.year)

    def __init__(self, a_month, a_year):
        self._month = a_month
        self._year = a_year

    def __lt__(self, other):
        return self._year < other.year() or (self._year == other.year() and self._month < other.month())

    def month(self):
        return self._month

    def year(self):
        return self._year
