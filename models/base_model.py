#!/usr/bin/python3

import uuid
import datetime
from models.__init__ import storage

"""Base class"""


class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
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
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """returns a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the object"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns object dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return obj_dict