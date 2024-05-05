# Alex Giang
# Professor Abolghasemi
# CIS 502
# 11 March 2024

# Week 8, Exercise

# This file is intended to demonstrate beginning knowledge in implementing
# operator overloading.

import threading


class ComplexNumber:
    def __init__(self, real, imag=0):
        self.re = real
        self.im = imag

    def __add__(self, other):
        return ComplexNumber(
            self.re + other.re,
            self.im + other.im
        )

    def __sub__(self, other):
        return ComplexNumber(
            self.re - other.re,
            self.im - other.im
        )

    def __mul__(self, other):
        return ComplexNumber(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re
        )

    def recip(self):
        conj = ComplexNumber(self.re, -self.im)
        den = (self * conj).re
        return ComplexNumber(
            conj.re / den,
            conj.im / den
        )

    def __truediv__(self, other):
        return self * ComplexNumber.recip(other)

    def __str__(self):
        return str(self.re) + ' + ' + str(self.im) + 'i'


if __name__ == "__main__":
    num1 = ComplexNumber(2, 3)
    num2 = ComplexNumber(1, 4)

    # Perform addition
    sum_result = num1 + num2
    print("Addition Result:", sum_result)

    # Perform subtraction
    sub_result = num1 - num2
    print("Subtraction Result:", sub_result)

    # Perform multiplication
    mul_result = num1 * num2
    print("Multiplication Result:", mul_result)

    # Perform division
    div_result = num1 / num2
    print("Division Result:", div_result)

    # Perform division

