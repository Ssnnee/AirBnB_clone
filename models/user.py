#!/usr/bin/python3
"""This is the user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """ This class is the User model"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
