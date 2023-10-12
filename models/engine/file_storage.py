#!/usr/bin/python3
"""This method contains the model for managing File Storage"""
import json
import os


class FileStorage:
    """This class serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """This method sets in __objects the obj with key <obj
        class name>.id"""


    def save(self):
        """This method serializes __objects to the
        JSON file (path: __file_path)"""


    def reload(self):
        """This method deserializes the JSON file to __objects"""

