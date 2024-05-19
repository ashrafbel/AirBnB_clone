#!/usr/bin/python3
"define unittest for place"
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_place_inheritance(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_place_to_dict(self):
        ptodic = self.place.to_dict()
        self.assertIsInstance(ptodic, dict)
        self.assertIsInstance(ptodic["created_at"], str)
        self.assertIsInstance(ptodic["updated_at"], str)

    def test_attr(self):
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.user_id, str)
        self.assertIsInstance(self.place.name, str)

    def test_str(self):
        exp = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), exp)


if __name__ == "__main__":
    unittest.main()
