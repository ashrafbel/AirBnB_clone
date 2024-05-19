#!/usr/bin/python3
"define unittest for state"
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_inheritance(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_attr(self):
        self.assertEqual(self.state.name, "")
        self.assertIsInstance(self.state.name, str)

    def test_state_str_(self):
        expe = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expe)

    def test_state_to_dict(self):
        statetodic = self.state.to_dict()
        self.assertIsInstance(statetodic["created_at"], str)
        self.assertIsInstance(statetodic["updated_at"], str)
        self.assertIsInstance(statetodic, dict)
        self.assertEqual(statetodic["__class__"], "State")
        


    def test_state_from_dict(self):
        state_dict = self.state.to_dict()
        NEW_ = State(**state_dict)
        self.assertIsInstance(NEW_, State)
        self.assertEqual(NEW_.name, "")
        self.assertIsInstance(NEW_.created_at, datetime)
        self.assertIsInstance(NEW_.updated_at, datetime)

if __name__ == "__main__":
    unittest.main()
