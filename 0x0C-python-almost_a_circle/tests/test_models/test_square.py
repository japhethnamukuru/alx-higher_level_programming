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
