#!/usr/bin/python3
"Unittest user"
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_attr_user(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_type_user(self): 
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)

    def test_str(self):
        exp = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), exp)


    def test_from_dict(self):
        ud = self.user.to_dict()
        NEW_ = User(**ud)
        self.assertIsInstance(NEW_, User)
        self.assertEqual(NEW_.email, "")
        self.assertEqual(NEW_.password, "")
        self.assertEqual(NEW_.first_name, "")
        self.assertEqual(NEW_.last_name, "")
        self.assertIsInstance(NEW_.created_at, datetime)
        self.assertIsInstance(NEW_.updated_at, datetime)
    
    def test_user_to_dict(self):
        usertodict = self.user.to_dict()
        self.assertIsInstance(usertodict, dict)
        self.assertEqual(usertodict["__class__"], "User")
        self.assertIsInstance(usertodict["created_at"], str)
        self.assertIsInstance(usertodict["updated_at"], str)

if __name__ == "__main__":
    unittest.main()
