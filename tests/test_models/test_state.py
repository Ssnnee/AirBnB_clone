#!/usr/bin/python3
"""This is test module fot the State class"""
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """This class is the unit test for State class"""
    
    def test_default_attributes(self):
        """This method test the default attributes"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
