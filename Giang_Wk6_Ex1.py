# Alex Giang
# Professor Abolghasemi
# CIS 502
# 29 February 2024

# Week 6, Exercise 1

# This file is intended to demonstrate beginning knowledge in implementing
# generator functions.

def fibonacci_generator(limit):
    prev1 = 1
    curr = 0
    while curr <= limit:
        yield curr
        prev2 = prev1
        prev1 = curr
        curr = prev2 + prev1


limits = [50, 200, 1000, 5000, 25000, 100000]
for lim in limits:
    fib_seq = fibonacci_generator(lim)
    print("\n\nFibonacci numbers up to", lim, ":")
    for n in fib_seq:
        print(n, end=" ")
