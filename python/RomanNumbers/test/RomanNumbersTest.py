import unittest

from src.RomanNumberTextRepresentation import RomanNumberTextRepresentation

class RomanNumbersTest(unittest.TestCase):
    def test_negative_numbers_have_no_roman_representation(self):
        try:
            RomanNumberTextRepresentation().of(-1)
            self. fail('Esperaba una excepción')
        except ValueError as error:
            error_message = error.args[0]
            self.assertEqual('Los números no positivos no tienen representación romana', error_message)

    def test_zero_has_no_roman_representation(self):
        try:
            RomanNumberTextRepresentation().of(0)
            self. fail('Esperaba una excepción')
        except ValueError as error:
            error_message = error.args[0]
            self.assertEqual('Los números no positivos no tienen representación romana', error_message)

    def test_001_to_003(self):
        self.assertEqual('I', RomanNumberTextRepresentation().of(1))
        self.assertEqual('II', RomanNumberTextRepresentation().of(2))
        self.assertEqual('III', RomanNumberTextRepresentation().of(3))

    def test_004(self):
        self.assertEqual('IV', RomanNumberTextRepresentation().of(4))

    def test_005_to_008(self):
        self.assertEqual('V', RomanNumberTextRepresentation().of(5))
        self.assertEqual('VI', RomanNumberTextRepresentation().of(6))
        self.assertEqual('VII', RomanNumberTextRepresentation().of(7))
        self.assertEqual('VIII', RomanNumberTextRepresentation().of(8))

    def test_009(self):
        self.assertEqual('IX', RomanNumberTextRepresentation().of(9))

    def test_010(self):
        self.assertEqual('X', RomanNumberTextRepresentation().of(10))

    def test_011(self):
        self.assertEqual('XI', RomanNumberTextRepresentation().of(11))

    def test_012(self):
        self.assertEqual('XII', RomanNumberTextRepresentation().of(12))

    def test_013(self):
        self.assertEqual('XIII', RomanNumberTextRepresentation().of(13))

    def test_014(self):
        self.assertEqual('XIV', RomanNumberTextRepresentation().of(14))

    def test_015_to_018(self):
        self.assertEqual('XV', RomanNumberTextRepresentation().of(15))
        self.assertEqual('XVI', RomanNumberTextRepresentation().of(16))
        self.assertEqual('XVII', RomanNumberTextRepresentation().of(17))
        self.assertEqual('XVIII', RomanNumberTextRepresentation().of(18))

    def test_019(self):
        self.assertEqual('XIX', RomanNumberTextRepresentation().of(19))

    def test_020_to_029(self):
        self.assertEqual('XX', RomanNumberTextRepresentation().of(20))
        self.assertEqual('XXIV', RomanNumberTextRepresentation().of(24))
        self.assertEqual('XXIX', RomanNumberTextRepresentation().of(29))

    def test_030_to_039(self):
        self.assertEqual('XXX', RomanNumberTextRepresentation().of(30))
        self.assertEqual('XXXIV', RomanNumberTextRepresentation().of(34))
        self.assertEqual('XXXIX', RomanNumberTextRepresentation().of(39))

    def test_040_to_049(self):
        self.assertEqual('XL', RomanNumberTextRepresentation().of(40))
        self.assertEqual('XLIV', RomanNumberTextRepresentation().of(44))
        self.assertEqual('XLIX', RomanNumberTextRepresentation().of(49))

    def test_050_to_059(self):
        self.assertEqual('L', RomanNumberTextRepresentation().of(50))
        self.assertEqual('LIV', RomanNumberTextRepresentation().of(54))
        self.assertEqual('LIX', RomanNumberTextRepresentation().of(59))

    def test_060_to_089(self):
        self.assertEqual('LX', RomanNumberTextRepresentation().of(60))
        self.assertEqual('LXXIV', RomanNumberTextRepresentation().of(74))
        self.assertEqual('LXXXIX', RomanNumberTextRepresentation().of(89))

    def test_090_to_099(self):
        self.assertEqual('XC', RomanNumberTextRepresentation().of(90))
        self.assertEqual('XCIV', RomanNumberTextRepresentation().of(94))
        self.assertEqual('XCIX', RomanNumberTextRepresentation().of(99))

    def test_100_to_999(self):
        self.assertEqual('C', RomanNumberTextRepresentation().of(100))
        self.assertEqual('CDXLIV', RomanNumberTextRepresentation().of(444))
        self.assertEqual('CMXCIX', RomanNumberTextRepresentation().of(999))

if __name__ == '__main__':
    unittest.main()
