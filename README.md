0x00. AirBnB clone - The console

Project description:
Console is the first step of Airbnb full web application. The repository AirBnB_clone holds the classes(User, State, City, Place, etc that inherit from BaseModel) and command interpreters. Shell command interpreter can be activated. file storage is our first abstract storage engine. The unittests is created to validate all our classes and storage engine.

How to use it:
-Create new object
-Retrieve an object from a file
-Do operations on objects
-Update attributes of an object
-Destroy an object

Installation:
git clone https://github.com/DChipape/AirBnB_clone.git
Change directory to AirBnB_clone

Execution
Interactive mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

Testing:
unittest module will be used for testing

