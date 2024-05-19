#!/usr/bin/python3
"Unittest for file_storage"
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        self.test_model = BaseModel()
        self.test_model.name = "TestModel"

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_new(self):
        self.storage.new(self.test_model)
        KEY_ = f"BaseModel.{self.test_model.id}"
        self.assertIn(KEY_, self.storage.all())
        self.assertEqual(self.storage.all()[KEY_], self.test_model)

    def test_save(self):
        self.storage.new(self.test_model)
        self.storage.save()
        with open(self.file_path, "r") as file:
            D = json.load(file)
        KEY_ = f"BaseModel.{self.test_model.id}"
        self.assertEqual(D[KEY_], self.test_model.to_dict())
        self.assertIn(KEY_, D)

    def test_all(self):
        self.storage.new(self.test_model)
        obj_ = self.storage.all()
        self.assertIn(f"BaseModel.{self.test_model.id}", obj_)

    def test_reload(self):
        self.storage.new(self.test_model)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        KEY_ = f"BaseModel.{self.test_model.id}"
        self.assertIn(KEY_, self.storage.all())
        self.assertEqual(self.storage.all()[KEY_].id, self.test_model.id)
        self.assertEqual(self.storage.all()[KEY_].name, self.test_model.name)


if __name__ == '__main__':
    unittest.main()
