#!/usr/bin/python3
""""""

import cmd
import sys
import shlex

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    intro = """

          .-===-
         +*=:.:+*.
        =*-     -*-
      .+*.   ::  -*-             .--:        ::.                    .:.
     .**.  .=*+=. .*-            :**=        **+                    =*+
     +*.   +- :*+  :*+           :**=        **+                    =*+
    +*.  ::===**+   -*-          :**++****-  **+-=++=:   -=--=++-:  =**-=++=:
   =*.   -****+==:   .*-         :***:..=**= ***-::-+**: +**=::=**- =**=-:-+**.
  =*.    +***=.       :*-        :**=   .**+.**+     **+ +*+   .**= =*+     =**
 +*:     .+***+        -*.       :**=   .**+.**+    .**= +*+   .**= =*+    .+*+
-*=        -**:         =*:      :**=   .**+.***+=-=**+. +*+   .**= =**+=-=**+.
*-          :-=         .**      .--:    --- --::-=--.   :-:    --: :-:.-=--.
+=         -*++:        :*+
 .-++++++-:     :=+++++=:

                              .-----------------------.
                              | Welcome to hbnb Clone |
                              | For help, input 'help'|
                              | For quit, input 'quit'|
                              .-----------------------.
    """
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Amenity", "City",
                  "Place", "Review", "State"]


    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_create(self, line):
        """"""
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            line = eval(line)()
            #models.storage.save()
            line.save()
            print(line.id)

    def do_show(self, line):
        """"""
        i = line.split()
        if not line:
            print("** class name missing **")
            return
        elif i[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        elif len(i) == 1:
            print("** instance id missing **")
            return
        data = storage.all()
        key = i[0] + "." + i[1]
        if key not in data.keys():
            print("** no instance found **")
        else:
            print(data[key])

    def do_destroy(self, line):
        """"""
        i = line.split()
        if not line:
            print("** class name missing **")
            return
        elif i[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        elif len(i) == 1:
            print("** instance id missing **")
            return
        data = storage.all()
        key = i[0] + "." + i[1]
        if key not in data.keys():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()
            return
    def do_all(self, line):
        """"""
        i = line.split()
        list_obj = []
        data = storage.all()
        if not line:
            for value in data.values():
                list_obj.append(value.__str__())
            print(list_obj)
        elif i[0] not in self.class_list:
            print("** class doesn't exist **")
        else:
            for key, value in data.items():
                if i[0] in key:
                    list_obj.append(data[key].__str__())
            print(list_obj)

    def do_update(self, line):
        i = shlex.split(line)
        if not line:
            print("** class name missing **")
            return
        elif i[0] not in self.class_list:
            print("** class doesn't exist **")
            return
        elif len(i) == 1:
            print("** instance id missing **")
            return
        data = storage.all()
        key = i[0] + "." + i[1]
        if key not in data:
            print("** no instance found **")
        elif len(i) == 2:
            print("** attribute name missing **")
        elif len(i) == 3:
            print("** value missing **")
        else:
            setattr(data[key], i[2], i[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
