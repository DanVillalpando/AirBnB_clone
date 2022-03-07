#!/usr/bin/python3
"""
3. BaseModel
"""

import uuid
import models
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes/methods for other classes:
    """
    def __init__(self, *args, **kwargs):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, format)
                if k != "__class__":
                    setattr(self, key, val)
        else:
            models.storage.new(self)

    def __str__(self):
        """
	Should print: [<class name>] (<self.id>) <self.__dict__>
	"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
	updates the public instance attribute updated_at
	with the current datetime
	"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
	Returns a dictionary containing all keys/values
	of __dict__ of the instance
	"""
        dict2 = dict(**self.__dict__)
        dict2['__class__'] = str(type(self).__name__)
        dict2['created_at'] = self.created_at.isoformat()
        dict2['updated_at'] = self.updated_at.isoformat()
        return (dict2)
