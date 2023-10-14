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
        """Creating new instance of BaseModel"""
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
            return
    
    def do_destory(self,arg):
        """Deletes an instance based on the class name and id"""
        className = args[0]
        argSpl = arg.split()
        if not argSpl:
            print("** class name missing **")
            return
        if className not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
    #arg with least 2 comp
        if len(argSpl) < 2:
            print("** instance id missing **")
            return
        instId = arg[1]
        k= f"{className}.{instId}"
        objDic = storage.all()
        objSave = storage.save()
        if k not in objDic:
            print("** no instance found **")
            return

        del objDic[k]
        return (objSave)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
