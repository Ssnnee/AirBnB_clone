#!/usr/bin/python3
"""This module is unut test for the User model"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """This class is test for the User class"""

    def test_default_attributes(self):
        """This method test the default attributes of User"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_valid_user(self):
        """This method tests User with valid assignements"""

        User.email = "user@example.com"
        User.password = "password"
        User.first_name = "Sne"
        User.last_name = "Zjaad"

        self.assertEqual(User.email, "user@example.com")
        self.assertEqual(User.password, "password")
        self.assertEqual(User.first_name, "Sne")
        self.assertEqual(User.last_name, "Zjaad")


if __name__ == "__main__":
    unittest.main()
