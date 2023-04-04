class Person():
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("k1")
p2 = Person("p2")

# print(Person.number_of_people)

print(Person.number_of_people_())


# Static methods

class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10


print(Math.add5(3))
print(Math.add10(3))