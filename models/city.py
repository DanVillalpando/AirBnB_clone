#!/bin/usr/python3
"""
9. More classes!
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inherited from BaseModel
    """

    state_id = ""
    name = ""
