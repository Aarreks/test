# Alex Giang
# Professor Abolghasemi
# CIS 502
# 12 February 2024

# Week 5, Exercise 1

# This file is intended to demonstrate beginning knowledge in implementing
# classes that accept a variable number of keyword arguments.

class Student:
    ssid = 0

    def __init__(self, **kwargs):
        Student.ssid += 1
        self.ssid = Student.ssid
        self.name = kwargs['name'] if 'name' in kwargs.keys() else '(no name)'
        self.age = kwargs['age'] if 'age' in kwargs.keys() else '?'
        self.grade = kwargs['grade'] if 'grade' in kwargs.keys() else '?'

    def __str__(self):
        return "ID# " + str(self.ssid) + " | " + str(self.name) \
            + " | Age " + str(self.age) + " | Grade " + str(self.grade)


s1 = Student(name='Stas Ofitserov', age=18, grade='A+')
s2 = Student(name='Vinayak Sarkar', age=17)
s3 = Student(name='Tom Poultney')
s4 = Student()

print(s1, s2, s3, s4, sep='\n')
