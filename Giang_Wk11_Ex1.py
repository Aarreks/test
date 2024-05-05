# Alex Giang
# Professor Abolghasemi
# CIS 502
# 11 March 2024

# Week 11, Exercise 1

# This file is intended to demonstrate beginning knowledge in implementing
# dependency injections.

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2


class ShapeWrapper:
    def __init__(self, shape):
        self.shape = shape

    def calculate_area(self):
        return self.shape.calculate_area()

    def extended_functionality(self):
        return (self.calculate_area() / 3.1416) ** 0.5


# Test
square = Square(5)
wrapper = ShapeWrapper(square)
print("Area:", wrapper.calculate_area())
print("This has the same area as a circle with radius "
      "{:.3f}".format(wrapper.extended_functionality()))

