import unittest
from datetime import date

from DateInterval import DateInterval


class DateIntervalTest(unittest.TestCase):
    def test_01_start_date_must_be_before_end_date(self):
        start_date = date(2023, 12, 20)
        end_date = date(2022, 12, 20)

        try:
            DateInterval(start_date, end_date)
            self.fail()
        except Exception as error:
            self.assertEqual(DateInterval.ERROR_INVALID_INTERVAL, str(error))

    def test_02_an_interval_can_include_a_date(self):
        start_date = date(2022, 12, 20)
        end_date = date(2023, 12, 20)
        date_within_interval = date(2022, 12, 25)
        a_date_interval = DateInterval(start_date, end_date)

        self.assertTrue(a_date_interval.includes(date_within_interval))

    def test_03_an_interval_does_not_include_a_date_before_start_date(self):
        start_date = date(2022, 12, 20)
        end_date = date(2023, 12, 20)
        date_not_within_interval = date(2019, 12, 25)
        a_date_interval = DateInterval(start_date, end_date)

        self.assertFalse(a_date_interval.includes(date_not_within_interval))

    def test_04_an_interval_does_not_include_a_date_after_start_date(self):
        start_date = date(2022, 12, 20)
        end_date = date(2023, 12, 20)
        date_not_within_interval = date(2029, 12, 25)
        a_date_interval = DateInterval(start_date, end_date)

        self.assertFalse(a_date_interval.includes(date_not_within_interval))

    def test_05_an_interval_includes_its_starting_and_ending_date(self):
        start_date = date(2022, 12, 20)
        end_date = date(2023, 12, 20)
        a_date_interval = DateInterval(start_date, end_date)

        self.assertTrue(a_date_interval.includes(start_date))
        self.assertTrue(a_date_interval.includes(end_date))

if __name__ == '__main__':
    unittest.main()
