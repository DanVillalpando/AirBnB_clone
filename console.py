#!/usr/bin/python3
"""
6. Console 0.0.1
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Contains the entry point of the command interpreter
    """

    prompt = '(hbnb) '
    my_class = {"BaseModel", "User", "Place", "State",
                "City", "Amenity", "Review"}

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        EOF command (exit)
        """
        return True

    def do_help(self, args):
        """
        Help command
        """
        return cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """
        Empty line execute anything/ignore
        """
        #return cmd.Cmd.emptyline(self)
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        args = args.split(" ")
        if args == "":
            print("** class name missing **")
        if args[0] not in self.my_class:
            print("** class doesn't exist **")
        else:
            new = eval("{}()".format(args[0]))
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
        args = args.split()
        if args == "":
            print("** class name missing **")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            try:
                obj = objects[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file)
        """
        if not args:
            print("** class name missing **")
            return
        i = args.split(" ")
        objects = models.storage.all()

        if i[0] in self.classes:
            if len(i) < 2:
                print("** instance id missing **")
                return
            name = i[0] + "." + i	[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj = objects[name]
                if obj:
                    objs = models.storage.all()
                    del objs["{}.{}".format(type(obj).__name__, obj.id)]
                    models.storage.save()
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        objects = models.storage.all()
        list = []
        if not args:
            for name in objects.keys():
                obj = objects[name]
                list.append(str(obj))
            print(list)
            return
        args = args.split(" ")
        if args[0] in self.my_class:
            for name in objects:
                if name[0:len(args[0])] == args[0]:
                    obj = objects[name]
                list.append(str(obj))
            print(list)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        """
        args = args.split()
        objects = models.storage.all()
        if args == "":
            print("** class name missing **")

        if args[0] not in self.my_class:
            print("** class doesn't exist **")

        if len(args) < 2:
            print("** instance id missing **")

        else:
            k = "{}.{}".format(args[0], args[1])
            if k in objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                if len(args) < 4:
                    print("** value missing **")
                else:
                    obj = objects[k]
                    setattr(obj, args[2], args[3])
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
