import converters


print('hi 6')

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def miau(self):
        print("miau")


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.miau()

def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


#importing mogules

import converters
from converters import kg_to_lbs

x = kg_to_lbs(100)

print(converters.kg_to_lbs(20))

