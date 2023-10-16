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

        class_name = obj.__class__.__name__
        class_id = obj.id
        self.__objects[f"{class_name}.{class_id}"] = obj

    def save(self):
        """ This method serializes __objects to the
        JSON file (path: __file_path)
        """
        try:
            serialized_object = {
                    k: v.to_dict() for k, v in self.__objects.items()
            }
            with open(self.__file_path, mode='w', encoding="utf-8") as file:
                file.write(json.dumps(serialized_object))
        except Exception:
            pass

    def reload(self):
        """This method deserializes the JSON file to __objects """

        # This import avoid circular import
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.state import State

        CLASSES = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'Place': Place,
            'Amenity': Amenity,
            'State': State
            }

        if not os.path.exists(self.__file_path):
           pass 

        try:
            with open(self.__file_path, 'r') as file:
                objects = json.load(file)
                for k, serialized_object in objects.items():
                    class_name = serialized_object['__class__']
                    clas = CLASSES[class_name]
                    self.__objects[k] = clas(**serialized_object)
        except json.JSONDecodeError:
            pass
