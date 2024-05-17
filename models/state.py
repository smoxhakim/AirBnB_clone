#!/usr/bin/python3

from models.base_model import BaseModel
from models.__init__ import storage


class State(BaseModel):
    name: str = ""
    
