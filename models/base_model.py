#!/usr/bin/python3
""" Contains the base model for the objects """
import datetime
import uuid
import models

class BaseModel:
    """ Model for the objects created
    """
    def __init__(self, *args, **kwargs):
        """Constructor: each object has an id and creation and updation dates"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            for key, value in kwargs.items():
                if key not in ["id", "created_at", "updated_at", "__class__"]:
                    setattr(self, key, value)

            if "id" in kwargs.keys():
                try:
                    uuid.UUID(kwargs["id"])
                    self.id = kwargs["id"]
                except:
                    self.id = str(uuid.uuid4())
            else:
                self.id = str(uuid.uuid4())

            if ("created_at" in kwargs.keys()):
                try:
                    self.created_at = datetime.\
                                      datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                except:
                    self.created_at = datetime.datetime.now()
            else:
                self.created_at = datetime.datetime.now()

            if ("updated_at" in kwargs.keys()):
                try:
                    self.updated_at = datetime.\
                                      datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                except:
                    self.updated_at = datetime.datetime.now()
            else:
                self.updated_at = datetime.datetime.now()

            models.storage.new(self)

    def __str__(self):
        """String representation of objects"""

        return "[" + type(self).__name__\
               + "] " + "(" + self.id + ") " + str(self.__dict__)

    def to_dict(self):
        """ This returns a dictionary representation of the objects for
        having JSON compatibility"""

        new_dict = self.__dict__.copy()
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['__class__'] = type(self).__name__
        return new_dict

    def save(self):
        """ Updates the public instance attribute Updated at
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def delete(self):
        """delete the current instance from the storage (models.storage)
        by calling the method delete
        """
        models.storage.delete(self)
