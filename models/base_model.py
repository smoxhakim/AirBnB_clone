#!/usr/bin/python3

import uuid
import datetime

"""Base class"""


class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
        if kwargs is not None:
            for key,value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "update_at":
                    date_object = datetime.datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date_object)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """returns a string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """saves the object"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns object dictionary"""
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
