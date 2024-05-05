
# Alex Giang
# Professor Abolghasemi
# CIS 502
# 12 February 2024

# Week 4, Exercise 2

# This file is intended to demonstrate beginning knowledge in implementing custom metaclasses
# by implementing a simple metaclass that logs attributes, and how derived
# classes inherit changes to the metaclass.


def log_one(attr, val, cls):
    '''decorator for debugging passed function'''

    print("Created ", attr, "in class", cls, "\nwith value", val, "!!!\n")


def log_attr_in(cls):
    '''class decorator make use of debug decorator
       to debug class methods '''

    for key, val in vars(cls).items():
        log_one(key, val, cls)
    return cls


class AttributeLoggerMeta(type):
    '''meta class which feed created class object
       to debugmethod to get debug functionality
       enabled objects'''

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        print('cls:', cls, 'clsname:', clsname, 'bases', bases, 'clsdict', clsdict)
        obj = log_attr_in(obj)
        return obj


# base class with metaclass 'AttributeLoggerMeta'
# now all the subclass of this
# will have debugging applied
class LoggerBase(metaclass=AttributeLoggerMeta): pass


# inheriting LoggerBase
class DerivedClass(LoggerBase):

    def __init__(self, waist=0.8, height=1.7):
        self.waist = waist
        self.height = height

    def is_healthy(self):
        return 0.37 < self.waist / self.height < 0.52

    def more_attributes(self):
        for attr, val in self.__dict__.items():
            print("There exists attribute", attr, "in object of class\n", type(self), "with value", val, "!!!\n")
            return "That's all the attributes I have."



# Now DerivedClass object showing
# attribute logging behaviour
my_body = DerivedClass(0.89, 1.82)
print("Called is_healthy from DerivedClass and got:", my_body.is_healthy())
print(my_body.more_attributes())