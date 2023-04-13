# filter(func, iterable)

a = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9, 10]

def add7(x):
    return x + 7

def is_odd(x):
    return x % 2 != 0


b = list(filter(is_odd, a)) # is_odd return True -> add value to list
print(b)

c = list(map(add7, filter(is_odd, a)))
print(c)