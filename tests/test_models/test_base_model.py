#!/usr/bin/python3
""" Test cases for the BaseModels class
"""
import unittest
import io
import os
import datetime
import pep8
import uuid
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBase(unittest.TestCase):
    """ Unit tests for the Base model class for the project
    """
    def setUp(self):
        """ This method is always run for every test before execution
        """
        FileStorage._FileStorage__file_path = 'testfile.json'

    def tearDown(self):
        """ Always run after execution of tests
        """
        if os.path.isfile('testfile.json'):
            os.remove('testfile.json')
        FileStorage._FileStorage__objects = {}

    def test_base_pep8_conformance(self):
        """ The BaseModel code is PEP8 conformant?
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_base_performance(self):
        """ Tests if instances are working correctly
        """
        model_1 = BaseModel()
        self.assertTrue(uuid.UUID(model_1.id))
        self.assertIsInstance(model_1.created_at, datetime.datetime)
        self.assertIsInstance(model_1.updated_at, datetime.datetime)
        model_2 = BaseModel()
        self.assertIsNot(model_1, model_2)
        self.assertNotEqual(model_1.id, model_2.id)
        self.assertNotEqual(model_1.created_at, model_2.created_at)
        self.assertNotEqual(model_1.updated_at, model_2.updated_at)
        self.assertTrue(uuid.UUID(model_2.id))
        self.assertIsInstance(model_2.created_at, datetime.datetime)
        self.assertIsInstance(model_2.updated_at, datetime.datetime)
        self.assertIsInstance(model_1, BaseModel)
        self.assertIsInstance(model_2, BaseModel)

    def test_base_created_at_is_datetime(self):
        """ BaseModel's created_at is a datetime object?
        """
        obj = BaseModel()
        self.assertTrue(type(obj.created_at) is datetime.datetime)

    def test_base_updated_at_is_datetime(self):
        """ BaseModel's updated_at is a datetime object?
        """
        obj = BaseModel()
        self.assertTrue(type(obj.updated_at) is datetime.datetime)

    def test_base_save_updates_timestamp(self):
        """ BaseModel's save() is updating the timestamp?
        """
        new_obj = BaseModel()
        date1 = new_obj.updated_at
        new_obj.save()
        date2 = new_obj.updated_at
        self.assertIsInstance(date1, datetime.datetime)
        self.assertIsInstance(date2, datetime.datetime)
        self.assertTrue(date2 > date1)

    def test_base_to_dict_returns_dict(self):
        """ BaseModel's to_dict() returns a dict?
        """
        obj = BaseModel()
        dic = obj.to_dict()
        self.assertTrue(type(dic) is dict)

    def test_base_to_dict_prints_isoformat(self):
        """ BaseModel's to_dict() are storing isoformats?
        """
        obj = BaseModel()
        iso_regex = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}$'
        dic = obj.to_dict()
        self.assertRegex(dic['created_at'], iso_regex)
        self.assertRegex(dic['updated_at'], iso_regex)

    def test_base_kwargs_used(self):
        """ Tests if instantiation is correct using kwargs
        """
        dic = {"id": 'ccb68527-5744-4e5c-ae6d-d21a09ecf50d',
               "created_at": '2000-01-01T00:00:00.000000',
               "updated_at": '2000-01-01T00:00:00.000000',
               "name": "Antioquia",
               "victims": 10}
        obj = BaseModel(**dic)
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(uuid.UUID(obj.id))
        self.assertTrue('ccb68527-5744-4e5c-ae6d-d21a09ecf50d' == obj.id)
        self.assertTrue(type(obj.created_at) is datetime.datetime)
        self.assertTrue(obj.created_at == datetime.
                        datetime(2000, 1, 1, 0, 0, 0, 0))
        self.assertTrue(type(obj.updated_at) is datetime.datetime)
        self.assertTrue(obj.updated_at == datetime.
                        datetime(2000, 1, 1, 0, 0, 0, 0))
        self.assertTrue(obj.name == "Antioquia")
        self.assertTrue(obj.victims == 10)

    def test_save_and_delete(self):
        """ Tests if method save and delete work correctly
        """
        obj1 = BaseModel()
        obj1.save()
        self.assertTrue(obj1 in FileStorage._FileStorage__objects.values())
        obj1.delete()
        self.assertTrue(obj1 not in FileStorage._FileStorage__objects.values())
