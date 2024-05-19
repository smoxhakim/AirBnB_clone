#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    This class handles the serialization and deserialization of instances
    for the application.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects in the FileStorage."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the FileStorage dictionary."""
        key = "{}.{}".format(obj.to_dict()['__class__'], obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves the FileStorage data to a file."""
        dictionary = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dictionary, file, indent=4)

    def reload(self):
        """Reloads the FileStorage data from a file."""
        try:
            with open(FileStorage.__file_path, "r") as file:
                dictionary = json.load(file)
            for key, value in dictionary.items():
                cls_name = value['__class__']
                cls = eval(cls_name)
                self.new(cls(**value))
        except FileNotFoundError:
            pass
