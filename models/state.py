#!/usr/bin/python3

from models.base_model import BaseModel
from models.__init__ import storage

"""State Module"""


class State(BaseModel):
    """This class represents a State object.

    Fields:
        name (str): The name of the state.
    """
    name: str = ""
