"""
any()
Return 'True' if any element of the iterable is True
"""

a = [1, 0 ,1 ,2 ,3]
print(any(a))

b = [True, True, 1, 2]
print(any(b))

c = ["", "a", "b"]
print(any(c))

d = [0, False, ""]
print(any(d))