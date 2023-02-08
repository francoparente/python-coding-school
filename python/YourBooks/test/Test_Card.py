import unittest

from src.Card import Card
from tests.TestObjectsFactory import TestObjectsFactory


class CardTest(unittest.TestCase):
    def setUp(self):
        self._factory = TestObjectsFactory()

    def test_cannot_checkout_with_invalid_card_number(self):
        try:
            self._factory.an_invalid_card()
            self.fail()
        except Exception as error:
            self.assertEqual(Card.ERROR_INVALID_CARD, str(error))


if __name__ == '__main__':
    unittest.main()
