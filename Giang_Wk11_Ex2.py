# Alex Giang
# Professor Abolghasemi
# CIS 502
# 11 March 2024

import math


# Week 11, Exercise 2

# This file is intended to demonstrate beginning knowledge in implementing
# callback functions.

def callback_function(message):
    print(message)


def perform_operation(*args):
    n_sides, side_len, *_ = args
    apothem = side_len / 2 / math.tan(3.1416/n_sides)
    area = n_sides * side_len * apothem / 2
    result = "The area of a {:.1f}-gon with side length" \
        " {:.3f} is {:.3f}".format(n_sides, side_len, area)
    callback_function(result)


perform_operation(5, 69.42, 0, -12002)
