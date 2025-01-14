# Create a basemodel class with the following attributes:
#1. ud
#2. created_at
#3. updated_at
#4. __str__: should print [<class name>] (<self.id>) <self.__dict__>
# save(self): updates the public instance attribute updated_at with the current datetime
# to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance:
# created_at and updated_at must be converted to string object in ISO format:
# format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
# you can use isoformat() of datetime object


#!/usr/bin/python3
"""Module for BaseModel class."""
from datetime import datetime
import uuid
import model:
    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

