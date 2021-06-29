#!/usr/bin/python3
"""class that inherit from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attributes:
    place_id: string - empty string
    user_id: string - empty string
    text: string - empty string"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
