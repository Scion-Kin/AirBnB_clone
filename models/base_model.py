#!/usr/bin/python3
""" This is the base model of future classes. They will inherit from this"""
import uuid
import datetime
from engine.file_storage import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id", str(uuid.uuid4()))
        created_at_value = kwargs.get("created_at")
        self.created_at = (datetime.datetime.strptime(created_at_value,
                           "%Y-%m-%dT%H:%M:%S.%f") if created_at_value
                           else datetime.datetime.now().isoformat())
        updated_at_value = kwargs.get("updated_at")
        self.updated_at = (datetime.datetime.strptime(updated_at_value,
                           "%Y-%m-%dT%H:%M:%S.%f") if updated_at_value
                           else datetime.datetime.now().isoformat())
        if self.__name__ not in self.__dict__: # if the instance is new and not from a dictionary representation
            storage.new(self)

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()
        storage.save()

    def to_dict(self):
        vars(self)['__class__'] = self.__class__.__name__
        return vars(self)
