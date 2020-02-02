#!/usr/bin/python3
"""Module that contains class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.jurisdiction import Jurisdiction
import os


class FileStorage:
    """ Serializes and deserializes instances to JSON format
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        new_dict = {}
        if cls:
            for key, value in self.__objects.items():
                if type(value) == cls:
                    new_dict[key] = value
            return new_dict

        return self.__objects

    def new(self, obj):
        """ Sets in __object dictionary an instance <obj classname>.id
        """
        FileStorage.__objects[str(type(obj).__name__) + "." + str
                              (obj.id)] = obj

    def save(self):
        """ Serializes __objects to the file
        """
        serialized = {}

        for keys, objs in FileStorage.__objects.items():
            dict_obj = objs.to_dict()
            serialized[keys] = dict_obj

        json_dictionary = json.dumps(serialized)

        with open(FileStorage.__file_path, encoding="UTF", mode="w") as f:
            f.write(json_dictionary)

    def reload(self):
        """ deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as f:
                objs_dict_read = f.read()
                new_dict_reloaded = json.loads(objs_dict_read)
        except:
            return
        for keys, objs_dict in new_dict_reloaded.items():
            class_name = objs_dict["__class__"]
            obj = eval(class_name)(**objs_dict)
            FileStorage.__objects[keys] = obj

    def delete(self, obj=None):
        """To delete obj from __objects if its inside
        """
        if obj:
            try:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                del self.__objects[key]
                self.save()
            except:
                pass

    def get(self, cls, name):
        """A method to retrieve one object by its name
        """
        obj_dict = self.all(cls)
        for obj in obj_dict.values():
            if obj.name == name:
                return obj
        return None

    def reset(self):
        """ Resets the database, SECURITY RISK ALLOWED """
        os.remove(FileStorage.__file_path)
        FileStorage.__objects = {}
        self.save()
        self.reload()
