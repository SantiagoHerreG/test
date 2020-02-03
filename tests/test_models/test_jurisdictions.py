#!/usr/bin/python3
""" Module for unit testing of Jurisdiction class
"""
import unittest
from models.jurisdiction import Jurisdiction


class Test_jurisdiction(unittest.TestCase):
    """Tests class for jurisdictions
    """
    def test_jurisdictions_instances(self):
        """Tests if Jurisdiction instances are working
        """
        obj = Jurisdiction()
        self.assertIsInstance(obj, Jurisdiction)

    def test_jurisdiction_attributes(self):
        """Tests if jurisdiction instances are working
        """
        obj = Jurisdiction(**{'name': 'Antioquia', 'victims': 1})
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.victims, int)
