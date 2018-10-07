# Duplicate Files

Simple program for finding duplicate files in a directory inputted by the user.

## Project description

### Prerequisites

What things you need to install the software and how to install them

```
Python 3
```

### Additional information

The file simple_script.py is a simple implementation of the problem with a simple script. 
The folder solution contains the solution that could be extended and run in a distributed system.

### Design patterns used

- Template method: 

The files encodefile.py is_duplicate.py and store_files.py define a template for what methods the given classes should have, but doesn't provide implementation. Using this structure, the baseclasses implement the behaviour best for the current task. For example, in the file store_files.py we define a class that has an abstract method add_item. The class StoreFilesSet implements StoreFiles from the aforementioned file and stores the input in a set. In the future, other classes can do the same, providing the freedom to the interface to choose how the files to be stored.
- Iterator : 

In the file duplicates_in_current_directory.py used a built in iterator from "path" library to acess files in a folder without exposing its underlying representation.

## Running the tests

Tests can be run from the main directory with

```
python3 -m unittest
```

### To run individual tests

Add path to test as a parameter to the above command

```
python3 -m unittest test/test_run_duplicates.py
```

## Running project

To ran project type
When asked provide the relative path where to look for duplicates.

```
python3 run_duplicates.py
```

