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
        self.rect1 = Rectangle(4, 6, 2, 1, 12)

    def test_rectangle_area_method(self):
        self.assertEqual(self.rect.area(), 12)

    def test_rectangle_update_method_args_id(self):
        self.rect1.update(89)
        self.assertEqual(self.rect1.id, 89)

    def test_rectangle_update_method_args_width(self):
        self.rect1.update(89, 2)
        self.assertEqual(self.rect1.width, 2)

    def test_rectangle_update_method_args_height(self):
        self.rect1.update(89, 2, 3)
        self.assertEqual(self.rect1.height, 3)

    def test_rectangle_update_method_args_x(self):
        self.rect1.update(89, 2, 3, 4)
        self.assertEqual(self.rect1.x, 4)

    def test_rectangle_update_method_args_y(self):
        self.rect1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.rect1.y, 5)


    def test_update_method_kwargs_height(self):
        self.rect1.update(height=1)
        self.assertEqual(self.rect1.height, 1)

    def test_rectangle_method_kwargs_width(self):
        self.rect1.update(width=1, x=2)
        self.assertEqual(self.rect1.width, 1)
        self.assertEqual(self.rect1.x, 2)

    def test_rectangle_method_kwargs_y(self):
        self.rect1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(self.rect1.y, 1)
        self.assertEqual(self.rect1.width, 2)
        self.assertEqual(self.rect1.x, 3)
        self.assertEqual(self.rect1.id, 89)

    def test_update_method_kwargs_x(self):
        self.rect1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.rect1.x,1)
        self.assertEqual(self.rect1.height, 2)
        self.assertEqual(self.rect1.y, 3)
        self.assertEqual(self.rect1.width, 4)


if __name__ == '__main__':
    unittest.main()
