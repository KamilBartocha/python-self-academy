import timeit
import numpy
# basic sum form 0 to n-1

def while_loop_speed(n=100_000_000):
    idx = 0
    sum = 0
    while idx < n:
        sum += idx
        idx += 1
    return sum


def for_loop_speed(n=100_000_000):
    sum = 0
    for idx in range(n):
        sum += idx
    return sum


def sum_builtin_speed(n=100_000_000):
    return sum(range(n))


def sum_numpy_speed(n=100_000_000):
    return numpy.sum(numpy.arange(n))


def main():
    print('while loop \t', timeit.timeit(while_loop_speed, number=1))
    print('for loop \t', timeit.timeit(for_loop_speed, number=1))
    print('sum built-in \t', timeit.timeit(sum_builtin_speed, number=1))
    print('sum numpy\t', timeit.timeit(sum_numpy_speed, number=1))



if __name__ == '__main__':
    main()

"""
Result:
while loop       7.039948624998942
for loop         4.3902550829989195
sum built-in     1.359557624997251
sum numpy        0.1718235830012418

explanation:
 - in for loop C language takes care of range, only incrementation in python
 - in while loop condition check and incrementation is done in python
 - built-in is better than incrementing in python
 - numpy the best, but needs a lot of memory

"""