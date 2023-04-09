"""
callable()
Returns True if some thing is callable, False if not.
"""

class Class:
    pass

def func():
    print("hi")

def func2():
    def inner():
        print("Im inner")

    return inner

func3 = lambda x: x+1
not_func = "Im string"

print(callable(Class))
print(callable(func))
print(callable(func2()))
print(callable(func3))
print(callable(not_func))