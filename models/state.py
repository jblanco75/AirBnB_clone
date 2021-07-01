#!/usr/bin/python3
"""class that inherit from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Public class attributes: name: string - empty string"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Commom definition for models"""
        super().__init__(*args, **kwargs)
