"""
all()
Return 'True' if all elements of the iterable are True
"""

a = [1, 0 ,1 ,2 ,3]
print(all(a))

b = [True, True, 1, 2]
print(all(b))

c = ["", "a", "b"]
print(all(c))