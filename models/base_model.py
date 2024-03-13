#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
"""
    Represents a sample class with attributes
    for identification and timestamps.

    Attributes:
        id (uuid.UUID): Unique identifier generated using uuid.uuid4().
        created_at (datetime.datetime):
            Date and time when the instance is created.
        updated_at (datetime.datetime):
            Date and time of the last update of the instance.
"""

class BaseModel:
    def __init__(self):
        """
        Initializes a new instance of the class.
        This function assigns initial values to the instance attributes
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns the form in which the information should be printed
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save the date current
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """Convert the instance to a dictionary.

        Returns:
        dict: A dictionary containing all attributes of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
