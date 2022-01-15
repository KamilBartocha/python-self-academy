from random import random, randint
# convert a list into a string
list_days = ['Monday', 'Thursday', 'Wednesday', 'Tuesday', 'Friday', 'Saturday', 'Sunday']
list_as_string = ''.join(list_days)
print(list_days, list_as_string)

# converting list into a tuple
list_days = ['Monday', 'Thursday', 'Wednesday', 'Tuesday', 'Friday', 'Saturday', 'Sunday']
list_as_tuple = tuple(list_days)
print(list_days, list_as_tuple)

# converting list into a set
list_days = ['Monday', 'Thursday', 'Wednesday', 'Tuesday', 'Friday', 'Saturday', 'Sunday']
list_as_set = set(list_days)
print(list_days, list_as_set)
# count the occurrences of a particular element in the list

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print(weekdays.count('mon'))

weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
list_count_correct = [[x, weekdays.count(x)] for x in set(weekdays)] # remove duplicats
list_count_wrong = [[x, weekdays.count(x)] for x in weekdays]
print(list_count_correct, '\n', list_count_wrong)

# set

items = set()
items.add("Python")
items.add("coding")
items.add("tips")
print(items)

# generate random numbers in Python
x = random()
print(x)
y = randint(10, 70)
print(y)

# sum from 1 to 100
print(sum(range(1,101)))

# set a global variable inside a function
globvar = 0
def set_globvar_to_one():
    global globvar # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print(globvar) # No need for global declaration to read value of globvar

set_globvar_to_one()
print_globvar() # Prints 1

# mutable list example

names1 = ['Amir', 'Bear', 'Charlton', 'Daman']
names2 = names1
names3 = names1[:]

names2[0] = 'Alice'
names3[1] = 'Bob'

sum = 0
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10

print(sum)

# list multiplication
list_a = [1, 2, 3]
print(list_a * 2)

# reverse a number in Python

n = 123
rev_n = 0
while(n>0):
    dig = n%10
    rev_n = rev_n*10 + dig
    n = n//10
print(rev_n)

#23 todo

x = 120093492
y = str(x)
print(y[::-1])

x1 = ["doa","doac","dao"]
print("".join(x1))
