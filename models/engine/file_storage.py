#!/usr/bin/python3

import json
import os

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
    __file_path: str = "file.json"
    __objects: dict = dict()

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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj.to_dict()

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
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "w") as f:
                    json.dump(FileStorage.__objects, f)
            except Exception as e:
                print(e)
        elif not os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "w") as f:
                    json.dump(FileStorage.__objects, f)
            except Exception as e:
                print(e)
                return

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
        if (os.path.exists(FileStorage.__file_path) and
                os.path.getsize(FileStorage.__file_path) != 0):
            try:
                with open(FileStorage.__file_path, mode='r',
                          encoding='utf-8') as f:
                    FileStorage.__objects = json.load(f)
            except json.JSONDecodeError as e:
                print("Error Decoding Json")
                return
            except Exception as e:
                print(e)
                return
        else:
            return
