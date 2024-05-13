#!/usr/bin/python3

import json

class FileStorage:
    __file_path: str = str()
    __objects: dict = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__+"."+obj.id] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        try:
            FileStorage.__objects = json.load(FileStorage.__file_path)
        except FileNotFoundError:
            return
