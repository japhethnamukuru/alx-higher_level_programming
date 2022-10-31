#!/usr/bin/python3

"""Square model test suite"""

from models.square import Square
import unittest


class TestSquareattributes(unittest.TestCase):
    def setUp(self):
        self.sq = Square(5)

    def test_size_attribute(self):
        self.assertEqual(self.sq.size, 5)

    def test_square_area_method(self):
        self.assertEqual(self.sq.area(), 25)

    def test_update_method_args_id(self):
        self.asserEqual(self.sq.id, 1)

    def test_update_method_args_id(self):
        self.sq.update(10)
        self.assertEqual(self.sq.id, 10)

    def test_update_method_args_size(self):
        self.sq.update(1, 2)
        self.assertEqual(self.sq.size, 2)

    def test_update_method_args_x(self):
        self.sq.update(1, 2, 3)
        self.assertEqual(self.sq.x, 3)

    def test_update_method_args_y(self):
        self.sq.update(1, 2, 3, 4)
        self.assertEqual(self.sq.y, 4)
