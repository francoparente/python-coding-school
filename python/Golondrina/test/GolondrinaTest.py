import unittest

from source.Golondrina import Golondrina


class GolondrinaTest(unittest.TestCase):
    def test_vuela_10km(self):
        Golondrina().volar(100)
        self.assertEqual(100, Golondrina().distancia())



if __name__ == '__main__':
    unittest.main()
