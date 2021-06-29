#!/usr/bin/python3
"""classes that inherit from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Public class attributes:
    name: string - empty string"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
