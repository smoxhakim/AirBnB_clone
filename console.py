#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
import json
import os

class HBNBCommand(cmd.Cmd):

    valid_models = ["BaseModel"]
    file_name = "file.json"
    prompt = "(hbnb) "
    
    

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

        #Attempt to assign first argument to Model_name
        #if no argument were passed, meaning args_list atkun khawya
        #when we assign Model_name to index 0 the try will throw an IndexError
        #and we assign Model_name to None
        try:
            Model_name = args_list[0]
        except IndexError:
            Model_name = None

        if Model_name is None:
            print("** class name missing **")
            return

        #had l if kat checki wach l value d Model_name makaynch f valid_models list
        #katfut 3la l values kamlin li kaynin f valid_models o kat compari kol value b Model_name
        #ila mal9atuch tma katprint "class dosen't exist"
        #khdmtha haka cause fl future aykon 3ndna bzaf dl models
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
        
                
                
        
            
 
        
        
        
        

        
        
        
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
