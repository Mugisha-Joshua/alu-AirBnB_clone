#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import os
import time


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test cases"""
        self.model = BaseModel()

    def test_init(self):
        """Test initialization"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test string representation"""
        string = str(self.model)
        self.assertIsInstance(string, str)
        self.assertIn("[BaseModel]", string)
        self.assertIn(self.model.id, string)

    def test_save(self):
        """Test save method"""
        old_updated_at = self.model.updated_at
        time.sleep(0.1)  # Ensure time difference
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        
        # Check if it's a dictionary
        self.assertIsInstance(model_dict, dict)
        
        # Check required keys
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        
        # Check values
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], 
                        self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], 
                        self.model.updated_at.isoformat())

    def test_unique_ids(self):
        """Test that each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_datetime_attributes(self):
        """Test that datetime attributes are created"""
        self.assertNotEqual(self.model.created_at, self.model.updated_at)
        self.assertLessEqual(self.model.created_at, self.model.updated_at)

    def test_custom_attributes(self):
        """Test adding custom attributes"""
        self.model.name = "Test Model"
        self.model.number = 89
        model_dict = self.model.to_dict()
        self.assertIn('name', model_dict)
        self.assertIn('number', model_dict)
        self.assertEqual(model_dict['name'], "Test Model")
        self.assertEqual(model_dict['number'], 89)

    def test_datetime_conversion(self):
        """Test datetime conversion in to_dict"""
        model_dict = self.model.to_dict()
        created_at = model_dict['created_at']
        updated_at = model_dict['updated_at']
        
        # Check if they're strings
        self.assertIsInstance(created_at, str)
        self.assertIsInstance(updated_at, str)
        
        # Check format
        try:
            datetime.fromisoformat(created_at)
            datetime.fromisoformat(updated_at)
        except ValueError:
            self.fail("Datetime strings are not in ISO format")


if __name__ == '__main__':
    unittest.main()
