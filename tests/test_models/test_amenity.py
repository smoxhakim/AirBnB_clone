#!/usr/bin/python3
""" unit test for bases """
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pep8
import models
from io import StringIO
import sys
from unittest.mock import patch
captured_output = StringIO()
sys.stdout = captured_output


class UserTest(unittest.TestCase):
    """ class for base test """

    def test_pep8_compliance(self):
        """
        pycodestyle testing
        """
        pycodestyle = pep8.StyleGuide(quiet=True)
        result = pycodestyle.check_files(["models/amenity.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)


if __name__ == '__main__':
    unittest.main()
