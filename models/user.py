#!/usr/bin/python3
"Define the user class module"
from models.base_model import BaseModel


class User(BaseModel):
    "Define class User"
    email = ""
    password = ""
    first_name = ""
    last_name = ""
