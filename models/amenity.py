#!/usr/bin/python3

from models.base_model import BaseModel
from models.__init__ import storage

"""Amenity Module"""


class Amenity(BaseModel):
    """This class represents an Amenity object that inherits from BaseModel.

    Attributes:
        name (str): The name of the Amenity.
    """
    name: str = ""
