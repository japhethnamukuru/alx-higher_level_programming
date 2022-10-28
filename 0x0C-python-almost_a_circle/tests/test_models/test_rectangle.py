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


class TestRectangleAttributes(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(1, 2)

    def test_width_exception(self):
        with self.assertRaises(TypeError):
            self.rect1 = Rectangle('1', 2)

        with self.assertRaises(ValueError):
            self.rect2 = Rectangle(-1, 3)


    def test_height_exception(self):
        with self.assertRaises(TypeError):
            self.obj = Rectangle(1, '2')

        with self.assertRaises(ValueError):
            self.obj1 = Rectangle(2, -1)

    def test_x_exception(self):
        with self.assertRaises(TypeError):
            self.rect3 = Rectangle(1, 1, '1')

        with self.assertRaises(ValueError):
            self.rect3 = Rectangle(1, 1, -2)

    def test_y_exception(self):
        with self.assertRaises(TypeError):
            self.rect = Rectangle(1, 1, 1, '1')

        with self.assertRaises(ValueError):
            self.rect = Rectangle(1, 1, 1, -2)


class TestRectangleMethods(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(3, 4)

    def test_rectangle_area_method(self):
        self.assertEqual(self.rect.area(), 12)


if __name__ == '__main__':
    unittest.main()
