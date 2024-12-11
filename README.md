# PyTesting
A Python library that contains tools for unit testing.

# How to install (with pip)
Since the version 2.1, PyTesting can be installed with pip installer.
To do that, you must type this command in your terminal:

```pip install PyTestingQA```

(Do not worry about the name of the project, PyTestingQA is the PyPi's name of the project,
PyTesting and PyTestingQA are virtually the same).

# How to use
To use the project, you have two options:

### Program execution.
If you execute the program as a main module, it will
print a small description of the project. 

### Tool use.
Instead, if you import the module to your project or 
you build your own code on the library's file, you will
be able to use it directly.

### Example of use.
You can use PyTesting (PyTestingQA) in two main ways, depending of the 
way you import PyTesting:

1st way: You import PyTesting (PyTestingQA) like this:
```
import PyTestingQA
test = [("1+1",2)]
PyTestingQA.PyTesting.UnitaryTests.TestingMethod(test)
```

This is the result of running the code:
```
Test1:  Test (1+1) has returned the expected result (2). 

{('1+1', 2): True}
```

2nd way: You import PyTesting (PytestingQA):
```
import PyTestingQA.PyTesting as PyTesting
test = [("1+1",2)]

PyTesting.UnitaryTests.TestingMethod(test)
```

This is the result of running the code: 
``` 
Test1:  Test (1+1) has returned the expected result (2). 

{('1+1', 2): True}
```

# Remember to read the code's comments, they contain very useful information.
