"""
abs()
Return the absolute value of a number. The argument may be an integer,
a floting point, or an object implementing __abs__().
"""

class ImplementAbs:
    def __init__(self, string):
        self.string = string

    def __abs__(self):
        """ Converts string to lower """
        return self.string.lower()


test_object = ImplementAbs("Hi Kamil")

x = abs(-9)
y = abs(-32.32)
z = abs(test_object)

print(x, y, z)