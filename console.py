#!/usr/bin/python3
''' A custom commnand-line prompt handler '''
import cmd


class HBNBCommand(cmd.Cmd):
    def do_EOF(self, line):
        '''Exits the program'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def help_(self):
        ''' Helps with available shell command'''
        help()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
