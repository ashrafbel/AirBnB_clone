#!/usr/bin/python3
""" class review module for the HBNB"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review representation """
    place_id = ""
    user_id = ""
    text = ""
