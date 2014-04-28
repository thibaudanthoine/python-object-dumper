#!/usr/bin/env python
##
## @file dumper.py
## @brief Various object dumper tools
##
## @details sample usage:
## from dumper import objectDumper
##
## myTestObj = someTestClass("helloWorld42")
## objectDumper.dump(myTestObj)
##
## Or
##
## myObjectAsString = objectDumper.toString(myTestObj)
## print "as Str:\n %s" % myObjectAsString
##
## Sample output:
##
## obj.__doc__ = None
## obj.__init__ = <bound method someTestClass.__init__ of <__main__.someTestClass instance at 0xb778a9ac>>
## obj.__module__ = __main__
## obj._someOtherVar = None
## obj._someVar = helloWorld42

from callable import Callable

class objectDumper:

    ##
    ## @brief returns a string representation of given object attributes
    ## @return string multi-line string, listing object attributes and their values
    ##
    def toString(obj, prefix = None, format = None):
        
        if format == 'dictionary':
            output_format = "%s %s : %s,"
        else:
            output_format = "%s\nobj.%s = %s"
        
        returnedString = ''
        for attr in dir(obj):
            if prefix == None or attr.find(prefix) == 0:
                returnedString = output_format % (returnedString, attr, getattr(obj, attr))
        return (returnedString)
    
    toString = Callable(toString)   # makes pseudo-static

    ##
    ## @brief dump given object as a string (attributes)
    ##
    def dump(obj):
        returnedString = objectDumper.toString(obj)
        print returnedString
    dump = Callable(dump)   # makes pseudo-static
