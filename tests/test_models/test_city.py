#!/usr/bin/python3
"""
Unittest for City Class
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class Test_City(unittest.TestCase):
    """Class Test for City"""

    def test_uuid(self):
        """Test the uuid"""
        c1 = City()
        c2 = City()
        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "id"))
        self.assertNotEqual(c1.id, c2.id)
        self.assertIsInstance(c1.id, str)

    def test_is_subclass(self):
        """Test if is a subclass"""
        c1 = City()
        self.assertIsInstance(c1, BaseModel)

    def test_datetime(self):
        """Test the datetime attributes"""
        c1 = City()
        self.assertTrue(hasattr(c1, "created_at"))
        self.assertTrue(hasattr(c1, "updated_at"))
        self.assertNotEqual(c1.created_at, c1.updated_at)

    def test_attributes(self):
        """Test the attributes"""
        c1 = City()
        self.assertTrue(hasattr(c1, "name"))
        self.assertEqual(c1.name, "")
        self.assertIsInstance(c1.name, str)
        self.assertTrue(hasattr(c1, "state_id"))
        self.assertEqual(c1.state_id, "")
        self.assertIsInstance(c1.state_id, str)

    def test_add_attributes(self):
        """Test new attributes"""
        c1 = City()
        c1.email = "Sebas@holberton.com"
        c1.number = 90
        self.assertTrue(hasattr(c1, "email"))
        self.assertEqual(c1.email, "Sebas@holberton.com")
        self.assertIsInstance(c1.email, str)
        self.assertTrue(hasattr(c1, "number"))
        self.assertEqual(c1.number, 90)
        self.assertIsInstance(c1.number, int)


if __name__ == '__main__':
    unittest.main()
