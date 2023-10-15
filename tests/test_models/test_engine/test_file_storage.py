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
        self.base = BaseModel()

    def tearDown(self):
        """This method remove a path"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """This method tests the all method of FileStorage"""
        self.storage.new(self.base)
        self.storage.save()
        objects_dic = self.storage.all()
        self.assertTrue(bool(objects_dic))

    def test_new(self):
        """This method test the new method of FileStorage"""
        pass

    def test_save(self):
        """This method test the save method of FileStorage"""
        self.storage.new(self.base)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """This method test the reload method of FileStorage"""
        self.storage.new(self.base)
        self.storage.save()
        self.storage.reload()
        self.assertTrue(os.path.exists("file.json"))


if __name__ == '__main__':
    unittest.main()
