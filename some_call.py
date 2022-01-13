# Implement generator `countdown` which:
#   * takes one argument int: `n`
#   * on iteration returns elements starting from `n` to 0 (inclusive)
# Tests:
#     >>> c = countdown(10)
#     >>> list(c)
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# Solution

def countdown(n):
    while(n >= 0):
        yield n
        n -= 1

c = countdown(10)
print(list(c))

def countdown2(x):
    for element in x:
        yield element

c = countdown2([1, 2, "kot"])
print(list(c))

# c = countdown(8)
# for _ in range(11):
#     next(c)

class Countdown:
    def __init__(self, n):
        self.idx = n + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > 0:
            self.idx -= 1
            return self.idx
        else:
            raise StopIteration

c = Countdown(7)

try:
    for _ in c:
        print(_)
except StopIteration as er:
    print("kot")


# >>> @reduce_pairs
# ... def add(a, b):
# ...    return a + b
# >>> add([1, 2, 3, 4, 5, 6])
# [3, 7, 11]

def reduce_pairs(func):
    list_a = []
    def wrapper(a):
        while(a):
            try:
                x = next(a)
                y = next(a)
                list_a.append(func(x, y))
            except StopIteration as e:
                break
        return list_a
    return wrapper

@reduce_pairs
def add(a, b):
    return a + b

print(add(c))
