#!/usr/bin/python3
""" Module that contains the class Jurisdiction, that
inherits from basemodel
"""
from models.base_model import BaseModel


class Jurisdiction(BaseModel):
    """ New class Jurisdiction that inherits from BaseModel
    """
    __victims = 0

    def __init__(self, *args, **kwargs):
        """Creates the new Jurisdiction objects"""
        try:
            Jurisdiction.__victims += kwargs["victims"]
        except:
            self.victims = 0
        super().__init__(*args, **kwargs)

    def update(self, victims):
        """Updates the number of victims of a Jurisdiction"""
        Jurisdiction.__victims -= self.victims
        self.victims = victims
        Jurisdiction.__victims += victims
        self.save()

    @classmethod
    def total(cls):
        """ Returns the total of victims in all Jurisdictions"""
        return cls.__victims
