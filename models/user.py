#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): There email of the user.
        password (str): There password of the user.
        first_name (str): There first name of the user.
        last_name (str): There last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
