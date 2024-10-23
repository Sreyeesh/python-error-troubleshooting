# pdb_debugging_example.py

import pdb

# This will throw a ZeroDivisionError, but we will use pdb to debug it.
def divide(a, b):
    pdb.set_trace()  # This will pause the execution and open the debugger
    return a / b

x = 10
y = 0
result = divide(x, y)  # The debugger will pause here, allowing you to step through

