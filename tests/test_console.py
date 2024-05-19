import unittest

from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestHBNBCommand_prompt(unittest.TestCase):
    """testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class ConsoleTestCase(unittest.TestCase):
    """testing errors"""

    def check_json(self, classname, id):
        keyname = classname + "." + id
        with open(self.filepath, "r") as file:
            saved_data = json.load(file)
        self.assertIn(keyname, saved_data)
        self.assertEqual(saved_data[keyname]["id"], id)
        self.assertEqual(saved_data[keyname]["__class__"], classname)

    def test_error(self):
        """testing errors"""
        cmd_classname = ["create", "update", "show", "destroy"]
        cmd_id = ["update", "show", "destroy"]
        cmd_attr = ["update"]

        """ class name missing """
        for cmd in cmd_classname:
            # print(f"class name missing : {cmd}")
            with patch("sys.stdout", new=StringIO()) as f:
                expected = "** class name missing **"
                HBNBCommand().onecmd(cmd)
                self.assertCountEqual(expected, f.getvalue().strip())

        """ class doesn't exist """
        class_dont_exist = [
                "create x", "update x", "show x", "destroy x", "all x"]

        for cmd in class_dont_exist:
            # print(f"class doesn't exist : {cmd}")
            with patch("sys.stdout", new=StringIO()) as f:
                expected = "** class doesn't exist **"
                HBNBCommand().onecmd(cmd)
                self.assertCountEqual(expected, f.getvalue().strip())

        """ instance id missing """
        cmds = ["update", "show", "destroy"]
        all_class = HBNBCommand().classes
        for cmd in cmds:
            for clas in all_class:
                # print(f"instance id missing : {cmd} {clas}")
                with patch("sys.stdout", new=StringIO()) as f:
                    expected = "** instance id missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas}")
                    self.assertCountEqual(expected, f.getvalue().strip())

        """ no instance found """
        cmds = ["update", "show", "destroy"]
        all_class = HBNBCommand().classes
        wrong_id = "x"
        for cmd in cmds:
            for clas in all_class:
                # print(f"no instance found : {cmd} {clas} {wrong_id}")
                with patch("sys.stdout", new=StringIO()) as f:
                    expected = "** no instance found **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {wrong_id}")
                    self.assertCountEqual(expected, f.getvalue().strip())

    def test_create_object(self):
        """testing for create"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            Key = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            Key = "User.{}".format(output.getvalue().strip())
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            Key = "State.{}".format(output.getvalue().strip())
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            Key = "City.{}".format(output.getvalue().strip())
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            Key = "Place.{}".format(output.getvalue().strip())
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            Key = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(Key, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            Key = "Review.{}".format(output.getvalue().strip())
            self.assertIn(Key, storage.all().keys())

        """ value missing """
        new_BaseModel = BaseModel()
        new_User = User()
        new_State = State()
        new_City = City()
        new_Amenity = Amenity()
        new_Place = Place()
        new_Review = Review()
        id_BaseModel = new_BaseModel.id
        id_User = new_User.id
        id_State = new_State.id
        id_City = new_City.id
        id_Amenity = new_Amenity.id
        id_Place = new_Place.id
        id_Review = new_Review.id
        id_dict = {
            "BaseModel": id_BaseModel,
            "User": id_User,
            "State": id_State,
            "City": id_City,
            "Amenity": id_Amenity,
            "Place": id_Place,
            "Review": id_Review,
        }
        cmds = ["update"]
        all_class = HBNBCommand().classes
        for cmd in cmds:
            for clas in all_class:
                # print(f"no instance found : {cmd} {clas} {wrong_id}")
                # print(f"{cmd} {clas} {id_dict[clas]}")
                with patch("sys.stdout", new=StringIO()) as f:
                    expected = "** value missing **"
                    HBNBCommand().onecmd(f"{cmd} {clas} {id_dict[clas]} name")
                    self.assertCountEqual(expected, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
