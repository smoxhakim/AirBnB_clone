#!/usr/bin/python3

import json
import os
from datetime import datetime
import copy

class FileStorage:
    __file_path: str = "file.json"
    __objects: dict = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__+"."+obj.id] = obj.__dict__

    def save(self):
        new_dictionary = {}
        for key, value in FileStorage.__objects.items():
            new_dictionary[key] = FileStorage.convert_datetime_to_str(value)


        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "w") as f:
                json.dump(new_dictionary, f)
                f.write("\n")

        elif not os.path.exists(FileStorage.__file_path):
            try:
                os.mknod(FileStorage.__file_path)
                with open(FileStorage.__file_path, "w") as f:
                    json.dump(new_dictionary, f)
                    f.write("\n")
            except Exception as e:
                print(e)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    FileStorage.__objects = json.load(f)
            except json.JSONDecodeError as e:
                print("Maybe the JSON file is corrupted")
                return
        else:
            return

    @staticmethod
    def convert_datetime_to_str(value):
        if isinstance(value, dict):
            new_dict = {}
            for k, v in value.items():
                new_dict[k] = FileStorage.convert_datetime_to_str(v)
            return new_dict
        elif isinstance(value, datetime):
            return value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        else:
            return value
