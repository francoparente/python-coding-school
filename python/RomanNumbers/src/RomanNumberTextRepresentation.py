class RomanNumberTextRepresentation:
    def of(self, a_number):
        self.assert_is_positive(a_number)

        hundreds, tens, units = self.positional_digits_of(a_number)

        return self.digit_as_roman_text(hundreds, 'C', 'D', 'M') + \
               self.digit_as_roman_text(tens, 'X', 'L', 'C') + \
               self.digit_as_roman_text(units, 'I', 'V', 'X')

    def assert_is_positive(self, a_number):
        if a_number <= 0:
            raise ValueError('Los números no positivos no tienen representación romana')

    def positional_digits_of(self, a_number):
        hundreds = a_number // 100
        tens = (a_number - 100 * hundreds) // 10
        units = a_number - (100 * hundreds) - (10 * tens)
        return hundreds, tens, units

    def digit_as_roman_text(self, a_digit, as_one, as_five, as_ten):
        if a_digit <= 3:
            return as_one * a_digit

        if a_digit == 4:
            return as_one + as_five

        if 5 <= a_digit <= 8:
            return as_five + as_one * (a_digit - 5)

        if a_digit == 9:
            return as_one + as_ten
