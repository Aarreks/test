
# Alex Giang
# Professor Abolghasemi
# CIS 502
# 27 January 2024

# Week 3, Exercise 1

# This file is intended to demonstrate beginning knowledge in nested list comprehensions with conditional statements
# using a simple numerical example.

# solution using conditionals (main submission)
solution1 = [i**2 for i in range(1, 21) if i % 4 == 0]
print("Squares of even numbers between 1 and 20 divisible by 4:", solution1)

# alternate solution using generator (all even numbers' squares are already divisible by 4)
solution2_generator = (j**2 for j in range(2, 21, 2))
print("All squares of even numbers between 2 and 20 using generator:")
[print(k) for k in solution2_generator]
