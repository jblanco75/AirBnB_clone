#!/usr/bin/python3
"""Amenity test"""

import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test amenity"""

    def setUp(self):
        """Creates an instance before each test"""
        self.test = Amenity()

    def off(self):
        """Delete isntance after test"""
        del self.test

    def test_idt(self):
        """check ID type"""
        self.assertEqual(type(self.test.id), str)

if __name__ == "__main__":
    unittest.main()
