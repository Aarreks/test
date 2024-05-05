
# Alex Giang
# Professor Abolghasemi
# CIS 502
# 31 January 2024

# Week 3, Exercise 2

# This file is intended to demonstrate beginning knowledge
# in dictionary comprehensions with conditional statements
# using a simple numerical example of country populations.

countries = ['USA', 'China', 'India', 'Brazil', 'Finland', 'Pakistan', 'UAE']
populations = [331, 1441, 1393, 213, 5, 231, 9]

output_dict = {countries[i]: populations[i] ** 2
               for i in range(min(len(countries), len(populations))) if populations[i] >= 100}

print("Countries with over 100 million people and their squared populations:", output_dict)
