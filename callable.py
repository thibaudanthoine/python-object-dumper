#!/usr/bin/env python
##
## @file callable.py
## @brief Callable class to emulate static methods.
##
## @details sample usage:
## from callable import Callable
##
## def myRandomFunction(someArg=None):
##     # ... some code
##     return (someVal)
##
## myReturnedValue = Callable(myRandomFunction) # 'myRandomFunction' pseudo-static call
##

class Callable:
    def __init__(self, anycallable):
        self.__call__ = anycallable
