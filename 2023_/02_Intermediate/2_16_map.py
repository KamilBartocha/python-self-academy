# map(func, iterable)

li = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9, 10]

def func_power(x):
    return x**x


# normal approach
new_list = []
for x in li:
    new_list.append(func_power(x))
print(new_list)

# map usage

print(list(map(func_power, li)))
