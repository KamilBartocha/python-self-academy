# YiELD The <yield> keyword can turn any function into a generator. Yields work like a standard return keyword

def fibgen(n):
    a0, b0 = 0, 1
    for _ in range(n):
        yield a0
        a0, b0 = b0, a0 + b0

# print(list(fibgen(100)))

def gen_fib():
    print(locals())
    first = 1
    print(locals())
    yield first
    print(locals())
    last = 1
    print(locals())
    yield last
    while True:
        print(locals())
        yield first + last
        first, last = last, first + last

x = gen_fib()
x.__next__()
x.__next__()
x.__next__()
x.__next__()