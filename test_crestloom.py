# test_crestloom.py
"""
Tests for CrestLoom module.
"""

import unittest
from crestloom import CrestLoom

class TestCrestLoom(unittest.TestCase):
    """Test cases for CrestLoom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrestLoom()
        self.assertIsInstance(instance, CrestLoom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrestLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
