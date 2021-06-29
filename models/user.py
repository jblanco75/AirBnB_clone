#!/usr/bin/python3
"""class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Public class attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string"""
    def __init__(self, *args, **kwargs):
        """Attributes"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
