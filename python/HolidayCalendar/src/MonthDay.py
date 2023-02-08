class MonthDay:
    @classmethod
    def new_from(cls, a_date):
        return cls(a_date.month, a_date.day)
    def __init__(self,a_month, a_day):
        self._month = a_month
        self._day = a_day
    def __eq__(self, other):
        return self._day == other.day() and self._month == other.month()
    def __hash__(self):
        return hash(self._month ** self._day)
    def month(self):
        return self._month
    def day(self):
        return self._day
