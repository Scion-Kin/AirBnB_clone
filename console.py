#!/usr/bin/python3
''' A custom commnand-line prompt handler '''
import cmd
import sys
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    ''' custom command-line prompt handler based on cmd module '''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    prompt = "(hbnb) "

    def do_EOF(self, line):
        '''Exits the program'''
        return True

    def do_quit(self, line):
        return True

    def help_quit(self):
        print('Quit command to exit the program\n')

    def emptyline(self):
        pass

    """def do_create(self, args):
        ''' Creates a new BaseModel instance and saves it to a file'''
        if args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        elif not args:
            print("** class name missing **")
            return

        else:
            new = HBNBCommand.classes[args]()
            storage.save()
            print(new.id)"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
