#!/usr/bin/python3

from models.base_model import BaseModel


"""City Module"""


class City(BaseModel):
    """This class represents a City object that inherits from BaseModel.

    Attributes:
        state_id (str): The State ID of the city.
        name (str): The name of the city.
    """
    state_id: str = ""
    name: str = ""
