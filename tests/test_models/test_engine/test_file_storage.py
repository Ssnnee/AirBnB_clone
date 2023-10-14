#!/usr/bin/python3
"""This module contains test for the serialization"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """This is test for the FileStorage class"""

    def setUp(self):
        """This method set up the test"""
        self.storage = FileStorage()
        self.obj = BaseModel()

    def tearDown(self):
        """This method remove a path"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """This method tests the all method of FileStorage"""
        objects = self.storage.all()
        self.assertIn(
                f"{self.model.__class__.__name__}.{self.model.id}", objects)

    def test_new(self):
        """This method test the new method of FileStorage"""
        self.storage.new(self.obj)
        self.assertEqual(
                self.storage.all(),
                {f"{self.obj.__class__.__name__}.{self.obj.id}": self.obj})

    def test_save(self):
        """This method test the save method of FileStorage"""
        self.storage.new(self.obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """This method test the reload method of FileStorage"""
        self.storage.new(self.obj)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(
                self.storage.all(),
                {f"{self.obj.__class__.__name__}.{self.obj.id}": self.obj})


if __name__ == '__main__':
    unittest.main()
