import unittest

from source.Point import Point


class CartesianCoordinatesTest(unittest.TestCase):
    def test_x_coordinate_of_point_five_three_is_five(self):
        self.assertEqual(5, Point(5, 3).x())

    def test_y_coordinate_of_point_five_three_is_three(self):
        self.assertEqual(3, Point(5, 3).y())

    def test_x_coordinate_of_point_seven_four_is_seven(self):
        self.assertEqual(7, Point(7, 4).x())

    def test_y_coordinate_of_point_seven_four_is_four(self):
        self.assertEqual(4, Point(7, 4).y())



if __name__ == '__main__':
    unittest.main()
