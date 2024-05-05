# Alex Giang
# Professor Abolghasemi
# CIS 502
# 12 February 2024

# Week 5-2, Exercise 1

# This file is intended to demonstrate beginning knowledge in implementing
# function wrappers to alter the behavior or return values of functions.

from datetime import datetime

def uppercase(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret.upper()
    return inner


@uppercase
def greet(name):
    hour = datetime.now().hour
    if 3 <= hour <= 11:
        return 'Good morning ' + name + '! Make today great.'
    elif 12 <= hour <= 17:
        return 'Good afternoon ' + name + '! Hope your day is going well.'
    else:
        return 'Good evening ' + name + '! Hope you had a pleasant day.'

@uppercase
def work_reminder_scream(name, mins_to_midnight):
    return name + ', it\'s midnight in ' + str(mins_to_midnight) + \
        ' minutes!!\nGet to work, stay at work!'

def work_reminder(name, mins_to_midnight):
    return name + ', it\'s midnight in ' + str(mins_to_midnight) + \
        ' minutes!!\nGet to work, stay at work!'


print(greet('Tom'))
print(greet('Bas'))
print(greet('Marcus'))
print(work_reminder('Vinny', 35))
print(work_reminder_scream('Stas', 20))
