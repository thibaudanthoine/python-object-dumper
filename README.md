Python Object Dumper
====================

A python object dumper tool.

Sample usage
============

```
from dumper import objectDumper

myTestObj = someTestClass("helloWorld42")

objectDumper.dump(myTestObj)
myObjectAsString = objectDumper.toString(myTestObj)

print "as Str:\n %s" % myObjectAsString
```
