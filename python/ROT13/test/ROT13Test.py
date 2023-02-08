import unittest

from src.ROT13 import ROT13


class ROT13Test(unittest.TestCase):
    def test_lower_letters_first_half(self):
        self.assertEqual('n', ROT13().rotate('a'))
        self.assertEqual('o', ROT13().rotate('b'))
        self.assertEqual('p', ROT13().rotate('c'))
        self.assertEqual('y', ROT13().rotate('l'))
        self.assertEqual('z', ROT13().rotate('m'))

    def test_lower_letters_second_half(self):
        self.assertEqual('a', ROT13().rotate('n'))
        self.assertEqual('b', ROT13().rotate('o'))
        self.assertEqual('k', ROT13().rotate('x'))
        self.assertEqual('l', ROT13().rotate('y'))
        self.assertEqual('m', ROT13().rotate('z'))

    def test_upper_letters_first_half(self):
        self.assertEqual('N', ROT13().rotate('A'))
        self.assertEqual('Z', ROT13().rotate('M'))

    def test_upper_letters_second_half(self):
        self.assertEqual('A', ROT13().rotate('N'))
        self.assertEqual('M', ROT13().rotate('Z'))

    def test_non_alpha_character_does_not_rotate(self):
        self.assertEqual('@', ROT13().rotate('@'))
        self.assertEqual('1', ROT13().rotate('1'))
        self.assertEqual(')', ROT13().rotate(')'))
        self.assertEqual('{', ROT13().rotate('{'))

    def test_non_english_letter_does_not_rotate(self):
        self.assertEqual('á', ROT13().rotate('á'))
        self.assertEqual('û', ROT13().rotate('û'))
        self.assertEqual('ò', ROT13().rotate('ò'))
        self.assertEqual('ë', ROT13().rotate('ë'))

    def test_more_than_one_character_conversion(self):
        self.assertEqual('UòYn1234@wczp.pbz', ROT13().rotate('HòLa1234@jpmc.com'))

    def test_no_character_conversion(self):
        self.assertEqual('', ROT13().rotate(''))


if __name__ == '__main__':
    unittest.main()
