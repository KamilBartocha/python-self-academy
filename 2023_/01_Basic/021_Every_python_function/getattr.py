"""
getattr() - Return the value of the named attribute of object.
"""

class MyClass:
    def __init__(self, x):
        self.x = x

c = MyClass(10)

print(getattr(c, "x"))