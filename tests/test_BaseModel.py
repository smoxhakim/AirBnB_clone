#!/usr/bin/python3
import unittest
import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        # Test creating a new instance with no arguments
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.created_at, datetime.datetime)
        self.assertIsNotNone(self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

        # Test creating a new instance with kwargs
        kwargs = {
            'id': 'test_id',
            'created_at': '2023-05-18T12:00:00.000000',
            'updated_at': '2023-05-18T12:00:00.000000'
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime.datetime(2023, 5, 18, 12, 0, 0))
        self.assertEqual(model.updated_at, datetime.datetime(2023, 5, 18, 12, 0, 0))

    def test_str(self):
        # Test the __str__ method
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        # Test the save method
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        # Test the to_dict method
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))

if __name__ == '__main__':
    unittest.main()
