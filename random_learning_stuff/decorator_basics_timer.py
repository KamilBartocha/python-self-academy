import time
def decorator(func):
    """Basic dummy decorator(no args handling, no return val handling)"""
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper


@decorator
def f1():
    print("I am f1")

f1()


def decorator2(func):
    """Handling 1 argument added"""
    def wrapper(x):
        print("Started")
        func(x)
        print("Ended")
    return wrapper


@decorator2
def f2(x):
    print("I am f2 ", x)

f2(2)

def decorator3(func):
    """Handling arguments added"""
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    return wrapper


@decorator3
def f3(x, y):
    print("I am f3 ", x, y)

f3(2, 3)


def decorator4(func):
    """Handling multiple args and return value"""
    def wrapper(*args, **kwargs):
        print("Started")
        rv = func(*args, **kwargs)
        print("Ended")
        return rv
    return wrapper

@decorator4
def f4(z):
    print("I am f4", z)
    return z

val = f4(4)
print(val)


def timer(func):
    """Calculates and returns time of execution of an function"""
    def wrapper():
        start_time = time.time()
        rv = func()
        total_time = time.time() - start_time
        print(f"Total time: {total_time}")
        return rv
    return wrapper

@timer
def f_timer():
    for _ in range(100000):
        pass

@timer
def f_timer2():
    time.sleep(2)

f_timer()
f_timer2()
