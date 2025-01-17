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
"""
Module for the BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all models in the HBNB clone"""
    
    def __init__(self):
        """Initialize a new BaseModel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Update the updated_at timestamp"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Convert instance to dictionary"""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """Return string representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, 
            self.id, 
            self.__dict__
        )
