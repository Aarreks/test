# Alex Giang
# Professor Abolghasemi
# CIS 502
# 25 February 2024

# Week 5-2, Exercise 2

# This file is intended to demonstrate beginning knowledge in implementing
# function wrappers to alter the behavior or return values of functions.

class debug:

    def __init__(self, func):
        if isinstance(func, type):
            self.function = debug.debug_all(func)
        else:
            self.function = debug.debug_one(func)

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    def debug_all(cls):
        for name, value in vars(cls).items():
            if callable(value):
                setattr(cls, name, debug.debug_one(value))
        return cls

    def debug_one(func):

        def wrapper(*args, **kwargs):
            try:
                print('Called', func.__name__)
            except AttributeError as e:
                pass
            n = 0
            for i in args:
                n += 1
                print('Attribute', n, 'is', i)
            n = 0
            for j in kwargs.items():
                n += 1
                print('Keyword attribute', n, 'is', j)
            return func(*args, **kwargs)

        return wrapper


@debug
class Calculator:
    def add(self, lhs=0, rhs=0):
        return lhs + rhs


calc = Calculator()
print(type(Calculator))
print(type(calc))
print(type(calc.add))
print(calc.add(3, 5))
print(calc.add(4 + 2j, rhs=-8j))
