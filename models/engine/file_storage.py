#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User


"""FileStorage Module"""


class FileStorage:
    """This class handles the serialization and deserialization of instances
    for the application.

    Methods:
        all(self): Returns all objects in the FileStorage.
        new(self, obj): Adds a new object to the FileStorage dictionary.
        save(self): Saves the FileStorage data to a file.
        reload(self): Reloads the FileStorage data from a
        file if the file exists and is not empty.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects in the FileStorage.

        Parameters:
            self

        Returns:
            dict: A dictionary containing all objects
            stored in the FileStorage.
        """
        return FileStorage.__objects

    def new(self, obj):
        """new(self, obj) - Adds a new object to the FileStorage dictionary

        Parameters:
            self
            obj: object - The object to be added to the dictionary

        Returns:
            None
        """
        FileStorage.__objects["{}.{}\
".format(obj.to_dict()['__class__'], obj.id)] = obj

    def save(self):
        """Saves the FileStorage data to a file.

        If the file path exists, it writes the FileStorage objects
        to the file in JSON format with an indentation of 4 spaces.

        If the file path does not exist, it creates the file and writes
        the FileStorage objects to it in JSON format with an indentation
        of 4 spaces.

        Parameters:
            self

        Returns:
            None
        """
        dictionary = {}
        for key in FileStorage.__objects:
            dictionary[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(dictionary))

    def reload(self):
        """Reloads the FileStorage data from a file
        if the file exists and is not empty.

        It reads the JSON data from the file and
        updates the FileStorage objects.

        Parameters:
            self

        Returns:
            None
        """
                


        try:
            with open(FileStorage.__file_path, "r") as file:
                dictionary = json.loads(file.read())
            for key in dictionary:
                self.new(eval(dictionary[key]["__class__"])(**dictionary[key]))
        except IOError:
            pass
