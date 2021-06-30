#!/usr/bin/python3
"""place_id: string - empty string: it will be the Place.id"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Public class creation"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Commom definition for all models """
        super().__init__(*args, **kwargs)
