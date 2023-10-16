#!/usr/bin/python3
""" Console Module. """
import cmd
from models.base_model import BaseModel
from models import storage
import argparse


class HBNBCommand(cmd.Cmd):
    """This class class is the model of the Console"""
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
        className = argSpl[0]
        if className not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        ni = BaseModel()
        ni.save()
        print(ni.id)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        className = arg[0]
        argSpl = arg.split()
        if not argSpl:
            print("** class name missing **")
            return
        if className not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        if len(argSpl) < 2:
            print("** instance id missing **")
            return
        instId = argSpl[1]
        k = f"{className}.{instId}"
        objDic = storage.all()
        objSave = storage.save()
        if k not in objDic:
            print("** no instance found **")
            return
        else:
            del objDic[k]
            return (objSave)

    def do_show(self, arg):
        """Show the str representation of an instance."""
        argSpl = arg.split()
        if len(argSpl) == 0:
            print("** class name missing **")
            return
        className = argSpl[0]
        if className not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        if len(argSpl) < 2:
            print("** instance id missing **")
            return

        instId = argSpl[1]
        k = "{}.{}".format(className, instId)
        storedObj = storage.all()

        if k in storedObj:
            print(storedObj[k])
        else:
            print("** no instance found **")


    def do_all(self, arg):
        """Prints all string representation of all inst."""
        storedObj = storage.all()
        argSpl = arg.split()
        if argSpl:
            className = arg[0]
            if className not in BaseModel.__subclasses__():
                print("** class doesn't exist **")
                return
            insts = [
                    x for x in storedObj.values()
                    if x.__class__.__name__ == className
            ]
            if not insts:
                print("** no instance found **")
            else:
                for i in insts:
                    print(i)
        else:
            for i in storedObj.values():
                print(i)

    def do_update(self, argSpl):
        """Updates an instance based on class name and id."""
        parser = argparse.ArgumentParser(description="Update an instance")
        parser.add_argument("className", help="Class name")
        parser.add_argument("instId", help="Instance ID")
        parser.add_argument("attName", help="Attribute name")
        parser.add_argument("attVal", help="Attribute value")
        argSpl = parser.parse_args(argSpl.split())
        className = argSpl.className
        instId = argSpl.instId
        attName = argSpl.attName
        attVal = argSpl.attVal
        storedObj = storage.all()
        k = f"{className}.{instId}"

        if not className:
            print("** class name missing **")
            return
        if className not in BaseModel.__classes:
            print("** class doesn't exist **")
            return
        if not instId:
            print("** instance id missing **")
            return

        if k not in storedObj:
            print("** no instance found **")
            return
        x = storedObj[k]
        if not attName:
            print("** attribute name missing **")
            return

        if not attVal:
            print("** value missing **")
            return

        if attName not in ["id", "created_at", "updated_at"]:
            setattr(x, attName, attVal)
            x.save()
        else:
            print(f"** cannot update {attName} **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
