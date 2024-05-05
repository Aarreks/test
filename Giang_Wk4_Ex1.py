
# Alex Giang
# Professor Abolghasemi
# CIS 502
# 12 February 2024

# Week 4, Exercise 1

# This file is intended to demonstrate beginning knowledge in implementing custom metaclasses
# by implementing a simple metaclass that counts attributes.

def count_attr_in(cls):
    '''class decorator make use of debug decorator
       to debug class methods '''
    print("You've instantiated an object of type", cls)
    print("Here are its attributes:")
    i = 0
    for key in vars(cls).keys():
        i += 1
        print("\tAttribute", i, "is", key)
    print("That's", i, "attributes outside __dict__ and including __dict__.")
    print("This includes", i-6, "function(s) that do not come by default.")
    return None


class AttributeLoggerMeta(type):
    '''meta class which feed created class object
       to debugmethod to get debug functionality
       enabled objects'''

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        count_attr_in(obj)
        return obj


# base class with metaclass 'AttributeLoggerMeta'
# now all the subclass of this
# will have debugging applied
class AttributeCounter(metaclass=AttributeLoggerMeta):
    def __init__(self, waist=0.8, height=1.7):
        self.waist = waist
        self.height = height

    def is_healthy(self):
        return 0.37 < self.waist / self.height < 0.52

    def tell_dict_attr(self):
        print("I have", len(self.__dict__), "attributes inside of __dict__:")
        i = 0
        for key in self.__dict__.keys():
            i += 1
            print("\t__dict__ Attribute", i, "is", key)
        print("This list does not include functions, only non-callable attributes.")



# Now DerivedClass object showing
# attribute logging behaviour
my_body = AttributeCounter(0.89, 1.82)
print("But also,")
my_body.tell_dict_attr()
print("Called is_healthy from DerivedClass and got:", my_body.is_healthy())
print(my_body.__weakref__)