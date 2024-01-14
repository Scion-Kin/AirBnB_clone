#!/usr/bin/python3
''' A custom commnand-line prompt handler '''
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


class HBNBCommand(cmd.Cmd):
    ''' custom command-line prompt handler based on cmd module '''

    classes = {
               'BaseModel': BaseModel, 'Place': Place, 'User': User,
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

    def do_create(self, args):
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
            print(new.id)

    def do_show(self, args):
        ''' prints the string representation of a class instance '''

        if not args:
            print("** class name is missing **")
            return
        
        arguments = args.split(' ')
        arg1 = arguments[0]
        if arg1 not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(arguments) >= 2:
            arg2 = arguments[1]
        else:
            print("** instance id missing **")
            return

        clss = arg1 + '.' + arg2
        try:
            print(storage._FileStorage__objects[clss])
        except KeyError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
