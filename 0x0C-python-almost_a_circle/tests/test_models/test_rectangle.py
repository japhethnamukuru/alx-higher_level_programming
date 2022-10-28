#!/usr/python3

"""REctangle tests"""
from models.rectangle import Rectangle
import unittest

class TestRectangleModel(unittest.TestCase):
    def setUp(self):
        self.obj = Rectangle(3, 4)

    def test_instance_width(self):
        self.assertEqual(self.obj.width, 3)

    def test_instance_height(self):
        self.assertEqual(self.obj.height, 4)

    def test_instance_x(self):
        self.assertEqual(self.obj.x, 0)

    def test_instance_y(self):
        self.assertEqual(self.obj.y, 0)

    def test_instance_id(self):
        self.assertIsNot(self.obj.id, None)

if __name__ == '__main__':
    unittest.main()
