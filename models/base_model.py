#!/usr/bin/python3
""" This is the base model of future classes. They will inherit from this"""
import uuid
from datetime import datetime


class BaseModel:
    ''' This is the base class for all others in this project '''

    def __init__(self, *args, **kwargs):
        ''' Initiates a new instance of the this class '''

        if not kwargs:
            # If the instance is new and not from a dictionary representation
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            kwargs['created_at'] = (datetime.strptime(kwargs['created_at'],
                                    "%Y-%m-%dT%H:%M:%S.%f") if
                                    kwargs['created_at'] else datetime.now())
            kwargs['updated_at'] = (datetime.strptime(kwargs['updated_at'],
                                    "%Y-%m-%dT%H:%M:%S.%f") if
                                    kwargs['updated_at'] else datetime.now())
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        r_dict = {}
        r_dict.update(self.__dict__)
        r_dict['__class__'] = self.__class__.__name__
        r_dict['created_at'] = self.created_at.isoformat()
        r_dict['updated_at'] = self.updated_at.isoformat()
        return r_dict
