#!/usr/bin/python3
"""Unit test City class."""
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_city_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_str_city(self):
        exp = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), exp)

    def test_todict(self):
        ct = self.city.to_dict()
        self.assertIsInstance(ct, dict)
        self.assertEqual(ct["__class__"], "City")
        self.assertIsInstance(ct["created_at"], str)
        self.assertIsInstance(ct["updated_at"], str)

    def test_from_dict(self):
        ct = self.city.to_dict()
        new_city = City(**ct)
        self.assertIsInstance(new_city, City)
        self.assertEqual(new_city.state_id, "")
        self.assertEqual(new_city.name, "")
        self.assertIsInstance(new_city.created_at, datetime)
        self.assertIsInstance(new_city.updated_at, datetime)

    def test_attr_city(self):
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
