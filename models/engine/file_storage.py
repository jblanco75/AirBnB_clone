#!/usr/bin/python3
"""This module contains 'FileStorage',
the class which serializes/deserializes to/from JSON"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """Serializes instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_1 = {}
        for key, value in FileStorage.__objects.items():
            dict_1[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as save_file:
            json.dump(dict_1, save_file)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                file_object = json.load(file)
                for key, value in file_object.items():
                    object = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = object
        except FileNotFoundError:
            pass
