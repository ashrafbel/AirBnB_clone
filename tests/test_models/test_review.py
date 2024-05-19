#!/usr/bin/python3
"define unittest for review"
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def test_inheritance_rv(self):
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes_rv(self):
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_from_dict_rv(self):
        rv = self.review.to_dict()
        NEW_ = Review(**rv)
        self.assertIsInstance(NEW_, Review)
        self.assertEqual(NEW_.place_id, "")
        self.assertEqual(NEW_.user_id, "")
        self.assertEqual(NEW_.text, "")
        self.assertIsInstance(NEW_.created_at, datetime)
        self.assertIsInstance(NEW_.updated_at, datetime)

    def test_str_rv(self):
        expected = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected)

    def test_review_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertIsInstance(review_dict["created_at"], str)
        self.assertIsInstance(review_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
