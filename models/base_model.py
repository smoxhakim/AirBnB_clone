#!/usr/bin/python3

import uuid
import datetime
from models import storage

"""Base Model"""


class BaseModel:
    """This class represents a Base Model object that serves as the base for other model classes.

    Attributes:
        id (str): The unique identifier for the object.
        created_at (datetime): The datetime when the object was created.
        updated_at (datetime): The datetime when the object was last updated.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel object.

        If kwargs is not empty, sets the attributes of the object based on the key-value pairs in kwargs.
        If kwargs is empty, initializes the id, created_at, and updated_at attributes.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key,value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    date_object = datetime.datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date_object)
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)


    def __str__(self):
        """Returns a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Saves the object"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return obj_dict

