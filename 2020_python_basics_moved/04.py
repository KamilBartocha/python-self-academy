#04

#tuples

numbers = (1,2,3)
print(numbers[0])

coordinates = (1,2,3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

sum = x * y * z
a, b, c, = coordinates #wors for list also
print(a)

#dictionary

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("age"))

customer["name"] = "Jack"
print(customer["name"])

numbers2 = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine"
}

number = input("Phone: ")
output = ""
for i in number:
    output += numbers2.get(i,"!") + " "
print(output)

message = input(">")
words = message.split(' ')
print(words)

##### function #####

def greet_user():
    print('hi!')


print("start")
greet_user()
print("finish")

def greet_user_param(name):
    print('hi! ' + name)


print("start")
greet_user_param("John")
greet_user_param("Johan")
print("finish")
