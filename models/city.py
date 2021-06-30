#!/usr/bin/python3
"""class that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Commom definition for models"""
        super().__init__(*args, **kwargs)
