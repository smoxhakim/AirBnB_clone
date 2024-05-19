#!/usr/bin/python3
"""
basemodel unittest
"""
import unittest
import subprocess
import pep8
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from io import StringIO
import sys
from unittest.mock import patch
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTest(unittest.TestCase):
    """
    Base Test class
    """
    def test_pep8_compliance(self):
        """
        pycodestyle testing
        """
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/base_model.py",
                                          "models/__init__.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)

    def test_all(self):
        """
        test all even if there is no
        point of testing it
        """
        for key in storage.all():
            self.assertTrue(eval(key.split(".\
")[0]) == storage.all()[key].__class__)

    def test_instance(self):
        """Testing a new created instance"""
        obj = BaseModel()
        self.assertEqual(BaseModel, type(obj))

    def test_instance_id(self):
        obj = BaseModel()
        self.assertEqual(str, type(obj.id))

    def test_obj_id(self):
        obj = BaseModel()
        self.assertEqual(datetime, type(obj.created_at))

    def test_unique_id(self):
        """
        test if two obj has two different ids
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_obj_str(self):
        """
        test obj sring reprisotation
        """
        obj = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(expected_str, obj.__str__())

    def test_obj_created_at(self):
        """
        test obj sring reprisotation
        """
        obj = BaseModel()
        self.assertEqual(datetime, type(obj.created_at))

    def test_time(self):
        """
        test obj time update
        """
        obj = BaseModel()

        self.assertEqual(str(obj),  f"[BaseModel] ({obj.id}) {obj.__dict__}")
        old_time = obj.updated_at
        obj.save()
        new_time = obj.updated_at
        self.assertLess(old_time, new_time)


if __name__ == '__main__':
    unittest.main()
