def calculate_fibb(n):
    """calculate n-th fibb seq num"""
    if n == 1:
        return 0
    fibb_list = [0, 1]
    while(len(fibb_list) < n):
        fibb_list.append(fibb_list[-1] + fibb_list[-2])
    return fibb_list[-1]

def calculate_fibb_for(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


def calculate_fibb_rec(n):
    """Calculate fibb sequence using recursion"""
    if n == 1 or n == 2:
        return 1
    return(calculate_fibb_rec(n - 1) + calculate_fibb_rec(n - 2))


def calculate_fibb_yield(n):
    """Calculate fibb sequence using yield"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(calculate_fibb(0))
print(calculate_fibb_for(0))
print(calculate_fibb_rec(11))
print(list(calculate_fibb_yield(100)))
