#!/usr/bin/python3
"""
6. Console 0.0.1
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter
    """

    prompt = '(hbnb) '

    def do_exit(self, args):
        return True

    def do_EOF(self, args):
        return True

    def do_help(self, args):
        return cmd.Cmd.do_help(self, args)

    def emptyline(self):
        print('emptyline()')
        return cmd.Cmd.emptyline(self)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
