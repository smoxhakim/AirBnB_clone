#!/usr/bin/python3
""" unit test for bases """
import json
import unittest
import pep8
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage
from io import StringIO
from os import remove
from os import path
import sys
from unittest.mock import patch
captured_output = StringIO()
sys.stdout = captured_output


class FileStorageTest(unittest.TestCase):
    """ class for save test """

    def test_pep8_compliance(self):
        """
        pycodestyle testing
        """
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/engine/file_storage.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)

    def testJSON(self):
        """
        Json file testing
        """
        file = storage._FileStorage__file_path
        self.assertEqual(file, "file.json")
        if path.exists(file):
            remove(file)
        self.assertFalse(path.exists(file))
        storage.reload()

    def testCreatInstanceNoKwarg(self):
        """
        Create object testing
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def testCreatInstanceKwarg(self):
        """
        Create object testing
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def testIsPrivate(self):
        """
        test private attribute type
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def testAttExist(self):
        """
        attributes existing testing
        """
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))

    def test_all(self):
        """
        all method testing
        """
        for key in storage.all():
            self.assertTrue(eval(key.split(".\
")[0]) == storage.all()[key].__class__)
        self.assertEqual(dict, type(storage.all()))
        with self.assertRaises(TypeError):
            storage.all(None)
        self.assertNotEqual(storage.all(), {})

    def test_id(self):
        """
        id testing
        """
        for key in storage.all():
            self.assertTrue(key.split(".\
")[1] == storage.all()[key].to_dict()["id"])

    def test_new(self):
        """
        new method testing
        """
        b = BaseModel()
        storage.new(b)
        u = User()
        storage.new(u)
        s = State()
        storage.new(s)
        p = Place()
        storage.new(p)
        c = City()
        storage.new(c)
        a = Amenity()
        storage.new(a)
        r = Review()
        storage.new(r)
        objs = storage.all()
        self.assertIn("BaseModel." + b.id, objs)
        self.assertIn("User." + u.id, objs)
        self.assertIn("State." + s.id, objs)
        self.assertIn("Place." + p.id, objs)
        self.assertIn("City." + c.id, objs)
        self.assertIn("Amenity." + a.id, objs)
        self.assertIn("Review." + r.id, objs)
        self.assertIn(b, objs.values())
        self.assertIn(u, objs.values())
        self.assertIn(s, objs.values())
        self.assertIn(p, objs.values())
        self.assertIn(c, objs.values())
        self.assertIn(a, objs.values())
        self.assertIn(r, objs.values())

    def test_save(self):
        """
        save method testing
        """
        b = BaseModel()
        storage.new(b)
        u = User()
        storage.new(u)
        s = State()
        storage.new(s)
        p = Place()
        storage.new(p)
        c = City()
        storage.new(c)
        a = Amenity()
        storage.new(a)
        r = Review()
        storage.new(r)
        storage.save()
        text = ""
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("BaseModel." + b.id, text)
            self.assertIn("User." + u.id, text)
            self.assertIn("State." + s.id, text)
            self.assertIn("Place." + p.id, text)
            self.assertIn("City." + c.id, text)
            self.assertIn("Amenity." + a.id, text)
            self.assertIn("Review." + r.id, text)

    def test_reload(self):
        """
        load method testing
        """
        b = BaseModel()
        storage.new(b)
        u = User()
        storage.new(u)
        s = State()
        storage.new(s)
        p = Place()
        storage.new(p)
        c = City()
        storage.new(c)
        a = Amenity()
        storage.new(a)
        r = Review()
        storage.new(r)
        storage.save()
        storage.reload()
        objs = storage.all()
        self.assertIn("BaseModel." + b.id, objs)
        self.assertIn("User." + u.id, objs)
        self.assertIn("State." + s.id, objs)
        self.assertIn("Place." + p.id, objs)
        self.assertIn("City." + c.id, objs)
        self.assertIn("Amenity." + a.id, objs)
        self.assertIn("Review." + r.id, objs)


if __name__ == '__main__':
    unittest.main()
