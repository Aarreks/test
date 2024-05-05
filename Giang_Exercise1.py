
# Alex Giang
# Professor Abolghasemi
# CIS 502
# 27 January 2024

# Exercise 1

class Rectangle:

    length: complex
    width: complex

    def __init__(self, length: complex, width: complex) -> None:
        self.length = length + 0.0j
        self.width = width + 0.0j
        assert isinstance(self.length, complex) and isinstance(self.width, complex), \
            'Numbers only! Got types ' + str(type(self.length)) + ' and ' + str(type(self.width))

    def calculate_area(self):
        return self.length * self.width


rectangle1 = Rectangle(4, 9.75)
rectangle2 = Rectangle(6-8j, -2.5)
print('Rectangle 1 has area = height * width =',
      rectangle1.length, '*', rectangle1.width, '=', rectangle1.calculate_area())
print('Rectangle 2 has area = height * width =',
      rectangle2.length, '*', rectangle2.width, '=', rectangle2.calculate_area())

