#!/usr/bin/python3
"""User Module"""


from models.base_model import BaseModel


class User(BaseModel):
    """This module defines the User class which inherits from BaseModel.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
