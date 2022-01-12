# A decorator is a function that takes a function object as an argument and returns a function as a value
def f1(func):
    """
    basic decorator example
    """
    def wrapper(*args, **kwargs):
        print("started")
        func(*args, **kwargs )
        print("ended")

    return wrapper
@f1
def f(a):
    print(a)

def f2(func):
    def wrapper(*args, **kwargs):
        print("started")
        val = func(*args, **kwargs)
        print("ended")
        return val

    return wrapper

@f2
def g(x):
    return x*x

print(g(3))

def memorize(function):
    """
    make fib run more efficient - save solutions
    """
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            val = function(*args)
            cache[args] = val
            return val
    return wrapper

@memorize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(50))