#
# Developed by 10Pines SRL
# License:
# This work is licensed under the
# Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
# or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View,
# California, 94041, USA.
#

class CustomerBook:

    ERROR_CUSTOMER_NAME_CAN_NOT_BE_EMPTY = 'Customer name must not be empty'
    ERROR_CUSTOMER_ALREADY_EXISTS = 'Customer already exists'
    ERROR_INVALID_CUSTOMER_NAME = 'Invalid customer name'

    def __init__(self):
        self._customer_names = set()

    def add_customer_named(self, name):
        self._assert_name_is_not_empty(name)
        self._assert_customer_exists(name)

        self._customer_names.add(name)

    def _assert_customer_exists(self, name):
        if self.includes_customer_named(name):
            raise ValueError(CustomerBook.ERROR_CUSTOMER_ALREADY_EXISTS)

    def _assert_name_is_not_empty(self, name):
        if not name:
            raise ValueError(CustomerBook.ERROR_CUSTOMER_NAME_CAN_NOT_BE_EMPTY)

    def is_empty(self):
        return self.number_of_customers() == 0

    def number_of_customers(self):
        return len(self._customer_names)

    def includes_customer_named(self, name):
        return name in self._customer_names

    def remove_customer_named(self, name):
        # Esta validacion mucho sentido no tiene, pero está puesta por motivos del ejericio
        if not self.includes_customer_named(name):
            raise KeyError(CustomerBook.ERROR_INVALID_CUSTOMER_NAME)

        self._customer_names.remove(name)
