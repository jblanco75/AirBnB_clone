#!/usr/bin/python3
"""contains the entry point of the command interpreter"""

import cmd
import json
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
    """HBNBNCommand interpreter implementation"""

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
        """method to bypass empty line entered and not execute prev.
        command."""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id. Ex: $ create BaseModel"""
        if not line:
            print("** class name missing **")
        elif line not in self.class_list:
            print("** class doesn't exist **")
        else:
            line = eval(line)()
            line.save()
            print(line.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on
        the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
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
        """Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy
        BaseModel 1234-1234-1234"""
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
        """Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all"""
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
        """Updates an instance based on the class name and id by
        adding or updating attribute."""
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
