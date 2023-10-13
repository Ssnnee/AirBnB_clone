#!/usr/bin/python3
""" This module contains the mean model of all classes in this project"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """ This class is the model of all class"""

    def __init__(self, *arg, **kwargs):
        """This method initializes a new BaseModel instance."""
        dateFormat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for k, value in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(value, date_format))
                else:
                # the k !== "created_at" or k !=="updated_at" case
                    setattr(self, k, value)
        else:
            models.storage.new(self)

    def save(self):
        """This method updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        model.storage.save()

    def to_dict(self):
        """This method returns a dictionary containing
        all keys/values  of __dict__ of  the instance"""
        className = self.__class__.__name__
        dict_to_return = self.__dict__.copy()
        dict_to_return['__class__'] = className
        dict_to_return['updated_at'] = self.updated_at.isoformat()
        dict_to_return['created_at'] = self.created_at.isoformat()

        return (dict_to_return)

    def __str__(self):
        """This is the Tostring method"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        )
