#!/usr/bin/python3
''' Defines a review class '''
from base_model import BaseModel


class Review(BaseModel):
    ''' class definition of reviews '''
    place_id = ''
    user_id = ''
    text = ''