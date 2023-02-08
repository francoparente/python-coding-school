import unittest
from datetime import date

from DateInterval import DateInterval
from src.HolidayRule import DayOfWeekHolidayRule, DayOfMonthHolidayRule, SpecificDateHolidayRule, TemporaryHolidayRule
from src.HolidayCalendar import HolidayCalendar
from src.MonthDay import MonthDay


class HolidayCalendarTest(unittest.TestCase):
    def test_01_any_day_of_week_can_be_holiday(self):
        a_holiday_calendar = HolidayCalendar()
        a_sunday = date(2022, 11, 20)
        a_holiday_calendar.add_holiday_rule(DayOfWeekHolidayRule(a_sunday.weekday()))
        self.assertTrue(a_holiday_calendar.is_holiday(a_sunday))

    def test_02_more_than_one_day_of_week_can_be_holiday(self):
        a_holiday_calendar = HolidayCalendar()
        a_sunday = date(2022, 11, 20)
        a_saturday = date(2022, 11, 19)

        a_holiday_calendar.add_holiday_rule(DayOfWeekHolidayRule(a_sunday.weekday()))
        a_holiday_calendar.add_holiday_rule(DayOfWeekHolidayRule(a_saturday.weekday()))
        self.assertTrue(a_holiday_calendar.is_holiday(a_sunday))
        self.assertTrue(a_holiday_calendar.is_holiday(a_saturday))

    def test_03_any_day_of_month_can_be_holiday(self):
        a_holiday_calendar = HolidayCalendar()
        a_christmas = date(2022, 12, 25)
        a_holiday_calendar.add_holiday_rule(DayOfMonthHolidayRule(MonthDay.new_from(a_christmas)))
        self.assertTrue(a_holiday_calendar.is_holiday(a_christmas))

    def test_04_any_date_may_not_be_holiday(self):
        a_holiday_calendar = HolidayCalendar()
        a_non_holiday = date(2022, 12, 23)

        self.assertFalse(a_holiday_calendar.is_holiday(a_non_holiday))

    def test_05_more_than_one_month_of_week_can_be_holiday(self):
        a_holiday_calendar = HolidayCalendar()
        a_christmas = date(2022, 12, 25)
        a_holiday_calendar.add_holiday_rule(DayOfMonthHolidayRule(MonthDay.new_from(a_christmas)))
        a_new_yers_day = date(2022, 1, 11)
        a_holiday_calendar.add_holiday_rule(DayOfMonthHolidayRule(MonthDay.new_from(a_new_yers_day)))

        self.assertTrue(a_holiday_calendar.is_holiday(a_christmas))
        self.assertTrue(a_holiday_calendar.is_holiday(a_new_yers_day))

    def test_06_any_specific_date_can_be_holiday(self):
        a_holiday_calendar = HolidayCalendar()
        an_anniversary = date(2023, 8, 19)
        a_holiday_calendar.add_holiday_rule(SpecificDateHolidayRule(an_anniversary))
        self.assertTrue(a_holiday_calendar.is_holiday(an_anniversary))

    def test_07_more_then_one_specific_date_can_be_holiday(self):
        a_holiday_calendar = HolidayCalendar()
        a_aniversary = date(2022, 8, 19)
        a_holiday_calendar.add_holiday_rule(SpecificDateHolidayRule((a_aniversary)))
        another_aniversary = date(2022, 9, 19)
        a_holiday_calendar.add_holiday_rule(SpecificDateHolidayRule((another_aniversary)))
        self.assertTrue(a_holiday_calendar.is_holiday(a_aniversary))
        self.assertTrue(a_holiday_calendar.is_holiday(another_aniversary))

    def test_08_date_that_matches_holiday_rule_and_is_in_interval_is_holiday(self):
        a_holiday_calendar = HolidayCalendar()
        a_monday = date(2023, 1, 2)
        start_date = date(2023, 1, 1)
        end_date = date(2023, 12, 31)
        a_week_holiday_rule = DayOfWeekHolidayRule(a_monday.weekday())
        a_date_interval = DateInterval(start_date, end_date)
        a_holiday_calendar.add_holiday_rule(TemporaryHolidayRule(a_week_holiday_rule, a_date_interval))

        self.assertTrue(a_holiday_calendar.is_holiday(a_monday))

    def test_09(self):
        a_holiday_calendar = HolidayCalendar()
        start_date = date(2023, 1, 1)
        end_date = date(2023, 12, 31)
        a_date_interval = DateInterval(start_date, end_date)
        a_monday_outside_interval = date(2022, 12, 26)
        a_week_holiday_rule = DayOfWeekHolidayRule(a_monday_outside_interval.weekday())
        a_holiday_calendar.add_holiday_rule(TemporaryHolidayRule(a_week_holiday_rule, a_date_interval))

        self.assertFalse(a_holiday_calendar.is_holiday(a_monday_outside_interval))

    def test_10(self):
        a_holiday_calendar = HolidayCalendar()
        start_date = date(2023, 1, 1)
        end_date = date(2023, 12, 31)
        a_date_interval = DateInterval(start_date, end_date)
        a_monday_within_interval = date(2023, 1, 2)
        a_week_holiday_rule = DayOfWeekHolidayRule(4) #4 es viernes
        a_holiday_calendar.add_holiday_rule(TemporaryHolidayRule(a_week_holiday_rule, a_date_interval))

        self.assertFalse(a_holiday_calendar.is_holiday(a_monday_within_interval))

if __name__ == '__main__':
    unittest.main()
