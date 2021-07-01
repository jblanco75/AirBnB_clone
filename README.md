## Background and context
Introduction
-----------------------
First part of many others to create a full web application, an **AirBnb clone**.
In this project, the objective is to write a command interpreter to manage AirBnb objects.

Management of the objects include:
-----------------------
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object


The tasks carried out include:
-----------------------
- Create a main class (called BaseModel) that takes care of the initialization, serialization, and deserialization of new instances.
- Create a simple serialization / deserialization flow: Instance <-> Dictionary <-> JSON String <-> file
- Create all the classes used for AirBnB that inherit from BaseModel (User, State, City, Place, Amenities, Review)
- Create a storage engine to be able to save and retrieve data.
- Create all the unittests to validate all the processes

What’s a command interpreter?
-----------------------
The command interpreter is the program that receives what is written in the terminal and converts it into instructions for the operating system. In this case, we create our own command interpreter for the functions that we need for the correct functioning of our Airbnb clone.

## 01. Installation instructions:
[Clone repository](https://github.com/Rode1o/AirBnB_clone)

## Technical Characteristics
* Written in Python3
* PEP8 compliant
* Console created with the module [cmd](https://docs.python.org/3.4/library/cmd.html)
* Tested with the [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g)

## 02. Operation instructions:
How to use the interpreter?
-----------------------

Usage in interactive mode: 
```
$ ./console.py
```
This executes the command interpreter and displays the prompt:
```
(hbnb)
```
and waits for the user to type a command. A command line always ends with a new line. The prompt is displayed again each time a command is executed.

...and in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```

## 03. Usage
Here is an example of how to use our console
-----------------------
```
(hbnb) create BaseModel
de2630a8-7556-4e6d-8b55-8b0a4ba8082d
(hbnb) show BaseModel de2630a8-7556-4e6d-8b55-8b0a4ba8082d
[BaseModel] (de2630a8-7556-4e6d-8b55-8b0a4ba8082d) {'updated_at': datetime.datetime(2021, 2, 18, 18, 4, 12, 756946), 'created_at': datetime.datetime(2021, 2, 18, 18, 4, 12, 756836), 'id': 'de2630a8-7556-4e6d-8b55-8b0a4ba8082d'}
(hbnb) quit
```
Commands the console accepts:
-----------------------
* create: creates a new instance of the class, saves it to the JSON file and prints the id.
Ex: `create BaseModel` (Must be used with existing class, otherwise prints error)
* show: Prints the string representation of an instance based on the class name and id. 
Ex: `show BaseModel 1234-1234-1234` (Must be used with existing class and id, otherwise prints error)
* update: Updates an instance based on the class name and id by adding or updating attributes and saves the changes to the JSON file.
Ex: `update BaseModel 1234-1234-1234 email "airbnb@holbertonschool.com"` (Must be used with existing class and id, otherwise prints error)
* destroy: Deletes an instance based on the class name and id and saves the changes in the JSON file.
Ex `destroy BaseModel 121212` (Must be used with existing class and id, otherwise prints error)
* all: Prints all string representation of all instances based or not on the class name.
Ex `all BaseModel` (shows all instances of class) or `all` (shows all instances of all classes) (Must be used with existing class, otherwise prints error)

The console also accepts the following usage for the previous commands:
-----------------------
* `<class name>.all()`
* `<class name>.count()` (Retrieves the number of instances of a class)
* `<class name>.show(<id>)`
* `<class name>.destroy(<id>)`
* `<class name>.update(<id>, <attribute name>, <attribute value>)`
* `<class name>.update(<id>, <dictionary representation>)`

## 04. File Manifest:
- models
    - engine
        - __init__.py
        - file_storage.py
    - __init__.py
    - amenity.py
    - base_model.py
    - city.py
    - place.py
    - review.py
    - state.py
    - user.py
    - tests
        - __init__.py
        - test_models
            - __init__.py
            - test_amenity.py
            - test_base_model.py
            - test_city.py
            - test_file_storage.py
            - test_place.py
            - test_review.py
            - test_state.py
            - test_user.py
- console.py
- README.md
- AUTHORS

## 05. Copyright and licencing information
Made by [Duvan Rodelo](https://github.com/Rode1o)
and [Jaime Blanco](https://github.com/jblanco75) for Holberton School .

## 06. Contact information for the programmers
#### Duvan Rodelo :
- [Linkedin](https://www.linkedin.com/in/duvanrode1o/)
- [Twitter](https://twitter.com/duvanrode1o)

#### Jaime Blanco:
- [Linkedin](https://www.linkedin.com/)
- [Twitter](https://twitter.com/jblanco75)


## 07. Troubleshooting
* Unittests available [here](https://github.com/Rode1o/AirBnB_clone/tree/main/tests) in case of errors.
* All tests can be executed with the following command:
```
python3 -m unittest discover tests
```
* Tests can also be executed using:
```
python3 -m unittest tests/test_models/test_base_model.py
```
> Finished 30 / 06 / 2021
