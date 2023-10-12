#!/usr/bin/python3
""" This module contains the mean model of all classes in this project"""
import uuid
from datetime import datetime


class BaseModel:
    """ This class is the model of all class"""

    def __init__(self, *arg, **kwargs):
        """This method initializes a new BaseModel instance."""
        if kwargs:
            for k, value in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    value = datetime.fromisoformat(value)
                if k != "__class__":
                    setattr(self, k, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """This method updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """This method returns a dictionary containing
        all keys/values  of __dict__ of  the instance"""
        dict_to_return = self.__dict__.copy()
        dict_to_return['__class__'] = self.__class__.__name__
        dict_to_return['updated_at'] = self.updated_at.isoformat()
        dict_to_return['created_at'] = self.created_at.isoformat()

        return dict_to_return

    def __str__(self):
        """This is the Tostring method"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )

