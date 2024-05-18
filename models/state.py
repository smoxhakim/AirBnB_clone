#!/usr/bin/python3

from models.base_model import BaseModel

"""State Module"""


class State(BaseModel):
    """This class represents a State object.

    Fields:
        name (str): The name of the state.
    """
    name: str = ""
