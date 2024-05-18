#!/usr/bin/python3

from models.base_model import BaseModel

"""Amenity Module"""


class Place(BaseModel):
    """This class represents a Place object that inherits from BaseModel.

    Attributes:
        city_id (str): The City ID of the place.
        user_id (str): The User ID of the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can
        accommodate.
        price_by_night (int): The price per night of the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of Amenity IDs associated with the place.
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
