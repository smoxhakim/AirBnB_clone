#!/usr/bin/python3
"""
HBNBCommand class for AirBnB clone project
"""

import cmd
import ast

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for AirBnB clone
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
    storage.reload()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

    def do_create(self, args):
        """Creates a new instance of a specified class and saves it"""
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instance = HBNBCommand.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, args):
        """Shows the specified instance of a class"""
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        class_id = args_list[1]
        objects_dictionary = HBNBCommand.storage.all()
        obj_key = f"{class_name}.{class_id}"

        if obj_key not in objects_dictionary:
            print("** no instance found **")
            return

        print(objects_dictionary[obj_key])

    def do_destroy(self, args):
        """Destroys a specified instance of a class"""
        args_list = args.split()

        if not args_list:
            print("** class name missing **")
            return

        class_name = args_list[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        class_id = args_list[1]
        obj_key = f"{class_name}.{class_id}"
        objects_dictionary = HBNBCommand.storage.all()

        if obj_key not in objects_dictionary:
            print("** no instance found **")
            return

        del objects_dictionary[obj_key]
        HBNBCommand.storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if arg:
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            class_name = arg
            obj_list = [str(obj) for obj in HBNBCommand.storage.all().values() if type(obj).__name__ == class_name]
        else:
            obj_list = [str(obj) for obj in HBNBCommand.storage.all().values()]
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        obj_key = f"{class_name}.{instance_id}"
        objects_dictionary = HBNBCommand.storage.all()

        if obj_key not in objects_dictionary:
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

        obj = objects_dictionary[obj_key]
        try:
            attr_value = ast.literal_eval(attr_value)
        except (ValueError, SyntaxError):
            pass

        setattr(obj, attr_name, attr_value)
        obj.save()
        
    def default(self, line):
        """
        default commands
        """
        if line.endswith(".all()"):
            """
            Check if the command matches
            <class_name>.all()
            """
            if line[:-6] != "":
                self.do_all(line[:-6])
        elif line.endswith(".count()"):
            """
            Check if the command matches
            <class_name>.count()
            """
            if line[:-8] != "":
                if line[:-8] in HBNBCommand.classes_list:
                    num_obj = 0
                    for key in storage.all():
                        if line[:-8] in key:
                            num_obj += 1
                    print(num_obj)
                else:
                    print("** class doesn't exist **")

        elif ".show(" in line and line.endswith(")"):
            """
            Check if the command matches
            <class_name>.show(<id>)
            """
            className = line.split(".")[0]
            id = line.split("(")[1][:-1]
            self.do_show(className+" "+id)

        elif ".destroy(" in line and line.endswith(")"):
            """
            Check if the command matches
            <class_name>.destroy(<id>)
            """
            className = line.split(".")[0]
            id = line.split("(")[1][:-1]
            self.do_destroy(className+" "+id)

        elif ".update(" in line and line.endswith(")"):
            className = line.split(".")[0]
            args = line.split("(")[1][:-1]
            if "{" in args and args.endswith("}"):
                id = args.split(", ")[0]
                str_dict = "{"+args.split("{")[1]
                dictionary = dict(eval(str_dict))
                string = className+" "+id
                for attr in dictionary:
                    self.do_update(string+" \
"+attr+" "+"\""+str(dictionary[attr])+"\"")
            else:
                string = className
                for elm in args.split(", "):
                    string += " "+elm
                self.do_update(string)
        else:
            print("*** Unknown syntax: "+line)      

if __name__ == '__main__':
    HBNBCommand().cmdloop()
