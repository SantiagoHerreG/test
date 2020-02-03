import unittest
""" Test cases for the FileStorage class
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.jurisdiction import Jurisdiction
import os


class TestFileStorage(unittest.TestCase):
    """ Tests for the FileStorage class
    """
    def setUp(self):
        """ This method is always run for every test before execution
        """
        FileStorage._FileStorage__objects = {}
        FileStorage._FileStorage__file_path = 'test_storage_file.json'

    def tearDown(self):
        """ Always run after execution of tests
        """
        if os.path.isfile('test_storage_file.json'):
            os.remove('test_storage_file.json')

    def test_file_storage_instances(self):
        """ Test a new instance of file storage
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_storage_attributes(self):
        """ Tests File Storage class attributes
        """
        storage = FileStorage()
        self.assertIsInstance(storage._FileStorage__objects, dict)
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_file_storage_all(self):
        """ Tests the all() method
        """
        storage = FileStorage()
        objs = storage.all()
        self.assertIsInstance(objs, dict)
        self.assertTrue(objs == {})

    def test_file_storage_new_save_delete(self):
        """ Tests the methods new(), save() and delete() for serialization
        of objects
        """
        obj = BaseModel()
        storage = FileStorage()

        storage.new(obj)
        objects = storage.all()
        self.assertTrue(obj in objects.values())

        storage.save()
        with open("test_storage_file.json", encoding="UTF-8") as f:
            read_json = f.read()
            self.assertTrue('updated_at' in read_json)

        storage.delete(obj)
        self.assertTrue(obj not in objects.values())
        with open("test_storage_file.json", encoding="UTF-8") as f:
            read_json = f.read()
            self.assertTrue("{}" == read_json)

    def test_file_storage_reload(self):
        """ Tests if the reload method is working correctly
        """
        with open("test_storage_file.json", encoding="UTF-8", mode="w") as f:
            f.write('{"BaseModel.ccb68527-5744-4e5c-ae6d-d21a09ecf50d": {"\
updated_at": "2000-01-01T00:00:00", "id": "ccb68527-5744-4e5c-\
ae6d-d21a09ecf50d", "__class__": "BaseModel", "created_at": "\
2000-01-01T00:00:00"}}')

        storage = FileStorage()
        storage.reload()
        objs = storage.all()
        self.assertTrue(type(objs["BaseModel.ccb68527-\
5744-4e5c-ae6d-d21a09ecf50d"]) is BaseModel)

    def test_get(self):
        """Tests the get() method, retrieves an object by its name
        """
        storage = FileStorage()
        storage.reload()
        jur1 = Jurisdiction(**{"name": "Cauca", "victims": 3})
        storage.save()

        jur1_clone = storage.get(Jurisdiction, "Cauca")
        self.assertTrue(jur1_clone is jur1)

    def test_reset(self):
        """ Tests if the reset method empties the database
        """
        storage = FileStorage()
        storage.reload()
        jur1 = Jurisdiction(**{"name": "Cauca", "victims": 3})
        storage.save()
        storage.reset()
        data = storage.all()
        self.assertTrue(data == {})
