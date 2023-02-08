from abc import ABCMeta, abstractmethod
from src.MonthDay import MonthDay

class HolidayRule(metaclass=ABCMeta):
    @abstractmethod
    def is_holiday(self, a_date):
        pass

class DayOfWeekHolidayRule(HolidayRule):
    def __init__(self, a_weekday):
        self._weekday = a_weekday
    def is_holiday(self, a_date):
        return a_date.weekday() == self._weekday
class DayOfMonthHolidayRule(HolidayRule):
    def __init__(self, a_month_day):
        self._a_month_day = a_month_day
    def is_holiday(self, a_date):
        return MonthDay.new_from(a_date) == self._a_month_day

class SpecificDateHolidayRule(HolidayRule):
    def __init__(self, a_date):
        self._date = a_date
    def is_holiday(self, a_date):
        return a_date == self._date

class TemporaryHolidayRule(HolidayRule):
    def __init__(self, a_holiday_rule, a_date_interval):
        self._date_interval = a_date_interval
        self._a_holiday_rule = a_holiday_rule

    def is_holiday(self, a_date):
        return self._date_interval.includes(a_date) and self._a_holiday_rule.is_holiday(a_date)
