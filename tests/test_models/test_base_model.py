#!/usr/bin/python3
"""Unit the for baseMOdel """
import unittest
from models.base_model import BaseModel
from uuid import UUID
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.value = BaseModel
        self.name = 'BaseModel'

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init_with_id(self):
        base_model = BaseModel(id="test_id")
        self.assertEqual(base_model.id, "test_id")

    def test_default(self):
        x = self.value()
        self.assertEqual(type(x), self.value)

    def test_with_save(self):
        js = 'file.json'
        x = self.value()
        x.save()
        KEY_ = self.name + "." + x.id
        with open(js, 'r') as Fl:
            j = json.load(Fl)
            self.assertEqual(j[KEY_], x.to_dict())

    def test_with_str(self):
        x = self.value()
        y = '[{}] ({}) {}'.format(self.name, x.id, x.__dict__)
        self.assertEqual(str(x), y)

    def test_to_dict(self):
        ins = self.value()
        N = ins.to_dict()
        self.assertEqual(ins.to_dict(), N)

    def test_for_id(self):
        NEW_ = self.value()
        self.assertEqual(type(NEW_.id), str)

    def test_created_at(self):
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_save_updates_updated_at(self):
        _baseMod = BaseModel()
        old_updated_at = _baseMod.updated_at
        _baseMod.save()

    def test_to_dict_keys(self):
        _baseMod = BaseModel()
        obj_dict = _baseMod.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(list(obj_dict.keys()), expected_keys)


if __name__ == "__main__":
    unittest.main()
