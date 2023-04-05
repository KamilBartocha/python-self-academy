# for loop =    a statement that will execute it's block of code
#               a limited amount of times
#
#                     while loop = unlimited
#                     for loop = limited

import time

for i in range(10):
    print(i+1)

for i in range(50,100+1,2):
    print(i)

for i in "String example":
    print(i)

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")


#while loop = perform some code WHILE some condition remains true

# ---------------- EXAMPLE 1 ----------------

name = input("Enter your name: ")

while name == "":
   print("You did not enter your name!")
   name = input("Enter your name: ")

print(f"Hello {name}")

# ---------------- EXAMPLE 2 ----------------

age = int(input("Enter your age: "))

while age < 0:
   print("Age can't be negative")
   age = int(input("Enter your age: "))

print(f"You are {age} years old")


# ---------------- EXAMPLE 3 ----------------

food = input("Enter a food you like (q to quit): ")

while not food == "q":
   print(f"You like {food}")
   food = input("Enter another food you like (q to quit): ")

print("bye")

# ---------------- EXAMPLE 4 ----------------

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"You picked the number {num}")


# nested loop = A loop within another loop (outer, inner)
#                          outer loop:
#                              inner loop:

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
   for y in range(columns):
       print(symbol, end="")
   print()