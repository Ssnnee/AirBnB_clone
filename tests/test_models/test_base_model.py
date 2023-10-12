#!/usr/bin/python3
"""This module is the unittest of the BaseModel class"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseMadel(unittest.TestCase):
    """This class test the BaseModel"""

    def test_attributes(self):
        """This method test if attributes are initialized correctly"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """This method test if the __init__ method
        initializes correctly with kwargs"""
        datas = {
                "id": "1sne3",
                "created_at": "2023-10-12T20:00:00",
                "updated_at": "2023-10-12T20:02:00",
                "random_attri": "random_value",
                "__class__": "notvalid"
        }

        model = BaseModel(**datas)
        self.assertEqual(model.id, "1sne3")
        self.assertEqual(model.created_at.isoformat(), "2023-10-12T20:00:00")
        self.assertEqual(model.updated_at.isoformat(), "2023-10-12T20:02:00")
        self.assertEqual(model.random_attri, "random_value")
        self.assertNotEqual(model.__class__.__name__, "notvalid")

    def test_save_method(self):
        """This method test if the save
        method updates the 'updated_at' attribute"""
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """This method test if the to_dict method returns
        the expected dictionary"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str_method(self):
        """This method test if the __str__
        method returns the expected string"""
        model = BaseModel()
        expected_string = "[BaseModel] ({}) {}".format(
                model.id, model.__dict__
        )
        self.assertEqual(str(model), expected_string)


if __name__ == '__main__':
    unittest.main()
