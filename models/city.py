#!/usr/bin/python3
"""class that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Public class attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
