#!/usr/bin/python3
"""Unit test amenity class."""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attre(self):
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.name, str)

    def test_to_dict(self):
        a = self.amenity.to_dict()
        self.assertIsInstance(a["created_at"], str)
        self.assertIsInstance(a["updated_at"], str)
        self.assertIsInstance(a, dict)
        self.assertEqual(a["__class__"], "Amenity")

    def test_from_dict(self):
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertIsInstance(new_amenity, Amenity)
        self.assertIsInstance(new_amenity.created_at, datetime)
        self.assertIsInstance(new_amenity.updated_at, datetime)

    def test_representation_str(self):
        exp = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), exp)


if __name__ == "__main__":
    unittest.main()
