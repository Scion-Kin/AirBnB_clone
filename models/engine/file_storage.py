#!/usr/bin/python3
""" This class will be used for computing file storage """
import json


class FileStorage:
    __file_path = ''
    __objects = {}
    def __init__(self):
        pass

    def all(self):
        return self.__class.__objects

    def new(self, obj):
        self.__class__.__objects.append(obj)

    def save(self):
        with open(self.__class__.__file_path, mode="w") as f:
            json.dumps(f, self.__class__.__objects)

    def reload(self):
        if self.__class__.__file_path is not None:
            with open(self.__class__.__file_path, mode="r") as f:
                json.loads(f, self.__class__.__objects)
