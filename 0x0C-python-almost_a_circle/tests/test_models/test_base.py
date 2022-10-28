#!/usr/bin/python3

import unittest
from models.base import Base

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_obj = Base()

    def test_instance_id(self):
        self.assertIsNot(self.my_obj.id, None)

    def test_class_instance(self):
        self.assertIsInstance(self.my_obj, Base)

if __name__ == "__main__":
    unittest.main()
