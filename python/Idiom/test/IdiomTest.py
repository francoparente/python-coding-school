#
# Developed by 10Pines SRL
# License:
# This work is licensed under the
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
# or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View,
# California, 94041, USA.
#

import unittest
import time

from src.CustomerBook import CustomerBook


class IdiomTest(unittest.TestCase):

    def setUp(self):
        self.customer_book = CustomerBook()

    def measure_task_duration_in_milliseconds(self, task_to_measure):
        time_before_running = time.time()
        task_to_measure()
        time_after_running = time.time()
        task_duration = (time_after_running - time_before_running) * 1000
        return task_duration

    def test_adding_customer_should_not_take_more_than_50_milliseconds(self):
        task_duration = self.measure_task_duration_in_milliseconds(lambda: self.customer_book.add_customer_named("John Lennon"))

        self.assertLess(task_duration, 50)

    def test_removing_customer_should_not_take_more_than_100_milliseconds(self):
        # setup
        self.customer_book.add_customer_named("Paul McCartney")
        # exercise
        task_duration = self.measure_task_duration_in_milliseconds(lambda: self.customer_book.remove_customer_named("Paul McCartney"))
        # assert
        self.assertLess(task_duration, 100)

    def assert_raises_and_satisfies(self, task_to_try, exception_class, assertions):
        try:
            task_to_try()
            self.fail()
        except exception_class as exception:
            assertions(exception)

    def test_can_not_add_a_customer_with_empty_name(self):
        def assertions(exception):
            self.assertEquals(exception.args[0], CustomerBook.ERROR_CUSTOMER_NAME_CAN_NOT_BE_EMPTY)
            self.assertTrue(self.customer_book.is_empty())

        self.assert_raises_and_satisfies(
            lambda: self.customer_book.add_customer_named(''),
            ValueError,
            assertions
        )

    def test_can_not_remove_not_added_customer(self):
        self.customer_book.add_customer_named('Paul McCartney')

        def assertions(exception):
            self.assertEquals(exception.args[0], CustomerBook.ERROR_INVALID_CUSTOMER_NAME)
            self.assertEquals(self.customer_book.number_of_customers(), 1)
            self.assertTrue(self.customer_book.includes_customer_named('Paul McCartney'))

        self.assert_raises_and_satisfies(
            lambda: self.customer_book.remove_customer_named('John Lennon'),
            KeyError,
            assertions
        )


if __name__ == "__main__":
    unittest.main()
