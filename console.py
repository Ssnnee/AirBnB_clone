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
    


    def do_show(self, arg):
        """display str representation of an inst."""
        className= arg_list[0]
        argList = pars(arg)
        instId = arg_list[1]
        if len(argList) == 0:
            print("** class name missing **")
            return
        if className not in BaseModel.__subclasses__():
            print("** class doesn't exist **")
            return
        if len(argList) == 1:
            print("** instance id missing **")
            return
        k = "{}.{}".format(className, instId)
        storedObj = storage.all()
        if k in storedObj:
            print(storedObj)
        else:
            print("** no instance found **")
    

    def do_all(self, arg):
        """Prints all string representation of all inst."""
        storedObj = storage.all()
        argSpl = arg.split()
        if argSpl:
            className = args[0]
            if className not in BaseModel.__subclasses__():
                print("** class doesn't exist **")
                return
            insts [x for x in storedObj.values() if x.__class__.__name__ == className]
            if not insts:
                print("** no instance found **")
            else:
                for i in insts:
                    print(i)
        else:
            for i in storedObj.values():
                print(i)

    def do_update(seld, arg):
        """Updates an instance based on the class name and id."""
         argSpl = argSpl.split()

    if len(argSpl) == 0:
        print("** class name missing **")
        return

    className = argSpl[0]

    if className not in HBNBCommand.__classes:
        print("** class doesn't exist **")
        return

    if len(argSpl) == 1:
        print("** instance id missing **")
        return

    instId = argSpl[1]
    storedObj = storage.all()
    k = f"{className}.{instId}"

    if k not in storedObj:
        print("** no instance found **")
        return

    if len(argSpl) < 4:
        print("** attribute name or value missing **")
        return

    attName = argSpl[2]
    attVal = argSpl[3]
    x = storedObj[k]

    if attName not in ["id", "created_at", "updated_at"]:
        setattr(x, attName, attVal)
        x.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
