#!/usr/bin/python3
"""
Defines amenities class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents  amenities that user can choose from to offer at its place"""
    name = ""
