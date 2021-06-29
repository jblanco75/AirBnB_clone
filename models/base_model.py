#!/usr/bin/python3
"""test"""

from datetime import datetime
import uuid
import models

class BaseModel():
    """test"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                #if key == "__class__":
                 #   pass
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        #else:
         #   self.id = str(uuid.uuid4())
          #  self.created_at = self.updated_at = datetime.now()
            #models.storage.new(self)
##### DEBUG CHECKER ABOVE
#### EL bloque de abajo deberia estar en else
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """test"""
        return ("[{}] ({}) {}").format(self.__class__.__name__,
                                       self.id , self.__dict__)

    def save(self):
        """test"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """test"""
        dic = dict(self.__dict__)
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
