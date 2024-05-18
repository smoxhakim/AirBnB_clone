#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    def test_id(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertTrue(hasattr(model1, 'id'))
        self.assertTrue(hasattr(model2, 'id'))
        self.assertNotEqual(model1.id, model2.id)
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model2.id, str)