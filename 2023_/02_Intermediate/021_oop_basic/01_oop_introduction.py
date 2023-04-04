class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name

    def bark(self):
        print("wof")

    def add_one(self, x):
        return x + 1


d = Dog("Azor", 3)
d2 = Dog("Bill", 4)

print(d.get_age())

print(d2.name)
print(d.bark())
print(type(d))
print(d.add_one(5))