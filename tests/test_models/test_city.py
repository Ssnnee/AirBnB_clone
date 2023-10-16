#!/usr/bin/python3
"""This modules contais tests for the City class"""
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """This class is unit test for the City class"""

    def test_default_attributes(self):
        """This method test the default attribute"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
