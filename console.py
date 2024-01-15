#!/usr/bin/python3
""" A custom commnand-line prompt handler """
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
    """ custom command-line prompt handler based on cmd module """

    classes = {
               'BaseModel': BaseModel, 'Place': Place, 'User': User,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exits the program"""
        return True

    def help_EOF(self):
        """ The help documentation for the EOF command """
        print("       Exits the program\n\
       Usage: EOF")

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def help_quit(self):
        """ The help documentation of the <quit> command """
        print("       Quit command to exit the program.\n\
       Usage: quit")

    def emptyline(self):
        """ Handles the empty line command """
        pass

    def do_create(self, args):
        """ Creates a new BaseModel instance and saves it to a file"""

        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            new = HBNBCommand.classes[args]()  # create a new instance
            storage.save()
            print(new.id)

    def help_create(self):
        """ The help documentation of the <create> command """
        print("       Creates a new instance and saves it.\n\
       Usage: create <className>")

    def do_show(self, args):
        """ prints the string representation of a class instance """

        if not args:
            print("** class name missing **")
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

    def help_show(self):
        """ The help documentation of the <show> command """
        print("       Show the instance associated with an id.\n\
       Usage: show <class-name> <instanceId>")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name
            and id (save the change into the JSON file) """
        import json

        if not args:
            print("** class name missing **")
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
            data = {}
            with open(storage._FileStorage__file_path, 'r') as f:
                data = json.load(f)
            del data[clss]
            del storage._FileStorage__objects[clss]
            with open(storage._FileStorage__file_path, 'w') as f:
                json.dump(data, f)

        except KeyError:
            print("** no instance found **")

        except FileNotFoundError:
            pass

    def help_destroy(self):
        """ The help documentation of the <destroy> command """
        print("       Deletes an instance based on the class name\
and id and saves the change into the JSON file.\n\
       Usage: destroy <class-name> <instanceId>")

    def do_all(self, args):
        """ Prints all instances of a given class or all classes """

        if not args:
            li = []
            for i in storage._FileStorage__objects:
                li.append(str(storage._FileStorage__objects[i]))
            print(li)
            return

        if len(storage._FileStorage__objects) == 0:
            print("[]")

        else:
            arguments = args.split(' ')
            arg1 = arguments[0]
            li = []

            for h in range(0, len(arguments)):
                arg = arguments[h]
                if arg not in HBNBCommand.classes:
                    print("** class doesn't exist **")
                    pass
                for i in storage._FileStorage__objects:
                    temp = i.split(' ')
                    temp = temp[0].split('.')
                    temp = temp[0]

                    if arg == temp:
                        li.append(str(storage._FileStorage__objects[i]))
            if len(li) > 0:
                print(li)

    def help_all(self):
        """ The help documentation for the <all> command """

        print("       Displays all the information about given instances.\n\
       Usage: all\n              all <class-name>\n\
              all <class-name1> <class-name2> and so on")

    def do_update(self, args):
        """ Updates a given class instance """

        if not args:
            print("** class name missing **")
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
            if len(arguments) < 3:
                print("** attribute name missing **")
                return
            arg3 = arguments[2].strip('\"')
            if len(arguments) < 4:
                print("** value missing **")
                return
            arg4 = arguments[3].strip('\"')
            li = storage.all()[clss]
            li.__dict__.update({arg3: arg4})
            li.save()
        except KeyError:
            print("** no instance found **")

    def help_update(self):
        """ The help documentation of <update> command """
        print("       Updates the value of an instance's attribute\n\
       Usage: update <class-name> <instanceId> <attribute> <value>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
