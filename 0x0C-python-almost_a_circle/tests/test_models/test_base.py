#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_obj = Rectangle(10, 7, 2, 8)

    def test_instance_id(self):
        self.assertIsNot(self.my_obj.id, None)

    def test_class_instance(self):
        self.assertIsInstance(self.my_obj, Base)

    def test_to_json_method(self):
        dictionary = self.my_obj.to_dictionary()
        json_str = Base.to_json_string([dictionary])
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_str, str)

if __name__ == "__main__":
    unittest.main()
