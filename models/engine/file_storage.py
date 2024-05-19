#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    "class for serializing instances to JSON files & deserializing them back."

    JSON_ = "file.json"
    __file_path = JSON_
    __objects = {}

    def all(self):
        "Returns the dictionary containing the stored objects."
        Obj_ = FileStorage.__objects
        return Obj_

    def new(self, obj):
        "Adds an object to the storage."
        name_class_object = obj.__class__.__name__
        obj_id = obj.id
        FileStorage.__objects["{}.{}".format(name_class_object, obj_id)] = obj

    def save(self):
        "Serializes `__objects` to the JSON file at `__file_path`."
        data_serialz = {}
        StorageObj = FileStorage.__file_path
        File_obj_items = FileStorage.__objects.items()
        for KEY, Val in File_obj_items:
            data_serialz[KEY] = Val.to_dict()
            with open(StorageObj, "w") as fl:
                fl.write(json.dumps(data_serialz))

    def reload(self):
        "Deserialize the JSON file at f_path into obj  if the file exists."
        try:
            with open(self.__file_path, "r") as Fl:
                json_dict = json.load(Fl)
                for KEY_, Val in json_dict.items():
                    class_name = Val["__class__"]
                    self.__objects[KEY_] = eval(class_name)(Val)
        except FileNotFoundError:
            pass
