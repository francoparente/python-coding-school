from src.Clock import Clock

class ManualClock(Clock):
    def __init__(self, a_datetime):
        self._current_datetime = a_datetime

    def today(self):
        return self._current_datetime

    def advance(self, a_duration):
        self._current_datetime += a_duration
