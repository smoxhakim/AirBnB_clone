#!/usr/bin/python3


from models.base_model import BaseModel
from models.__init__ import storage

class Review(BaseModel):
    place_id: str = ""
    user_id: str = ""
    text: str = ""
    