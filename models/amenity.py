#!/usr/bin/python3
"""Amenity class module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity class
    Attributes:
        name (str): the name of the amenity
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place", secondary="place_amenity", viewonly=False)
