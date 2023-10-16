#!/usr/bin/python3
"""Test"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """This tests the Review class"""
    def test_default_attributes(self):
        """Tests default attributes for Review"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
