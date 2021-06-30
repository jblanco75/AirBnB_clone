#!/usr/bin/python3
"""class BaseModel that defines all common
attributes/methods for other classes"""

from datetime import datetime
import uuid
import models


class BaseModel():
    """Commom definition for all models (attributes/methods)"""
    def __init__(self, *args, **kwargs):
        """Initialization method which defines attributtes"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key not in ["__class__"]:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String respresentation of the BaseModel class"""
        return ("[{}] ({}) {}").format(self.__class__.__name__,
                                       self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        dic = dict(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
