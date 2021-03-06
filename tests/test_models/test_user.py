#!/usr/bin/python3
"""
Unittest for User Class
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class Test_User(unittest.TestCase):
    """Class Test for User"""

    def test_uuid(self):
        """Test the uuid"""
        user1 = User()
        user2 = User()
        self.assertIsInstance(user1, User)
        self.assertTrue(hasattr(user1, "id"))
        self.assertNotEqual(user1.id, user2.id)
        self.assertIsInstance(user1.id, str)

    def test_is_subclass(self):
        """Test if is a subclass"""
        user1 = User()
        self.assertIsInstance(user1, BaseModel)

    def test_datetime(self):
        """Test the datetime attributes"""
        user1 = User()
        self.assertTrue(hasattr(user1, "created_at"))
        self.assertTrue(hasattr(user1, "updated_at"))
        self.assertNotEqual(user1.created_at, user1.updated_at)

    def test_attributes(self):
        """Test the attributes"""
        user1 = User()
        self.assertTrue(hasattr(user1, "email"))
        self.assertEqual(user1.email, "")
        self.assertIsInstance(user1.email, str)
        self.assertTrue(hasattr(user1, "password"))
        self.assertEqual(user1.password, "")
        self.assertIsInstance(user1.password, str)
        self.assertTrue(hasattr(user1, "first_name"))
        self.assertEqual(user1.first_name, "")
        self.assertIsInstance(user1.first_name, str)
        self.assertTrue(hasattr(user1, "last_name"))
        self.assertEqual(user1.last_name, "")
        self.assertIsInstance(user1.last_name, str)

    def test_add_attributes(self):
        """Test new attributes"""
        user1 = User()
        user1.number = 90
        self.assertTrue(hasattr(user1, "number"))
        self.assertEqual(user1.number, 90)
        self.assertIsInstance(user1.number, int)


if __name__ == '__main__':
    unittest.main()
