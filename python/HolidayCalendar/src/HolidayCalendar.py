from datetime import date

class HolidayCalendar:
    def __init__(self):
        self._holiday_rule = set()
    def is_holiday(self, a_date: date):
        return any([rule.is_holiday(a_date) is True for rule in self._holiday_rule])
    def add_holiday_rule(self, a_holidai_rule):
        self._holiday_rule.add(a_holidai_rule)

