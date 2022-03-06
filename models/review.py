#!/bin/usr/python3
"""
9. More classes!
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Revie class inherited from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
            
