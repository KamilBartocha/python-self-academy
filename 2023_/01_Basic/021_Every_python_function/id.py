"""
id() - Return the "identity" of an object.
"""

x = [1, 2, 3]
y = x
a = 100000
b = a + 1 - 1

print(id(x))
print(id(y)) # ref to the same object - same id
print()
print(id(a))
print(id(b))
