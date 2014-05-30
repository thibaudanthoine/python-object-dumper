Python Object Dumper
====================

Various object dumper tools.

Sample usage
============

```
from dumper import objectDumper

myTestObj = someTestClass("helloWorld42")

objectDumper.dump(myTestObj)
myObjectAsString = objectDumper.toString(myTestObj)

print "as Str:\n %s" % myObjectAsString
```
