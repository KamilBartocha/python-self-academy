# variable = a reusable container for storing a value
#            a variable behaves as if it were the value it contains

# INTEGER
age = 21
players = 2
quantity = 5

print(f"You are {age} years old")
print(f"There are {players} players online")
print(f"You would like to buy {quantity} items")

# FLOAT
gpa = 3.2
distance = 2.5
price = 10.99

print(f"Your gpa is {gpa}")
print(f"You ran {distance}Km")
print(f"The price is ${price}")

# STRING
name = "Kamil"
food = "Burgers"
email = "kamilbartocha53@gmail.com"

print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")

# BOOLEAN
online = True
for_sale = False
running = False

print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")
print(f"Game running: {running}")

# tricky questions:

x = 100
y = 100
print(id(x) == id(y))

# swaping
x = 10
y = 20

x, y = y, x
print(x,y)