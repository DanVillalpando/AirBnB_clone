#!/usr/bin/python3
"""
3. BaseModel
"""

import uuid
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


    def __str__(self):
	return "[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__)

    def save(self):
	self.updated_at = datetime.now()

    def to_dict(self):
        dict2 = dict(**self.__dict__)
        dict2['__class__'] = str(type(self).__name__)
        dict2['created_at'] = self.created_at.isoformat()
        dict2['updated_at'] = self.updated_at.isoformat()
        return (dict2)
