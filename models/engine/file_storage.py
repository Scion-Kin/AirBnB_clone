#!/usr/bin/python3
''' This class will be used for computing file storage '''
import json


class FileStorage:
    ''' Class definition for file storage handling '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' returns class info '''

        return FileStorage.__objects

    def new(self, obj):
        ''' stores the info of a new instance '''

        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name] = obj

    def save(self):
        ''' saves info of a new instance in a file '''

        with open(FileStorage.__file_path, 'w') as f:
            r_dict = {}
            r_dict.update(FileStorage.__objects)
            for key, value in r_dict.items():
                r_dict[key] = value.to_dict()
            json.dump(r_dict, f)

    def reload(self):
        ''' loads info from a json file '''

        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {
                    'BaseModel': BaseModel,
                    'Amenity': Amenity,
                    'City': City,
                    'Place': Place,
                    'Review': Review,
                    'State': State,
                    'User': User
                  }
        try:
            r_dict = {}
            with open(FileStorage.__file_path, 'r') as f:
                r_dict = json.load(f)
                for key, value in r_dict.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
