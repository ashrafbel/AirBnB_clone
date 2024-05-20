#!/usr/bin/python3
"""Defines console airbnb"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    "defines command iterpreter"

    prompt = "(hbnb) "
    errors_ = ["** class name missing **", "** class doesn't exist **",
               "** instance id missing **", "** no instance found **",
               "** attribute name missing **", "** value missing **"]
    Classes_ = ["BaseModel", "User", "State", "City", "Amenity",
                "Place", "Review"]

    def do_quit(self, arg):
        """Exit command to close the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to terminate the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of the specified class and print its ID."""
        if arg in HBNBCommand.Classes_:
            NEW_ = eval(arg)()
            NEW_.save()
            print(NEW_.id)
        elif not arg:
            print(self.errors_[0])
        elif arg not in HBNBCommand.Classes_:
            print(self.errors_[1])

    def do_show(self, arg):
        "Display the string representation of an instance with a specified ID."
        arg = arg.split()
        if not arg:
            print(self.errors_[0])
        elif arg[0] not in HBNBCommand.Classes_:
            print(self.errors_[1])
        elif len(arg) < 2:
            print(self.errors_[2])
        elif arg:
            KEY_ = f'{arg[0]}.{arg[1]}'
            if KEY_ in models.storage.all():
                print(models.storage.all()[KEY_])
            else:
                print(self.errors_[3])

    def do_destroy(self, arg):
        "Delete an instance of a class with a specified ID."

        arg = arg.split()
        if not arg:
            print(self.errors_[0])
        elif arg[0] not in HBNBCommand.Classes_:
            print(self.errors_[1])
        elif len(arg) < 2:
            print(self.errors_[2])
        else:
            KEY_ = f"{arg[0]}.{arg[1]}"
            if KEY_ not in models.storage.all():
                print(self.errors_[3])
            else:
                del models.storage.all()[KEY_]
                models.storage.save()

    def do_all(self, arg):
        """Prints all str representations of instance"""
        Args = arg.split()
        instances_ = []
        if not Args:
            for inst in models.storage.all().values():
                instances_.append(str(inst))
        elif Args[0] not in HBNBCommand.Classes_:
            print(self.errors_[1])
        else:
            for KEY_, inst in models.storage.all().items():
                if KEY_.startswith(Args[0]):
                    instances_.append(str(inst))
            print(instances_)

    def do_update(self, args):
        """
        Update instance by adding or modifying attr the class name and ID."
        """
        args = args.split()
        if not args:
            print(self.errors_[0])
        elif args[0] not in HBNBCommand.Classes_:
            print(self.errors_[1])
        elif len(args) < 2:
            print(self.errors_[2])
        else:
            KEY_ = f"{args[0]}.{args[1]}"
            if KEY_ not in models.storage.all():
                print(self.errors_[3])
            elif len(args) < 3:
                print(self.errors_[4])
            elif len(args) < 4:
                print(self.errors_[5])
            else:
                instances_ = models.storage.all()[KEY_]
                setattr(instances_, args[2], eval(args[3]))
                instances_.save()

    def default(self, line):
        """Handle class-specific commands with dot notation."""
        if "." in line:
            spt = line.split(".")
            if len(spt) == 2 and spt[1] == "all()":
                return self.do_all(spt[0])
            elif len(spt) == 2 and spt[1] == 'count()':
                o = [obj for key, obj in models.storage.all().items()
                     if key.startswith(spt[0])]
                c = len(o)
                print(c)
            elif spt[1].startswith('show('):
                spt_ins = spt[1][5:-1].split(',')
                if len(spt_ins) >= 1:
                    instance_id = spt_ins[0].strip(' "')
                    key = f"{spt[0]}.{instance_id}"
                    if key not in models.storage.all():
                        print("** no instance found **")
                    else:
                        print(models.storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
