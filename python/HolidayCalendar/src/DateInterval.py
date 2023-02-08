class DateInterval:
    ERROR_INVALID_INTERVAL = "Invalid interval"

    def __init__(self, a_start_date, an_end_date):
        self.assert_valid_interval(a_start_date, an_end_date)
        self._end_date = an_end_date
        self._start_date = a_start_date

    def assert_valid_interval(self, a_start_date, an_end_date):
        if a_start_date >= an_end_date:
            raise Exception(DateInterval.ERROR_INVALID_INTERVAL)

    def includes(self, date_within_interval):
        return self._start_date <= date_within_interval <= self._end_date
