#!/usr/bin/python3
"""This module is tests for th Amenity class"""
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """This class test the Amenity class"""

    def test_default_attributes(self):
        """This method test de default attributes of Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
