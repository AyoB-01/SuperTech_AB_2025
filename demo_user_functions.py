#! usr/bin/env python3
# Author: ABabalola
# Description: This script will demo how to define name and exit
# a user function with optional parameter, default values and optional
# return value

"""
DOCSTRING
"""
#Example of a user function with optional
# parameter passing [(*,)] enforces named passing
# = in function call puts a DEFAULT value in
# Can add annotations to function

def say_hello(greeting:str, recipient:str="doston")->None:

    message = str(greeting) + " " + str(recipient)
    print(message)
    return

say_hello("hello", "my friends")
