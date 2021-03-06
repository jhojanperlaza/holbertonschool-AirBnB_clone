#!/usr/bin/python3
"""
Unittest for Amenity Class
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class Test_Amenity(unittest.TestCase):
    """Class Test for Amenity"""

    def test_uuid(self):
        """Test the uuid"""
        am1 = Amenity()
        am2 = Amenity()
        self.assertIsInstance(am1, Amenity)
        self.assertTrue(hasattr(am1, "id"))
        self.assertNotEqual(am1.id, am2.id)
        self.assertIsInstance(am1.id, str)

    def test_is_subclass(self):
        """Test if is a subclass"""
        am1 = Amenity()
        self.assertIsInstance(am1, BaseModel)

    def test_datetime(self):
        """Test the datetime attributes"""
        am1 = Amenity()
        self.assertTrue(hasattr(am1, "created_at"))
        self.assertTrue(hasattr(am1, "updated_at"))
        self.assertNotEqual(am1.created_at, am1.updated_at)

    def test_attributes(self):
        """Test the attributes"""
        am1 = Amenity()
        self.assertTrue(hasattr(am1, "name"))
        self.assertEqual(am1.name, "")
        self.assertIsInstance(am1.name, str)

    def test_add_attributes(self):
        """Test new attributes"""
        am1 = Amenity()
        am1.email = "Sebas@holberton.com"
        am1.number = 90
        self.assertTrue(hasattr(am1, "email"))
        self.assertEqual(am1.email, "Sebas@holberton.com")
        self.assertIsInstance(am1.email, str)
        self.assertTrue(hasattr(am1, "number"))
        self.assertEqual(am1.number, 90)
        self.assertIsInstance(am1.number, int)


if __name__ == '__main__':
    unittest.main()
