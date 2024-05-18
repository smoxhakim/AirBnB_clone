#!/usr/bin/python3
"""HBNBCommand class"""

import cmd
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review

from models.engine.file_storage import FileStorage


"""HBNBCommand class"""


class HBNBCommand(cmd.Cmd):
    """classes: Dictionary mapping class names to their corresponding classes.
    file_name: Name of the file to store data.
    prompt: Prompt displayed for the command line.
    storage: Instance of FileStorage class for data storage.
    """
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "Place": Place,
        "State": State,
        "Amenity": Amenity,
        "Review": Review,
    }
    file_name = "file.json"
    prompt = "(hbnb) "
    storage = FileStorage()

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        exit()

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)
        """
        print()
        exit()

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of a specified class and saves it to the file.
        """
        args_list = args.split()
        class_name = args_list[0] if args_list else None
        instance = HBNBCommand.classes[class_name]()

        if class_name is None:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Shows the specified instance of a class.
        """
        args_list = args.split()
        objects_dictionary = HBNBCommand.storage.all()

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) == 2:
            class_id = args_list[1]

        obj_key = f"{class_name}.{class_id}"
        lookup_result = objects_dictionary.get(obj_key,
                                               "** no instance found **")

        if not isinstance(lookup_result, dict):
            print(lookup_result)
        else:
            obj = BaseModel(**lookup_result)
            print(obj)

    def do_destroy(self, args):
        """Destroys a specified instance of a class.
        """
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) == 2:
            class_id = args_list[1]

        obj_key = f"{class_name}.{class_id}"
        objects_dictionary = HBNBCommand.storage.all()
        if obj_key not in objects_dictionary:
            print("** no instance found **")
            return

        del objects_dictionary[obj_key]
        HBNBCommand.storage.save()

    def do_all(self, args):
        """Lists all instances of a specified class.
        """
        args_list = args.split()
        object_list = []
        obj_dict = HBNBCommand.storage.all()
        class_name = args_list[0] if args_list else None

        if class_name is None:
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        for obj_value in obj_dict.values():
            instance = BaseModel(**obj_value)
            object_list.append(instance)

        string_representations = [obj.__str__() for obj in object_list]
        print(string_representations)

    def do_update(self, arg):
        """Updates an instance based on class name and
        id by adding or updating attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key not in HBNBCommand.storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            objects = HBNBCommand.storage.all()
            # check if the attribute passed by the user
            # exist in the key's value dictionary
            if attr_name in objects[key]:
                # convert the user type to the existing attribute type
                original_attribute = objects[key][attr_name]
                original_attribute_type = type(original_attribute)
                attr_value = original_attribute_type(attr_value)

            value_dictionary = objects[key]
            value_dictionary[attr_name] = attr_value
            HBNBCommand.storage.save()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    """This script is the main entry point for
    the consoleof the AirBnB application.

    It creates an instance of the HBNBCommand
    class and starts the command loop.
    """
    HBNBCommand().cmdloop()
