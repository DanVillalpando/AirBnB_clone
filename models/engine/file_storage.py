#!/usr/bin/python3
"""
5. Store first object
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key
	<obj class name>.id
        """
        if obj:
            self.__objects["{}.{}".format(
                obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON
	file (path: __file_path)
        """
        new_d = {}
        for key, va in self.__objects.items():
            new_d[key] = va.to_dict()
        with open(self.__file_path, "w", encoding="UTF-8") as MyFile:
            json.dump(new_d, MyFile)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
	otherwise, do nothing.
        """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as MyFile:
                obj = json.load(MyFile)
                for key, va in obj.items():
                    class_name = key.split('.')[0]
                    self.__objects[key] = eval(class_name)(**va)
        except:
            pass
