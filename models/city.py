#!/usr/bin/python3

from models.base_model import BaseModel
from models.__init__ import storage

class City(BaseModel):
    state_id: str = ""
    name: str = ""