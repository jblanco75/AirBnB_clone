#!/usr/bin/python3
"""class BaseModel that defines all common
attributes/methods for other classes"""

from datetime import datetime
import uuid
import models


class BaseModel():
    """Public instance attributes:
    id: string - assign with an uuid when an instance
    is created:
    you can use uuid.uuid4() to generate unique id but
    don’t forget to convert to a string
    the goal is to have unique id for each BaseModel
    created_at: datetime - assign with the current datetime
    when an instance is created
    updated_at: datetime - assign with the current datetime
    when an instance is created and it will be updated every
    time you change your object"""
    def __init__(self, *args, **kwargs):
        """Constructor"""
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
        """print method"""
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
