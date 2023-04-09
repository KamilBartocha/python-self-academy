"""
delattr(object, name)
The function deletes a named attribute.
"""

class MyClass:
    def __init__(self, x):
        self.x = x

c = MyClass(10)

print(c.x)
delattr(c, "x")    # NOTE, second parameter as a str!
                   # del c.x does the same.
print(c.x)