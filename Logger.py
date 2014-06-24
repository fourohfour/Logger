import time
from enum import Enum

# Types of log. Add more if needed.
#  A new type can be added with a new line such as:
#  SUCCESS = 2
#  Note that all types should have unique numerical values

class LogType(Enum):
    INFO = 0
    WARNING = 1

class Logger:
    def __init__(self, autoprint, header, timeformat = None):
        assert(isinstance(autoprint, bool))
        if timeformat == None:
            self.tf = "%H:%M:%S"
        else:
            self.tf = timeformat
        
        self.ap = autoprint
        self.l = [header]
        self.pointer = 0

        if autoprint:
            print(self.l[0])

    def log(self, ltype, logtext):
        tnow = time.strftime(self.tf)

        tolog = "[" + tnow + " " + ltype.name + "] " + logtext
        self.l.append(tolog)
        if self.ap:
            print(tolog)

    def getNew(self):
        return self.l[self.pointer:]
        self.pointer = len(self.l)

    def printNew(self):
        for i in self.l[self.pointer:]:
            print(i)
        self.pointer = len(self.l)

    def getAll(self):
        return self.l

    def printAll(self):
        for i in self.l:
            print(i)

    def resetPointer(self):
        self.pointer = 0

    def getPointer(self):
        return self.pointer

    def setPointer(self, p):
        self.pointer = p
        if self.pointer < 0:
            self.pointer = 0
            
        if self.pointer > len(self.l):
            self.pointer = len(self.l)

    def incrementPointer(self, amount = 1):
        self.pointer += amount
        
        if self.pointer > len(self.l):
            self.pointer = len(self.l)

    def decrementPointer(self, amount = 1):
        self.pointer -= amount
        if self.pointer < 0:
            self.pointer = 0
