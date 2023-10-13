#!/usr/bin/python3
""" Console Module. """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """Quit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        return True
    
    def do_help(self, arg):
        """Show help."""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """ empty line """
        pass

    def do_create(self, arg):
        """creating new instance of BaseModel"""
        argSpl = arg.split()
        if len(argSpl) == 0:
            print("** class name missing **")
            return
        elif argSpl[0] not in BaseModel.___subclasses__():
            print("** class doesn't exist **")
            return
        else:
            ni= BaseModel.__classes[argSpl]()
            ni.save()
            print(ni.id)
#

if __name__ == '__main__':
    HBNBCommand().cmdloop()
