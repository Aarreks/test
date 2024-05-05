# Alex Giang
# Professor Abolghasemi
# CIS 502
# 11 March 2024

# Week 10, Exercise

# This file is intended to demonstrate beginning knowledge in implementing
# lambda functions -- anonymous and single-expression but compact functions.

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
# Note: assignment directions indicated that name
# length must be strictly above 5 so only Charlie meets
# such criteria.
selected_students = list(filter(lambda s: len(s) > 5, students))
print(selected_students)

