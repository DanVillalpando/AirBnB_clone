#!/usr/bin/python3
"""
5. Store first object
"""

import json

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
           obj = self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)]

    def save(self):
        """
        Serializes __objects to the JSON 
	file (path: __file_path)
        """
        new_d = {}
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
        except:
            pass
