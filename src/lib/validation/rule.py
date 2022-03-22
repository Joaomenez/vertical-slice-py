from __future__ import annotations
from typing import Any



class Rule:
    def __init__(self, arg: Any, name_arg: str):
        self.arg = arg
        self.name_arg = name_arg
        self.rules = []
    
    def __isnumeric(self, a) -> bool:
        return ( isinstance(a, int)   | 
                isinstance(a, float)  | 
                isinstance(a, complex) )

    def __isiterable(self, a) -> bool:
        return ( isinstance(a, tuple) |
                 isinstance(a, list) |
                 isinstance(a, str) |
                 isinstance(a, bytearray))

    def of_type(self, type):
        if not isinstance(self.arg, type):
            self.rules.append("argument must be a %s" % type.__name__)
            return self.validate()
        return self



    def str_(self):
        return self.of_type(str)
    
    def int_(self):
        return self.of_type(int)
    
    def float_(self):
        return self.of_type(float)
    
    def list_(self):
        return self.of_type(list)
    
    def bool_(self):
        return self.of_type(bool)
    
    def tuple_(self):
        return self.of_type(tuple)
    
    def float_(self):
        return self.of_type(float)
    
    def dict_(self):
        return self.of_type(dict)

    def set_(self):
        return self.of_type(set)

    def grater_than(self, a) -> Rule:
        if not (self.__isnumeric(self.arg) and self.arg > a):
            self.rules.append("argument must be greater than %s" % a)
        return self

    def grater_or_equal_than(self, a) -> Rule:
        if not (self.__isnumeric(self.arg) and self.arg >= a):
            self.rules.append("argument must be greater or equal than %s" % a)
        return self

    def lower_than(self, a) -> Rule:
        if not (self.__isnumeric(self.arg) and self.arg < a):
            self.rules.append("argument must be lower than %s" % a)
        return self
    
    def lower_or_equal_than(self, a) -> Rule:
        if not (self.__isnumeric(self.arg) and self.arg <= a):
            self.rules.append("argument must be lower or equal than %s" % a)
        return self  
    
    def min_length(self, a) -> Rule:
        if not (self.__isiterable(self.arg) and len(self.arg) < a):
            self.rules.append("argument must be of min length %s" % a)
        return self

    
    def min_length_or_equal(self, a) -> Rule:
        if not (self.__isiterable(self.arg) and len(self.arg) <= a):
            self.rules.append("argument must be of min or equal length %s" % a)
        return self

    def max_length(self, a) -> Rule:
        if not (self.__isiterable(self.arg) and len(self.arg) <= a):
            self.rules.append("argument must be of max length %s" % a)
        return self

    def max_length_or_equal(self, a) -> Rule:
        if not (self.__isiterable(self.arg) and len(self.arg) <= a):
            self.rules.append("argument must be of max length or equal %s" % a)
        return self
    
    def includes(self, a) -> Rule:
        if not (self.__isiterable(self.arg) and a in self.arg):
            self.rules.append("argument must include '%s'" % a)
        return self
    
    def between(self, a, b) -> Rule:
        if self.__isnumeric(self.arg) and not (a <= self.arg <= b):
            self.rules.append("argument must be between %s and %s" % (a, b) )
        return self
    
    def equal(self, a) -> Rule:
        if self.arg != a:
            self.rules("argument must be equal to %s" % a)
        return self
    
    def validate(self):
        output = None
        print(self.rules)
        if len(self.rules) > 0:
            output = {
                "argument": self.name_arg,
                "errors": self.rules
            }
        return output