print('hi')

for item in 'Python':
    print(item)

for item in ['Mosh', 'John', 'Yenefer']:
    print(item)

for item in range(10):
    print(item)

for item in range(5 , 10):
    print(item)

for item in range(5 , 10 , 3):
    print(item)

prices = [10, 20 ,30]
sum = 0
for price in prices:
    sum+=price

print(sum)

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

numbers = [5,2,5,2,2]

for item in numbers:
    print('x'*item)

print(prices[2])
print(prices[1:])
print(prices[:])
prices[0] = 203
print(prices[0])

#two dimensional list

matrix = [
    [1,2,3],
    [2,3,4],
    [3,4,5]
]

print(matrix)
print(matrix[2][2])

for row in matrix:
    for item in row:
        print(item)


numbers = [2,3,2,4,5]
numbers.append(13)
print(numbers)
numbers.insert(2,43)
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(43))
print(43 in numbers)
print(numbers.count(2))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers2.append(10)

print(numbers)
print(numbers2)

numbers3 = [2,2,3,4,5,3,2,3,4,33]
numbers3_without_duplicates = []
for number in numbers3:
    if number not in numbers3_without_duplicates:
        numbers3_without_duplicates.append(number)
print(numbers3)
print(numbers3_without_duplicates)

