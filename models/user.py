#!/usr/bin/python3
from models.base_model import BaseModel
from models.__init__ import storage

class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    

