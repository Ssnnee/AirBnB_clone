# AirBnB clone

## Description 
This is a clone of AirBnb [website](https://www.airbnb.com)

## Project Structures 
+ .
+ models contains all classes used for the entire project. 
+ tests contains all unit tests.
+ models/engine contains all storage classes (using the same prototype).
+ console.py is the entry point of our command interpreter.
+ models/base_model.py file is the base class of all our models.
## Installation and Usage
To use the scripts in this repository, you need to have Python installed on your machine. You can check your Python version using the following command:
```
python --version
```

To execute a script, navigate to the directory containing the script and run the following command:
```
python3 script_name.py
```
Or simply
```
./script_name.py
```
To run the unit test, be sure to be in the root of the project and run :
```
python3 -m unittest discover tests
```

## Note 
The "#!/usr/bin/python3" in first line of all files is called shebang or hashbang. It is used in Unix-like operating systems (such as Linux) to indicate the interpreter that should be used to execute the script.
In the files, it specifies that the Python 3 interpreter located at /usr/bin/python3 should be used to execute the script. This way, when the script is run from the command line, the operating system knows which interpreter to use without needing to explicitly specify it.
