#!/usr/bin/python3
""" define Class user """

from models.base_model import BaseModel


class User(BaseModel):
    """ this is class User """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
