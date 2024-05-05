# Alex Giang
# Professor Abolghasemi
# CIS 502
# 3 March 2024

# Week 7, Exercise 1

# This file is intended to demonstrate beginning knowledge in implementing
# generator functions.

class GradeDescriptor(object):

    def __init__(self, min_grade, max_grade):
        self._min_grade = min_grade
        self._max_grade = max_grade

    def __get__(self, instance, owner):
        print('instance:', instance, 'owner:', owner)
        try:
            return instance.name + '\'s grade: ' + str(instance.grade_)
        except AttributeError:
            return instance.name + '\'s grade: ' + 'None'

    def __set__(self, instance, value):
        try:
            assert (self._min_grade <= value + 0.0 <= self._max_grade)
        except TypeError:
            raise ValueError('Grade must be a non-complex number')
        except AssertionError:
            raise ValueError('Grade must be between ' +
                             str(self._min_grade) + ' and ' + str(self._max_grade))
        instance.grade_ = value

    def __delete__(self, instance):
        del instance.grade_


class Student(object):
    grade = GradeDescriptor(0, 100)

    def __init__(self, name):
        self.name = name

    def display_grade(self):
        print(self.grade)


student1 = Student('Alice')
student2 = Student('Bob')

student1.grade = 96
student2.grade = 99.4

student1.display_grade()
student2.display_grade()

try:
    student1.grade = 110
except ValueError as e:
    print(e)

del student2.grade
student2.display_grade()
