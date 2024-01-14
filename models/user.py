#!/usr/bin/python3
""" Defines a class for a user """
from models.base_model import BaseModel


class User(BaseModel):
    ''' class definition for user '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
