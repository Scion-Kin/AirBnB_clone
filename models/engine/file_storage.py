#!/usr/bin/python3
''' This class will be used for computing file storage '''
import json


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name] = obj
        return self.__objects

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            r_dict = {}
            r_dict.update(FileStorage.__objects)
            for key, value in r_dict.items():
                r_dict[key] = value if isinstance(value, dict)\
                    else value.to_dict()
            json.dump(r_dict, f)

    def reload(self):
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        classes = {
                    'BaseModel': BaseModel,
                    'Amenity': Amenity,
                    'City': City,
                    'Place': Place,
                    'Review': Review,
                    'State': State
                  }
        try:
            r_dict = {}
            with open(FileStorage.__file_path, 'r') as f:
                r_dict = json.load(f)
                for key, value in r_dict.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
