"""
filter(function, iterable)
Constructs an iterator from those elements of iterable for with function
returns True.
"""

def filter_func(value):
    return value % 2 ==0

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = filter(filter_func, lst)    # evens - filter object, iterable
evens2 = filter(lambda x: x % 2 == 0, lst)

print(evens)
print(evens2)

print(list(evens))
print(list(evens2))

