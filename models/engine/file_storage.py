#!/usr/bin/python3
"""This method contains the model for managing File Storage"""
import json
#--import os
from models.base_model import BaseModel

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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    

    def save(self):
        """This method serializes __objects to the
        JSON file (path: __file_path)"""
        SerializeObj = {}
        for key, obj in self.__objects.items():
            SerializeObj[key] = obj.to.dict()
        with open(self.__file_path, 'w', encoding= 'utf-8') as file:
            json.dump(SerializeObj, file, indent= 4)


    def reload(self):
        """This method deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                #loading the Json data from the file
                ObjDic = json.load(file)
                for key, val in ObjDic.items():
                    #Extracting classname form dict
                    ClassName = val.get("__class__")
                    if ClassName:
                        #it removes the class from the dict
                        del val["__class__"]
                        ObjClass= class_mapping.get(ClassName)
                        if ObjClass:
                            obj = ObjClass(**val)
                            #adding the new obj to storage
                            self.new(obj)
        except FileNotFoundError:
            return
