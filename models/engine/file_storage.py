#!/usr/bin/python3
""""""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """"""
        return FileStorage.__objects

    def new(self, obj):
        """"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """"""
        dict_1 = {}
        for key, value in FileStorage.__objects.items():
            dict_1[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as save_file:
            json.dump(dict_1, save_file)

    def reload(self):
        """"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                file_object = json.load(file)
                for key, value in file_object.items():
                    FileStorage.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
