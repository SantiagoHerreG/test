#!/usr/bin/python3
""" Module that contains the class Jurisdiction, that
inherits from basemodel
"""
from models.base_model import BaseModel
import models


class Jurisdiction(BaseModel):
    """ New class Jurisdiction that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """Creates the new Jurisdiction objects"""
        self.victims = 0
        super().__init__(*args, **kwargs)

    def update(self, victims):
        """Updates the number of victims of a Jurisdiction"""
        self.victims = victims
        self.save()

    @classmethod
    def total(cls):
        """ Returns the total of victims in all Jurisdictions"""
        total = 0
        all_jurisd = models.storage.all(Jurisdiction)
        for jurisdiction in all_jurisd.values():
            total += jurisdiction.victims
        return total
