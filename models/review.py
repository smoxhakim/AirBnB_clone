#!/usr/bin/python3

from models.base_model import BaseModel

"""Review Model"""


class Review(BaseModel):
    """This class represents a Review object that inherits from BaseModel.

    Attributes:
        place_id (str): The Place ID of the review.
        user_id (str): The User ID of the review.
        text (str): The text content of the review.
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
