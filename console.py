#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
import json
import os
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):

    valid_models = ["BaseModel"]
    file_name = "file.json"
    prompt = "(hbnb) "
    storage = FileStorage()
    

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)
        """
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt
        """
        pass

    def do_create(self, args):
        args_list = args.split()


        try:
            Model_name = args_list[0]
        except IndexError:
            Model_name = None

        if Model_name is None:
            print("** class name missing **")
            return


        if Model_name not in HBNBCommand.valid_models:
            print("** class doesn't exist **")


        if len(args_list) == 1 and Model_name in HBNBCommand.valid_models:
            model = BaseModel()
            model.save()
            print(model.id)
            
    def do_show(self, args):
        
        args_list = args.split()
        
        try:
            first_args = args_list[0]
            Model_name =  first_args
        except IndexError:
            print("** class name missing ** ")
            return 
        if Model_name not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
            return
        
        try:             
            second_args = args_list[1]
            Model_id = second_args
        except IndexError:
            print("** instance id missing **")
            return
        
        if os.path.exists(HBNBCommand.file_name):
            with open(HBNBCommand.file_name) as f:
                json_dict = json.load(f)
                
        obj_key = f"{Model_name}.{Model_id}"
        new_obj = json_dict.get(obj_key, "** no instance found **")
        if not isinstance(new_obj, dict):
            print(new_obj)
        else:
            obj_1 = BaseModel(**new_obj)
            print(obj_1)
            
    def do_destroy(self, args):
        args_list = args.split()
        
        try:
            first_args = args_list[0]
            Model_name =  first_args
        except IndexError:
            print("** class name missing ** ")
            return 
        #Checks if the model passed to the cmd is a valid Model
        if Model_name not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
            return
        
        try:             
            second_args = args_list[1]
            Model_id = second_args
        except IndexError:
            print("** instance id missing **")
            return
        
        
        obj_key = f"{Model_name}.{Model_id}"
        if os.path.exists(HBNBCommand.file_name):
            with open(HBNBCommand.file_name, "r") as f:
                dict_objs = json.load(f)
                if obj_key not in dict_objs:
                    print("** no instance found **")
                    return
            
        del dict_objs[obj_key]
        file_storage = HBNBCommand.storage.all()
        del file_storage[obj_key]
        
            
        with open(HBNBCommand.file_name, "w") as f:
            json.dump(dict_objs, f, indent=4)
            
    # def do_all(self, args):
    #     args_list = args.split()
        
    #     try:
    #         Model_name = args_list[0]
    #     except IndexError:
    #         return
    #     if Model_name not in HBNBCommand.valid_models:
    #         print("** class doesn't exist **")
    #         return
    #     object_list = []
    #     with open(HBNBCommand.file_name) as f:
    #         obj_dict = HBNBCommand.storage.all()
    #     for obj_value in obj_dict.values():
    #         instance = BaseModel(**obj_value)
    #         object_list.append(instance)
        
    #         string_representations = [obj.__str__() for obj in object_list]
    #         print(string_representations)

    def do_all(self, args):
        """
        Prints string representations of all instances of the specified class or all instances if no class is specified.
        """
        args_list = args.split()
        class_name = args_list[0] if args_list else None
        if class_name is None:
            print("** class doesn't exist **")
            return
        
        if class_name not in HBNBCommand.valid_models:
            return
            
        instances = []
        for obj in HBNBCommand.storage.all().values():
            instances.append(str(obj))

        print(instances)

            
            
        
            
            
    
                
        
        
        
       
       
        
                
                
        
            
 
        
        
        
        

        
        
        
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
