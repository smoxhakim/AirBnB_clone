#!/usr/bin/python3

import json
import os

class FileStorage:
    __file_path: str = "file.json"
    __objects: dict = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__+"."+obj.id] = obj.to_dict()
        

    def save(self):
        #Converting datetime objects into a string before dumping them into a JSON file
        #datetime objectes are not serializable
        # new_dictionary = {}
        # for key, value in FileStorage.__objects.items():
        #     new_dictionary[key] = FileStorage.DatetimeEncoder(value)


        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "w") as f:
                    json.dump(FileStorage.__objects, f, indent=4)
            except Exception:
                print(f"The file {FileStorage.__file_path} exists but was enable to dump into it")
        elif not os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "w") as f:
                    json.dump(FileStorage.__objects, f, indent=4)
            except Exception as e:
                print(e)
                return

    def reload(self):
        if (os.path.exists(FileStorage.__file_path) and
            os.path.getsize(FileStorage.__file_path) != 0):
                try:
                    with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                        FileStorage.__objects = json.load(f)
                except json.JSONDecodeError as e:
                    print("Something went wrong loading objects from the JSON file")
                    print("Hint: Check for errors in the JSON file")
                    return
                except Exception as e:
                    print(e)
        else:
            return

    # @staticmethod
    # def DatetimeEncoder(value):
    #     if isinstance(value, dict):
    #         new_dict = {}
    #         for k, v in value.items():
    #             new_dict[k] = FileStorage.DatetimeEncoder(v)
    #         return new_dict
    #     elif isinstance(value, datetime):
    #         return value.strftime("%Y-%m-%dT%H:%M:%S.%f")
    #     else:
    #         return value
