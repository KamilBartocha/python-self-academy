def is_prime(x):
    y = int(x/2)
    for i in range(2 , y+1):
        if x % i == 0:
            return False
    return True

number_of_tests = 0
number_of_tests = int(input())

for x in range(number_of_tests):
    a, b = input().split(" ")
    n = int(a)
    m = int(b)
    if n ==1:
        n+=1

    for number in range(n,m+1):
        if is_prime(number):
            print(number)
    print(''
          '')
